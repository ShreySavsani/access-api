from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List, Optional
from app.models.patient import Patient
from app.schemas.patient import PatientCreate, PatientUpdate


class PatientService:
    def __init__(self, db: Session):
        self.db = db

    def create_patient(self, patient_data: PatientCreate) -> Patient:
        db_patient = Patient(**patient_data.dict())
        self.db.add(db_patient)
        try:
            self.db.commit()
            self.db.refresh(db_patient)
            return db_patient
        except IntegrityError as e:
            self.db.rollback()
            if "UNIQUE constraint failed: patients.email" in str(e):
                raise ValueError("Email already exists")
            elif "UNIQUE constraint failed: patients.patient_id" in str(e):
                raise ValueError("Patient ID already exists")
            else:
                raise ValueError("Database constraint violation")

    def get_patient(self, patient_id: int) -> Optional[Patient]:
        return self.db.query(Patient).filter(Patient.id == patient_id).first()

    def get_patient_by_patient_id(self, patient_id: str) -> Optional[Patient]:
        return self.db.query(Patient).filter(Patient.patient_id == patient_id).first()

    def get_patients(self, skip: int = 0, limit: int = 100) -> List[Patient]:
        return self.db.query(Patient).offset(skip).limit(limit).all()

    def update_patient(self, patient_id: int, patient_data: PatientUpdate) -> Optional[Patient]:
        db_patient = self.get_patient(patient_id)
        if db_patient:
            update_data = patient_data.dict(exclude_unset=True)
            for field, value in update_data.items():
                setattr(db_patient, field, value)
            self.db.commit()
            self.db.refresh(db_patient)
        return db_patient

    def delete_patient(self, patient_id: int) -> bool:
        db_patient = self.get_patient(patient_id)
        if db_patient:
            self.db.delete(db_patient)
            self.db.commit()
            return True
        return False
