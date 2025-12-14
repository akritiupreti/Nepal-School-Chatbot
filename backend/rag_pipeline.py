import os
import boto3
from dotenv import load_dotenv

from langchain_aws import ChatBedrock, BedrockEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langsmith import traceable

load_dotenv()

# AWS Bedrock client
bedrock_client = boto3.client(
    service_name="bedrock-runtime",
    region_name=os.getenv("AWS_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    aws_session_token=os.getenv("AWS_SESSION_TOKEN")
)

# LLM
llm = ChatBedrock(
    client=bedrock_client,
    model_id="amazon.nova-lite-v1:0",
    temperature=0
)

# Load data
loader = CSVLoader("data/schools.csv")
docs = loader.load()

# Split
splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# Embeddings + Vector DB
embeddings = BedrockEmbeddings(
    client=bedrock_client,
    model_id="amazon.titan-embed-text-v2:0"
)

DB_PATH = "db/chroma"

db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=DB_PATH
)

retriever = db.as_retriever(search_kwargs={"k": 5})

# Prompt (PDO)
prompt = PromptTemplate(
    template="""
You are an educational advisor chatbot that helps students and parents find the best school or college.

Follow PDO:
• **P**recise: Use ONLY the provided context.
• **D**eterministic: If answer is missing, say: "I don't know based on the provided information."
• **O**bjective: Provide unbiased, factual responses.

Context:
{context}

User Question:
{question}

Final Answer:""",
    input_variables=["context", "question"]
)

# RAG Chain
rag_chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser()
)