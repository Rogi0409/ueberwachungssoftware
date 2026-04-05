from sqlalchemy.orm import Session

from app.models.company import Company
from app.schemas import CompanyCreate

def create_company(db: Session, company_data: CompanyCreate) -> Company:
    company = Company(
        name=company_data.name,
        legal_form=company_data.legal_form,
        registration_country=company_data.registration_country,
        registration_number=company_data.registration_number
    )
    db.add(company)
    db.commit()
    db.refresh(company)
    return company