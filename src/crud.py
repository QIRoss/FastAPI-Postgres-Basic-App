from sqlalchemy.orm import Session
from src.models import User, Company
from src.schemas import UserCreate, CompanyCreate

def create_company(db: Session, company: CompanyCreate):
    db_company = Company(name=company.name)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

def get_companies(db: Session):
    return db.query(Company).all()

def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, company_id=user.company_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(User).all()
