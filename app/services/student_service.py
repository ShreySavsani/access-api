from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List, Optional
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentUpdate


class StudentService:
    def __init__(self, db: Session):
        self.db = db

    def create_student(self, student_data: StudentCreate) -> Student:
        db_student = Student(**student_data.dict())
        self.db.add(db_student)
        try:
            self.db.commit()
            self.db.refresh(db_student)
            return db_student
        except IntegrityError as e:
            self.db.rollback()
            if "UNIQUE constraint failed: students.email" in str(e):
                raise ValueError("Email already exists")
            elif "UNIQUE constraint failed: students.student_id" in str(e):
                raise ValueError("Student ID already exists")
            else:
                raise ValueError("Database constraint violation")

    def get_student(self, student_id: int) -> Optional[Student]:
        return self.db.query(Student).filter(Student.id == student_id).first()

    def get_student_by_student_id(self, student_id: str) -> Optional[Student]:
        return self.db.query(Student).filter(Student.student_id == student_id).first()

    def get_students(self, skip: int = 0, limit: int = 100) -> List[Student]:
        return self.db.query(Student).offset(skip).limit(limit).all()

    def update_student(self, student_id: int, student_data: StudentUpdate) -> Optional[Student]:
        db_student = self.get_student(student_id)
        if db_student:
            update_data = student_data.dict(exclude_unset=True)
            for field, value in update_data.items():
                setattr(db_student, field, value)
            self.db.commit()
            self.db.refresh(db_student)
        return db_student

    def delete_student(self, student_id: int) -> bool:
        db_student = self.get_student(student_id)
        if db_student:
            self.db.delete(db_student)
            self.db.commit()
            return True
        return False