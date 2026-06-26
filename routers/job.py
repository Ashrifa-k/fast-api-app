from fastapi import APIRouter

router=APIRouter(prefix="/job",tags=["job"])

@router.get("/")
def read_job():
    return {"job_id":job_id}