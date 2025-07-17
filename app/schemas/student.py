from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class StudentBase(BaseModel):
    student_id: str
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    major: Optional[str] = None
    year: Optional[int] = None
    gpa: Optional[str] = None
    is_active: bool = True


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    major: Optional[str] = None
    year: Optional[int] = None
    gpa: Optional[str] = None
    is_active: Optional[bool] = None


class StudentResponse(StudentBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True