from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db.base import get_db
from app.schemas.it_staff import ITStaffCreate, ITStaffUpdate, ITStaffResponse
from app.services.it_staff_service import ITStaffService

router = APIRouter()


@router.post("/", response_model=ITStaffResponse, status_code=status.HTTP_201_CREATED)
def create_it_staff(
    it_staff: ITStaffCreate,
    db: Session = Depends(get_db)
):
    service = ITStaffService(db)
    
    # Check if staff_id already exists
    existing_staff = service.get_it_staff_by_staff_id(it_staff.staff_id)
    if existing_staff:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="IT Staff ID already exists"
        )
    
    return service.create_it_staff(it_staff)


@router.get("/", response_model=List[ITStaffResponse])
def get_it_staff_list(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    service = ITStaffService(db)
    return service.get_it_staff_list(skip=skip, limit=limit)


@router.get("/{staff_id}", response_model=ITStaffResponse)
def get_it_staff(
    staff_id: int,
    db: Session = Depends(get_db)
):
    service = ITStaffService(db)
    it_staff = service.get_it_staff(staff_id)
    if not it_staff:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="IT Staff not found"
        )
    return it_staff


@router.put("/{staff_id}", response_model=ITStaffResponse)
def update_it_staff(
    staff_id: int,
    staff_update: ITStaffUpdate,
    db: Session = Depends(get_db)
):
    service = ITStaffService(db)
    it_staff = service.update_it_staff(staff_id, staff_update)
    if not it_staff:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="IT Staff not found"
        )
    return it_staff


@router.delete("/{staff_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_it_staff(
    staff_id: int,
    db: Session = Depends(get_db)
):
    service = ITStaffService(db)
    success = service.delete_it_staff(staff_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="IT Staff not found"
        )