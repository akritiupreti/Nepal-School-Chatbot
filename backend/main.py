from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from rag_pipeline import rag_chain

app = FastAPI(title="School Finder RAG API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class Query(BaseModel):
    query: str

@app.post("/query")
def query_rag(data: Query):
    answer = rag_chain.invoke(data.query)

    return {
        "answer": answer,
    }