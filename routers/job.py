from fastapi import APIRouter, HTTPException, Depends, status
from schemas.job import JobCreate, JobUpdate, JobResponse
from models.job import Job
from sqlalchemy.orm import Session
from database import get_db


router = APIRouter(prefix="/job", tags=["job"])


def get_job_by_id(job_id: int, db: Session):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job with id {job_id} not found",
        )
    return job


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=JobResponse)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    db_job = Job(**job.model_dump())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[JobResponse])
def get_all_jobs(db: Session = Depends(get_db)):
    return db.query(Job).all()


@router.get("/{job_id}", status_code=status.HTTP_200_OK, response_model=JobResponse)
def get_by_id(job_id: int, db: Session = Depends(get_db)):
    return get_job_by_id(job_id, db)


@router.put("/{job_id}", status_code=status.HTTP_200_OK, response_model=JobResponse)
def update_job(job_id: int, job: JobUpdate, db: Session = Depends(get_db)):
    db_job = get_job_by_id(job_id, db)
    for key, value in job.model_dump(exclude_unset=True).items():
        setattr(db_job, key, value)
    db.commit()
    db.refresh(db_job)
    return db_job


@router.delete("/{job_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_job(job_id: int, db: Session = Depends(get_db)):
    db_job = get_job_by_id(job_id, db)
    db.delete(db_job)
    db.commit()