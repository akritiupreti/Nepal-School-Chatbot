# 🎓 School & College Finder – RAG Based Chatbot (Nepal)

A Retrieval-Augmented Generation (RAG) based chatbot that helps students and parents find **schools and colleges in Nepal** based on queries such as board type, level, location, facilities, and programs.

The system combines **semantic search** over a structured CSV dataset with **LLM-based reasoning** using **AWS Bedrock**.

---

## 🚀 Features

- Natural language search for schools & colleges in Nepal
- Supports queries like:
  - Schools offering **NEB**
  - +2 colleges with **A Levels**
  - Schools with **hostel facilities**
- Retrieval-Augmented Generation (RAG) architecture
- Persistent vector database using **ChromaDB**
- Backend API built with **FastAPI**
- Frontend UI built with **Streamlit**
- Uses **AWS Bedrock** for embeddings and LLM

---

## 🧠 Tech Stack

- **Python 3.10+**
- **FastAPI** – Backend API
- **Streamlit** – Frontend UI
- **LangChain** – RAG pipeline
- **ChromaDB** – Vector database
- **AWS Bedrock**
  - `amazon.nova-lite-v1`
  - `amazon.titan-embed-text-v2`
- **Boto3**
- **Pydantic**

---

## ⚙️ Installation & Setup (Local)

Create a `.env` file in root directory:
```
AWS_REGION=your_region
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_SESSION_TOKEN=your_session_token
```

### Backend Setup

```
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend Setup

```
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

## 📡 API Endpoints

### 🔹 Query Schools / Colleges

**Endpoint**

POST /query

**Description**  
Accepts a natural language query and returns an AI-generated answer using a Retrieval-Augmented Generation (RAG) pipeline over the school/college dataset.


**Request Body**
```
{
  "query": "Which schools in Kathmandu offer NEB?"
}
```

**Response**
```
{
  "answer": "The following schools in Kathmandu offer NEB: ..."
}
```

### Notes

- The response is generated strictly from the dataset using RAG.
- If relevant information is not found, the system responds with:
`I don't know based on the provided information.`