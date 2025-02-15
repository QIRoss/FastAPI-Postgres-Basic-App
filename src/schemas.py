from pydantic import BaseModel, ConfigDict
from typing import Optional

class CompanyBase(BaseModel):
    name: str

class CompanyCreate(CompanyBase):
    pass

class CompanyResponse(CompanyBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class UserCreate(BaseModel):
    name: str
    company_id: int  # Agora sempre obrigatório

class UserResponse(BaseModel):
    id: int
    name: str
    company_id: int

    model_config = ConfigDict(from_attributes=True)
