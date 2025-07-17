from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from app.db.base import Base


class ITStaff(Base):
    __tablename__ = "it_staff"

    id = Column(Integer, primary_key=True, index=True)
    staff_id = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=True)
    department = Column(String, default="Information Technology")
    role = Column(String, nullable=False)  # System Admin, Network Admin, Developer, etc.
    access_level = Column(String, default="standard")  # admin, standard, limited
    office_location = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())