# FastAPI Student Management API with Ollama

A modular Student Management API built using FastAPI, SQLAlchemy, SQLite, and Ollama. The project provides CRUD operations for managing students and an AI-powered endpoint to ask questions about the student database using a locally running LLM.

## Features

- Create new student records
- Retrieve all students
- Retrieve a student by ID
- Update student information
- Delete student records
- Ask questions about the student database using Ollama
- Interactive API documentation with Swagger UI
- SQLite database integration
- Modular project structure using FastAPI routers

## Tech Stack

- **Language:** Python
- **Backend:** FastAPI
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **AI/LLM:** Ollama
- **LLM Model:** `llama3.2:1b`
- **AI Integration:** LangChain Ollama
- **API Documentation:** Swagger UI

## Project Structure

```text
FastAPI/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── model.py
│   └── schema.py
├── routes/
│   ├── __init__.py
│   ├── ai_query.py
│   ├── base.py
│   ├── create_students.py
│   ├── get_students.py
│   ├── update_students.py
│   └── delete_students.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/KashifAshfaque/EWB-AI-ML-interships.git
cd EWB-AI-ML-interships
```

### 2. Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 4. Install and Run Ollama

Download Ollama from:

https://ollama.com/download

Pull the Llama 3.2 1B model:

```bash
ollama pull llama3.2:1b
```

Verify the installed model:

```bash
ollama list
```

Make sure the Ollama service is running before using the AI query endpoint.

### 5. Run the FastAPI Application

```bash
python3 -m uvicorn main:app --reload
```

## API Documentation

Once the application is running, open:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **API Root:** http://127.0.0.1:8000

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/students/` | Create a student |
| GET | `/students/` | Retrieve all students |
| GET | `/students/{student_id}` | Retrieve a student by ID |
| PUT | `/students/{student_id}` | Update a student |
| DELETE | `/students/{student_id}` | Delete a student |
| POST | `/ai/query-students` | Ask questions about the student database using Ollama |

## Example AI Query

**Endpoint:** `POST /ai/query-students`

Request body:

```json
{
  "question": "How many students are in the database?"
}
```

The endpoint sends the question to the locally running Ollama model and returns an answer based on the application's AI query implementation.

## Learning Outcomes

- Building REST APIs with FastAPI
- Implementing CRUD operations
- Working with SQLite and SQLAlchemy
- Organizing a backend application using routers
- Integrating a locally running LLM with LangChain and Ollama
- Testing API endpoints using Swagger UI

## Author

**Kashif Ashfaque**

GitHub: https://github.com/KashifAshfaque

---

This project was developed as part of the EWB Tech Academy AI/ML learning journey.
