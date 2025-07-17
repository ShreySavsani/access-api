from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class ITStaffBase(BaseModel):
    staff_id: str
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    department: str = "Information Technology"
    role: str
    access_level: str = "standard"
    office_location: Optional[str] = None
    is_active: bool = True


class ITStaffCreate(ITStaffBase):
    pass


class ITStaffUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    department: Optional[str] = None
    role: Optional[str] = None
    access_level: Optional[str] = None
    office_location: Optional[str] = None
    is_active: Optional[bool] = None


class ITStaffResponse(ITStaffBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True