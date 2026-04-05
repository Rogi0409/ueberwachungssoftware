from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
class Company(Base):
    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(primary_key= True, unique=True, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    legal_form: Mapped[str|None] = mapped_column(String(100), nullable = True)
    registration_country: Mapped[str] = mapped_column(String(2), nullable = False)
    registration_number: Mapped[str] = mapped_column(String(100), nullable = True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, 
        default=datetime.utcnow, 
        nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, 
        default=datetime.utcnow, 
        onupdate=datetime.utcnow, 
        nullable=False)

