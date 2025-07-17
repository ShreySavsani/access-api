from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.faculty import Faculty
from app.schemas.faculty import FacultyCreate, FacultyUpdate


class FacultyService:
    def __init__(self, db: Session):
        self.db = db

    def create_faculty(self, faculty_data: FacultyCreate) -> Faculty:
        db_faculty = Faculty(**faculty_data.dict())
        self.db.add(db_faculty)
        self.db.commit()
        self.db.refresh(db_faculty)
        return db_faculty

    def get_faculty(self, faculty_id: int) -> Optional[Faculty]:
        return self.db.query(Faculty).filter(Faculty.id == faculty_id).first()

    def get_faculty_by_faculty_id(self, faculty_id: str) -> Optional[Faculty]:
        return self.db.query(Faculty).filter(Faculty.faculty_id == faculty_id).first()

    def get_faculty_list(self, skip: int = 0, limit: int = 100) -> List[Faculty]:
        return self.db.query(Faculty).offset(skip).limit(limit).all()

    def update_faculty(self, faculty_id: int, faculty_data: FacultyUpdate) -> Optional[Faculty]:
        db_faculty = self.get_faculty(faculty_id)
        if db_faculty:
            update_data = faculty_data.dict(exclude_unset=True)
            for field, value in update_data.items():
                setattr(db_faculty, field, value)
            self.db.commit()
            self.db.refresh(db_faculty)
        return db_faculty

    def delete_faculty(self, faculty_id: int) -> bool:
        db_faculty = self.get_faculty(faculty_id)
        if db_faculty:
            self.db.delete(db_faculty)
            self.db.commit()
            return True
        return False