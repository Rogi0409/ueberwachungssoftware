from datetime import datetime
from pydantic import BaseModel, ConfigDict

class CompanyCreate(BaseModel):
    name: str
    legal_form: str | None = None
    registration_country: str
    registration_number: str | None = None

class CompanyRead(BaseModel):
    id: int
    name: str
    legal_form: str | None = None
    registration_country: str
    registration_number: str | None = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
    