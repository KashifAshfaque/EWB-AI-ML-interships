# FastAPI — Student Management CRUD API

This is the master-style modular Student Management API directory.

## Run
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python3 -m uvicorn main:app --reload
```

Open http://127.0.0.1:8000/docs.

## Endpoints
- `POST /students/` — create a student
- `GET /students/` — list students
- `GET /students/{student_id}` — retrieve one student
- `PATCH /students/{student_id}` — update student fields
- `DELETE /students/{student_id}` — delete a student

Example request body:
```json
{
  "student_name": "Aarav Sharma",
  "student_class": "B.Tech",
  "student_section": "A",
  "student_dob": "2005-04-15"
}
```

Do not upload `.env`, `.venv`, or `students.db` to GitHub.
