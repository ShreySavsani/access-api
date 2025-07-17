from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class FacultyBase(BaseModel):
    faculty_id: str
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    department: str
    position: Optional[str] = None
    office_location: Optional[str] = None
    specialization: Optional[str] = None
    is_active: bool = True


class FacultyCreate(FacultyBase):
    pass


class FacultyUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    department: Optional[str] = None
    position: Optional[str] = None
    office_location: Optional[str] = None
    specialization: Optional[str] = None
    is_active: Optional[bool] = None


class FacultyResponse(FacultyBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True