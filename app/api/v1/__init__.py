from fastapi import APIRouter
from app.api.v1.endpoints import students, faculty, it_staff

api_router = APIRouter()

api_router.include_router(students.router, prefix="/students", tags=["students"])
api_router.include_router(faculty.router, prefix="/faculty", tags=["faculty"])
api_router.include_router(it_staff.router, prefix="/it-staff", tags=["it-staff"])