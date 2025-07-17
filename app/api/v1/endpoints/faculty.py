from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db.base import get_db
from app.schemas.faculty import FacultyCreate, FacultyUpdate, FacultyResponse
from app.services.faculty_service import FacultyService

router = APIRouter()


@router.post("/", response_model=FacultyResponse, status_code=status.HTTP_201_CREATED)
def create_faculty(
    faculty: FacultyCreate,
    db: Session = Depends(get_db)
):
    service = FacultyService(db)
    
    # Check if faculty_id already exists
    existing_faculty = service.get_faculty_by_faculty_id(faculty.faculty_id)
    if existing_faculty:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Faculty ID already exists"
        )
    
    return service.create_faculty(faculty)


@router.get("/", response_model=List[FacultyResponse])
def get_faculty_list(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    service = FacultyService(db)
    return service.get_faculty_list(skip=skip, limit=limit)


@router.get("/{faculty_id}", response_model=FacultyResponse)
def get_faculty(
    faculty_id: int,
    db: Session = Depends(get_db)
):
    service = FacultyService(db)
    faculty = service.get_faculty(faculty_id)
    if not faculty:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Faculty not found"
        )
    return faculty


@router.put("/{faculty_id}", response_model=FacultyResponse)
def update_faculty(
    faculty_id: int,
    faculty_update: FacultyUpdate,
    db: Session = Depends(get_db)
):
    service = FacultyService(db)
    faculty = service.update_faculty(faculty_id, faculty_update)
    if not faculty:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Faculty not found"
        )
    return faculty


@router.delete("/{faculty_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_faculty(
    faculty_id: int,
    db: Session = Depends(get_db)
):
    service = FacultyService(db)
    success = service.delete_faculty(faculty_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Faculty not found"
        )