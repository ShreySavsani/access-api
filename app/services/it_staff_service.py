from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.it_staff import ITStaff
from app.schemas.it_staff import ITStaffCreate, ITStaffUpdate


class ITStaffService:
    def __init__(self, db: Session):
        self.db = db

    def create_it_staff(self, staff_data: ITStaffCreate) -> ITStaff:
        db_staff = ITStaff(**staff_data.dict())
        self.db.add(db_staff)
        self.db.commit()
        self.db.refresh(db_staff)
        return db_staff

    def get_it_staff(self, staff_id: int) -> Optional[ITStaff]:
        return self.db.query(ITStaff).filter(ITStaff.id == staff_id).first()

    def get_it_staff_by_staff_id(self, staff_id: str) -> Optional[ITStaff]:
        return self.db.query(ITStaff).filter(ITStaff.staff_id == staff_id).first()

    def get_it_staff_list(self, skip: int = 0, limit: int = 100) -> List[ITStaff]:
        return self.db.query(ITStaff).offset(skip).limit(limit).all()

    def update_it_staff(self, staff_id: int, staff_data: ITStaffUpdate) -> Optional[ITStaff]:
        db_staff = self.get_it_staff(staff_id)
        if db_staff:
            update_data = staff_data.dict(exclude_unset=True)
            for field, value in update_data.items():
                setattr(db_staff, field, value)
            self.db.commit()
            self.db.refresh(db_staff)
        return db_staff

    def delete_it_staff(self, staff_id: int) -> bool:
        db_staff = self.get_it_staff(staff_id)
        if db_staff:
            self.db.delete(db_staff)
            self.db.commit()
            return True
        return False