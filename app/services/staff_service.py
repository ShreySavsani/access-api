from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List, Optional
from app.models.staff import Staff
from app.schemas.staff import StaffCreate, StaffUpdate


class StaffService:
    def __init__(self, db: Session):
        self.db = db

    def create_staff(self, staff_data: StaffCreate) -> Staff:
        db_staff = Staff(**staff_data.dict())
        self.db.add(db_staff)
        try:
            self.db.commit()
            self.db.refresh(db_staff)
            return db_staff
        except IntegrityError as e:
            self.db.rollback()
            if "UNIQUE constraint failed: staff.email" in str(e):
                raise ValueError("Email already exists")
            elif "UNIQUE constraint failed: staff.staff_id" in str(e):
                raise ValueError("Staff ID already exists")
            else:
                raise ValueError("Database constraint violation")

    def get_staff(self, staff_id: int) -> Optional[Staff]:
        return self.db.query(Staff).filter(Staff.id == staff_id).first()

    def get_staff_by_staff_id(self, staff_id: str) -> Optional[Staff]:
        return self.db.query(Staff).filter(Staff.staff_id == staff_id).first()

    def get_staff_list(self, skip: int = 0, limit: int = 100) -> List[Staff]:
        return self.db.query(Staff).offset(skip).limit(limit).all()

    def update_staff(self, staff_id: int, staff_data: StaffUpdate) -> Optional[Staff]:
        db_staff = self.get_staff(staff_id)
        if db_staff:
            update_data = staff_data.dict(exclude_unset=True)
            for field, value in update_data.items():
                setattr(db_staff, field, value)
            self.db.commit()
            self.db.refresh(db_staff)
        return db_staff

    def delete_staff(self, staff_id: int) -> bool:
        db_staff = self.get_staff(staff_id)
        if db_staff:
            self.db.delete(db_staff)
            self.db.commit()
            return True
        return False
