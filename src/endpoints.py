from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import SessionLocal
from src.schemas import UserCreate, UserResponse, CompanyCreate, CompanyResponse
from src.crud import create_user, get_users, create_company, get_companies

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/companies", response_model=CompanyResponse)
def add_company(company: CompanyCreate, db: Session = Depends(get_db)):
    return create_company(db, company)

@router.get("/companies", response_model=list[CompanyResponse])
def list_companies(db: Session = Depends(get_db)):
    return get_companies(db)

@router.post("/users", response_model=UserResponse)
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/users", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return get_users(db)
