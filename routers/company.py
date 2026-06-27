from fastapi import APIRouter,HTTPException,Depends,status
from schemas.company import CompanyCreate,CompanyUpdate,CompanyResponse
from models.company import Company
from sqlalchemy.orm import Session
from database import get_db,SessionLocal


router=APIRouter(prefix="/company",tags=["company"])
companies=[]

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=CompanyResponse)
def create_company(company:CompanyCreate,db:Session=Depends(get_db)):
    db_company=company(**company.dict())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

@router.get("/",status_code=status.HTTP_200_OK,response_model=list[CompanyResponse])
def get_all_company(db:Session=Depends(get_db)):
    pass

@router.get("/{id}",status_code=status.HTTP_200_OK)
def get_by_id(id):
    return companies['id']

@router.put("/{company_id}",status_code=status.HTTP_201_CREATED)
def update_company(company_id:int,company:CompanyUpdate,db:Session=Depends(get_db)):
    companies[company_id]=company
    return companies

@router.delete("/{company_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_company(company_id:int,db:Session=Depends(get_db)):
    companies.pop(company_id)
    return companies

#@router.get("/")
#def read_company():
    #return {"company": "Company root"}

#@router.get("/{company_id}")
#def read_company(company_id: int):
    #return {"company_id": company_id}