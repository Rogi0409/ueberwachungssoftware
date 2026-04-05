from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.company import CompanyCreate, CompanyRead
from app.services.company_service import create_company


app = FastAPI(title="Überwachungssoftware_API")

@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/companies/", response_model=CompanyRead, status_code=201)
def create_company_endpoint(
    company_data: CompanyCreate,
    db: Session = Depends(get_db),
):
    return create_company(db=db, company_data=company_data)           