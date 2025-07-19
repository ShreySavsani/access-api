from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db.base import get_db
from app.schemas.staff import StaffCreate, StaffUpdate, StaffResponse
from app.services.staff_service import StaffService

router = APIRouter()


@router.post("/", response_model=StaffResponse, status_code=status.HTTP_201_CREATED)
def create_staff(
    staff: StaffCreate,
    db: Session = Depends(get_db)
):
    service = StaffService(db)
    try:
        return service.create_staff(staff)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.get("/", response_model=List[StaffResponse])
def get_staff_list(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    service = StaffService(db)
    return service.get_staff_list(skip=skip, limit=limit)


@router.get("/{staff_id}", response_model=StaffResponse)
def get_staff(
    staff_id: int,
    db: Session = Depends(get_db)
):
    service = StaffService(db)
    staff = service.get_staff(staff_id)
    if not staff:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Staff not found",
        )
    return staff


@router.put("/{staff_id}", response_model=StaffResponse)
def update_staff(
    staff_id: int,
    staff_update: StaffUpdate,
    db: Session = Depends(get_db)
):
    service = StaffService(db)
    staff = service.update_staff(staff_id, staff_update)
    if not staff:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Staff not found",
        )
    return staff


@router.delete("/{staff_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_staff(
    staff_id: int,
    db: Session = Depends(get_db)
):
    service = StaffService(db)
    success = service.delete_staff(staff_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Staff not found",
        )
