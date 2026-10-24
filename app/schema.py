from datetime import date
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class StudentBase(BaseModel):
    student_name: str = Field(min_length=1, max_length=100)
    student_class: str = Field(min_length=1, max_length=50)
    student_section: str = Field(min_length=1, max_length=20)
    student_dob: date

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    student_name: Optional[str] = Field(default=None, min_length=1, max_length=100)
    student_class: Optional[str] = Field(default=None, min_length=1, max_length=50)
    student_section: Optional[str] = Field(default=None, min_length=1, max_length=20)
    student_dob: Optional[date] = None

class StudentResponse(StudentBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
