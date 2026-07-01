from fastapi import APIRouter, HTTPException, Depends, status
from schemas.company import CompanyCreate, CompanyUpdate, CompanyResponse
from models.company import Company
from sqlalchemy.orm import Session
from database import get_db


router = APIRouter(prefix="/company", tags=["company"])


def get_company_by_id(company_id: int, db: Session):
    company = db.query(Company).filter(Company.id == company_id).first()
    if not company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Company with id {company_id} not found",
        )
    return company


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CompanyResponse)
def create_company(company: CompanyCreate, db: Session = Depends(get_db)):
    db_company = Company(**company.model_dump())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[CompanyResponse])
def get_all_company(db: Session = Depends(get_db)):
    return db.query(Company).all()


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=CompanyResponse)
def get_by_id(id: int, db: Session = Depends(get_db)):
    return get_company_by_id(id, db)


@router.put("/{company_id}", status_code=status.HTTP_200_OK, response_model=CompanyResponse)
def update_company(company_id: int, company: CompanyUpdate, db: Session = Depends(get_db)):
    db_company = get_company_by_id(company_id, db)
    for key, value in company.model_dump(exclude_unset=True).items():
        setattr(db_company, key, value)
    db.commit()
    db.refresh(db_company)
    return db_company


@router.delete("/{company_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_company(company_id: int, db: Session = Depends(get_db)):
    db_company = get_company_by_id(company_id, db)
    db.delete(db_company)
    db.commit()
    return {"message": f"Company with id {company_id} deleted"}