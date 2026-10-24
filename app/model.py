from sqlalchemy import Date, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    student_name: Mapped[str] = mapped_column(String(100), nullable=False)
    student_class: Mapped[str] = mapped_column(String(50), nullable=False)
    student_section: Mapped[str] = mapped_column(String(20), nullable=False)
    student_dob: Mapped[Date] = mapped_column(Date, nullable=False)
