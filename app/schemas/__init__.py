from .student import StudentCreate, StudentUpdate, StudentResponse
from .faculty import FacultyCreate, FacultyUpdate, FacultyResponse
from .it_staff import ITStaffCreate, ITStaffUpdate, ITStaffResponse
from .staff import StaffCreate, StaffUpdate, StaffResponse
from .patient import PatientCreate, PatientUpdate, PatientResponse

__all__ = [
    "StudentCreate", "StudentUpdate", "StudentResponse",
    "FacultyCreate", "FacultyUpdate", "FacultyResponse",
    "ITStaffCreate", "ITStaffUpdate", "ITStaffResponse",
    "StaffCreate", "StaffUpdate", "StaffResponse",
    "PatientCreate", "PatientUpdate", "PatientResponse",
]