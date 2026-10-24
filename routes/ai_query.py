
import sqlite3

from fastapi import APIRouter, HTTPException
from langchain_ollama import ChatOllama
from pydantic import BaseModel

router = APIRouter(prefix="/ai", tags=["AI Query"])

llm = ChatOllama(model="llama3.2:1b", temperature=0)


class QueryRequest(BaseModel):
    question: str


@router.post("/query-students")
def ask_student_database(payload: QueryRequest):
    try:
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in cursor.fetchall()]

        if "students" not in tables:
            conn.close()
            raise HTTPException(
                status_code=500,
                detail="Students table not found in students.db"
            )

        cursor.execute("PRAGMA table_info(students)")
        columns = [row[1] for row in cursor.fetchall()]

        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        conn.close()

        context_data = (
            f"Columns: {columns}\n"
            f"Student records:\n" +
            "\n".join(str(row) for row in rows)
        )

        prompt = f"""You are a helpful assistant.
Answer the user's question using only the student database records below.
If the answer is not present, say that the information is not available.

Database Context:
{context_data}

User Question: {payload.question}

Answer:"""

        response = llm.invoke(prompt)
        answer_text = (
            response.content
            if hasattr(response, "content")
            else str(response)
        )

        return {
            "question": payload.question,
            "answer": answer_text
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
