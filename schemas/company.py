from pydantic import BaseModel
from typing import Optional
from .job import JobResponse


class CompanyBase(BaseModel):
    nmae:str
    email:str
    phone:str

class CompanyCreate(CompanyBase):
    pass

class CompanyUpdate(BaseModel):
    name: Optional[str] =None
    email: Optional[str] =None
    phone: Optional[str] =None

class CompanyResponse(CompanyBase):
    id:int
    jobs:list[JobResponse]

class config:
    from_attributes=True