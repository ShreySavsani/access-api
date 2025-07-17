# Access API

A comprehensive FastAPI application for managing access control across different user domains including Students, Faculty, and IT Staff. Built with modern Python web technologies and following industry-standard project structure.

## 🚀 Features

- **Multi-domain CRUD operations** for Students, Faculty, and IT Staff
- **RESTful API endpoints** with proper HTTP status codes
- **Automatic API documentation** with Swagger UI and ReDoc
- **Data validation** using Pydantic schemas
- **SQLite database** with SQLAlchemy ORM
- **Modular architecture** with clear separation of concerns
- **Error handling** with proper exception management
- **CORS support** for frontend integration

## 📋 API Endpoints

### Students (`/api/v1/students/`)
- `POST /` - Create a new student
- `GET /` - List all students (with pagination)
- `GET /{id}` - Get specific student by ID
- `PUT /{id}` - Update student information
- `DELETE /{id}` - Delete a student

### Faculty (`/api/v1/faculty/`)
- `POST /` - Create a new faculty member
- `GET /` - List all faculty (with pagination)
- `GET /{id}` - Get specific faculty by ID
- `PUT /{id}` - Update faculty information
- `DELETE /{id}` - Delete a faculty member

### IT Staff (`/api/v1/it-staff/`)
- `POST /` - Create a new IT staff member
- `GET /` - List all IT staff (with pagination)
- `GET /{id}` - Get specific IT staff by ID
- `PUT /{id}` - Update IT staff information
- `DELETE /{id}` - Delete an IT staff member

## 🏗️ Project Structure

```
access-api/
├── app/                           # Main application package
│   ├── api/                       # API routes
│   │   └── v1/                    # API version 1
│   │       ├── endpoints/         # Individual endpoint modules
│   │       │   ├── students.py    # Student endpoints
│   │       │   ├── faculty.py     # Faculty endpoints
│   │       │   └── it_staff.py    # IT staff endpoints
│   │       └── __init__.py        # API router setup
│   ├── core/                      # Core functionality
│   │   └── config.py              # Application configuration
│   ├── db/                        # Database configuration
│   │   └── base.py                # Database connection and session
│   ├── models/                    # SQLAlchemy database models
│   │   ├── student.py             # Student model
│   │   ├── faculty.py             # Faculty model
│   │   └── it_staff.py            # IT staff model
│   ├── schemas/                   # Pydantic request/response schemas
│   │   ├── student.py             # Student schemas
│   │   ├── faculty.py             # Faculty schemas
│   │   └── it_staff.py            # IT staff schemas
│   ├── services/                  # Business logic layer
│   │   ├── student_service.py     # Student business logic
│   │   ├── faculty_service.py     # Faculty business logic
│   │   └── it_staff_service.py    # IT staff business logic
│   ├── utils/                     # Utility functions
│   └── main.py                    # FastAPI application entry point
├── tests/                         # Test suite
│   ├── unit/                      # Unit tests
│   └── integration/               # Integration tests
├── docs/                          # Documentation
├── scripts/                       # Utility scripts
├── venv/                          # Virtual environment
├── access_api.db                  # SQLite database file
├── requirements.txt               # Python dependencies
├── .env                          # Environment variables
├── .gitignore                    # Git ignore rules
├── run.py                        # Application runner
├── start.bat                     # Windows startup script
├── view_db.py                    # Database viewer utility
└── README.md                     # This file
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone/Download the Project
```bash
# Navigate to your desired directory
cd /path/to/your/projects

# If using Git
git clone <repository-url>
cd access-api

# Or download and extract the ZIP file
```

### Step 2: Set Up Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment (Optional)
Edit the `.env` file to customize settings:
```env
APP_NAME=Access API
DEBUG=True
HOST=0.0.0.0
PORT=8000
DATABASE_URL=sqlite:///./access_api.db
SECRET_KEY=your-secret-key-here
```

### Step 5: Run the Application

#### Option A: Using the startup script (Windows)
```bash
# Double-click start.bat or run:
start.bat
```

#### Option B: Manual startup
```bash
# Activate virtual environment first
venv\Scripts\activate

# Start the server
python run.py

# Or using uvicorn directly
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 🌐 Accessing the Application

Once running, access:
- **API Documentation (Swagger)**: http://localhost:8000/docs
- **Alternative Documentation (ReDoc)**: http://localhost:8000/redoc
- **API Base URL**: http://localhost:8000/api/v1/
- **Health Check**: http://localhost:8000/health
- **Root Endpoint**: http://localhost:8000/

## 📝 Usage Examples

### Creating a Student
```bash
curl -X POST "http://localhost:8000/api/v1/students/" \
     -H "Content-Type: application/json" \
     -d '{
       "student_id": "STU001",
       "first_name": "John",
       "last_name": "Doe",
       "email": "john.doe@university.edu",
       "phone": "555-0123",
       "major": "Computer Science",
       "year": 2,
       "gpa": "3.8",
       "is_active": true
     }'
```

### Getting All Students
```bash
curl -X GET "http://localhost:8000/api/v1/students/"
```

### Updating a Student
```bash
curl -X PUT "http://localhost:8000/api/v1/students/1" \
     -H "Content-Type: application/json" \
     -d '{
       "major": "Software Engineering",
       "year": 3,
       "gpa": "3.9"
     }'
```

## 🗄️ Database

### Viewing Database Contents

#### Option 1: Using the Python viewer script
```bash
python view_db.py
```

#### Option 2: Using DB Browser for SQLite
1. Download [DB Browser for SQLite](https://sqlitebrowser.org/)
2. Open the `access_api.db` file

#### Option 3: Using API endpoints
- GET `/api/v1/students/` - View all students
- GET `/api/v1/faculty/` - View all faculty
- GET `/api/v1/it-staff/` - View all IT staff

### Database Schema

#### Students Table
- `id` - Primary key (auto-increment)
- `student_id` - Unique student identifier
- `first_name` - Student's first name
- `last_name` - Student's last name
- `email` - Unique email address
- `phone` - Phone number (optional)
- `major` - Academic major (optional)
- `year` - Academic year (1-4)
- `gpa` - Grade point average
- `is_active` - Account status
- `created_at` - Record creation timestamp
- `updated_at` - Last update timestamp

#### Faculty Table
- `id` - Primary key (auto-increment)
- `faculty_id` - Unique faculty identifier
- `first_name` - Faculty's first name
- `last_name` - Faculty's last name
- `email` - Unique email address
- `phone` - Phone number (optional)
- `department` - Department name
- `position` - Academic position (optional)
- `office_location` - Office location (optional)
- `specialization` - Area of expertise (optional)
- `is_active` - Account status
- `created_at` - Record creation timestamp
- `updated_at` - Last update timestamp

#### IT Staff Table
- `id` - Primary key (auto-increment)
- `staff_id` - Unique staff identifier
- `first_name` - Staff's first name
- `last_name` - Staff's last name
- `email` - Unique email address
- `phone` - Phone number (optional)
- `department` - Department (default: "Information Technology")
- `role` - Job role/title
- `access_level` - System access level (admin/standard/limited)
- `office_location` - Office location (optional)
- `is_active` - Account status
- `created_at` - Record creation timestamp
- `updated_at` - Last update timestamp

## 🔧 Adding New Domains

To add a new domain (e.g., "Vendors"), follow these steps:

### Step 1: Create Database Model
Create `app/models/vendor.py`:
```python
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from app.db.base import Base

class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True, index=True)
    vendor_id = Column(String, unique=True, index=True, nullable=False)
    company_name = Column(String, nullable=False)
    contact_person = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=True)
    service_type = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
```

### Step 2: Create Pydantic Schemas
Create `app/schemas/vendor.py`:
```python
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class VendorBase(BaseModel):
    vendor_id: str
    company_name: str
    contact_person: str
    email: EmailStr
    phone: Optional[str] = None
    service_type: str
    is_active: bool = True

class VendorCreate(VendorBase):
    pass

class VendorUpdate(BaseModel):
    company_name: Optional[str] = None
    contact_person: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    service_type: Optional[str] = None
    is_active: Optional[bool] = None

class VendorResponse(VendorBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
```

### Step 3: Create Service Layer
Create `app/services/vendor_service.py`:
```python
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List, Optional
from app.models.vendor import Vendor
from app.schemas.vendor import VendorCreate, VendorUpdate

class VendorService:
    def __init__(self, db: Session):
        self.db = db

    def create_vendor(self, vendor_data: VendorCreate) -> Vendor:
        db_vendor = Vendor(**vendor_data.dict())
        self.db.add(db_vendor)
        try:
            self.db.commit()
            self.db.refresh(db_vendor)
            return db_vendor
        except IntegrityError as e:
            self.db.rollback()
            if "UNIQUE constraint failed: vendors.email" in str(e):
                raise ValueError("Email already exists")
            elif "UNIQUE constraint failed: vendors.vendor_id" in str(e):
                raise ValueError("Vendor ID already exists")
            else:
                raise ValueError("Database constraint violation")

    def get_vendor(self, vendor_id: int) -> Optional[Vendor]:
        return self.db.query(Vendor).filter(Vendor.id == vendor_id).first()

    def get_vendors(self, skip: int = 0, limit: int = 100) -> List[Vendor]:
        return self.db.query(Vendor).offset(skip).limit(limit).all()

    def update_vendor(self, vendor_id: int, vendor_data: VendorUpdate) -> Optional[Vendor]:
        db_vendor = self.get_vendor(vendor_id)
        if db_vendor:
            update_data = vendor_data.dict(exclude_unset=True)
            for field, value in update_data.items():
                setattr(db_vendor, field, value)
            self.db.commit()
            self.db.refresh(db_vendor)
        return db_vendor

    def delete_vendor(self, vendor_id: int) -> bool:
        db_vendor = self.get_vendor(vendor_id)
        if db_vendor:
            self.db.delete(db_vendor)
            self.db.commit()
            return True
        return False
```

### Step 4: Create API Endpoints
Create `app/api/v1/endpoints/vendors.py`:
```python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db.base import get_db
from app.schemas.vendor import VendorCreate, VendorUpdate, VendorResponse
from app.services.vendor_service import VendorService

router = APIRouter()

@router.post("/", response_model=VendorResponse, status_code=status.HTTP_201_CREATED)
def create_vendor(
    vendor: VendorCreate,
    db: Session = Depends(get_db)
):
    service = VendorService(db)
    try:
        return service.create_vendor(vendor)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.get("/", response_model=List[VendorResponse])
def get_vendors(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    service = VendorService(db)
    return service.get_vendors(skip=skip, limit=limit)

@router.get("/{vendor_id}", response_model=VendorResponse)
def get_vendor(
    vendor_id: int,
    db: Session = Depends(get_db)
):
    service = VendorService(db)
    vendor = service.get_vendor(vendor_id)
    if not vendor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vendor not found"
        )
    return vendor

@router.put("/{vendor_id}", response_model=VendorResponse)
def update_vendor(
    vendor_id: int,
    vendor_update: VendorUpdate,
    db: Session = Depends(get_db)
):
    service = VendorService(db)
    vendor = service.update_vendor(vendor_id, vendor_update)
    if not vendor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vendor not found"
        )
    return vendor

@router.delete("/{vendor_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vendor(
    vendor_id: int,
    db: Session = Depends(get_db)
):
    service = VendorService(db)
    success = service.delete_vendor(vendor_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vendor not found"
        )
```

### Step 5: Register the Router
Update `app/api/v1/__init__.py`:
```python
from fastapi import APIRouter
from app.api.v1.endpoints import students, faculty, it_staff, vendors

api_router = APIRouter()

api_router.include_router(students.router, prefix="/students", tags=["students"])
api_router.include_router(faculty.router, prefix="/faculty", tags=["faculty"])
api_router.include_router(it_staff.router, prefix="/it-staff", tags=["it-staff"])
api_router.include_router(vendors.router, prefix="/vendors", tags=["vendors"])
```

### Step 6: Update Model Imports
Update `app/models/__init__.py`:
```python
from .student import Student
from .faculty import Faculty
from .it_staff import ITStaff
from .vendor import Vendor

__all__ = ["Student", "Faculty", "ITStaff", "Vendor"]
```

### Step 7: Update Schema Imports
Update `app/schemas/__init__.py`:
```python
from .student import StudentCreate, StudentUpdate, StudentResponse
from .faculty import FacultyCreate, FacultyUpdate, FacultyResponse
from .it_staff import ITStaffCreate, ITStaffUpdate, ITStaffResponse
from .vendor import VendorCreate, VendorUpdate, VendorResponse

__all__ = [
    "StudentCreate", "StudentUpdate", "StudentResponse",
    "FacultyCreate", "FacultyUpdate", "FacultyResponse", 
    "ITStaffCreate", "ITStaffUpdate", "ITStaffResponse",
    "VendorCreate", "VendorUpdate", "VendorResponse"
]
```

### Step 8: Restart the Application
The new tables will be created automatically when you restart the server:
```bash
python run.py
```

The new vendor endpoints will be available at `/api/v1/vendors/` and documented at http://localhost:8000/docs

## 🧪 Testing

### Manual Testing
Use the Swagger UI at http://localhost:8000/docs for interactive testing.

### Automated Testing
```bash
# Run tests (when implemented)
pytest

# Run with coverage
pytest --cov=app
```

## 🚀 Deployment

### Development
The application is pre-configured for development with SQLite and debug mode enabled.

### Production Considerations
1. **Database**: Switch to PostgreSQL or MySQL
2. **Environment Variables**: Use production values in `.env`
3. **Security**: Update SECRET_KEY and disable debug mode
4. **CORS**: Configure allowed origins appropriately
5. **Server**: Use a production ASGI server like Gunicorn

## 📚 Technologies Used

- **FastAPI** - Modern, fast web framework for building APIs
- **SQLAlchemy** - SQL toolkit and Object-Relational Mapping (ORM)
- **Pydantic** - Data validation using Python type annotations
- **SQLite** - Lightweight, serverless database
- **Uvicorn** - ASGI server for running the application
- **Python 3.8+** - Programming language

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-domain`)
3. Commit your changes (`git commit -am 'Add new domain'`)
4. Push to the branch (`git push origin feature/new-domain`)
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Change port in .env file or run with different port
   uvicorn app.main:app --port 8001
   ```

2. **Module not found errors**
   ```bash
   # Ensure virtual environment is activated
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # macOS/Linux
   ```

3. **Database locked errors**
   ```bash
   # Stop the server and restart
   # Delete access_api.db if necessary (will recreate tables)
   ```

4. **Email/ID already exists errors**
   - Use unique email addresses and IDs
   - Check existing data with `python view_db.py`

### Getting Help

- Check the [FastAPI documentation](https://fastapi.tiangolo.com/)
- Review the API documentation at http://localhost:8000/docs
- Check the server logs in the terminal for error details

## 📞 Support

For questions or issues, please:
1. Check the troubleshooting section above
2. Review the API documentation
3. Check server logs for error details
4. Create an issue in the repository (if applicable)