from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.model import Student
from app.schema import StudentCreate, StudentResponse

router = APIRouter()

@router.post("/", response_model=StudentResponse, status_code=201)
def create_student(student_data: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(**student_data.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
