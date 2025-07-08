from pydantic import BaseModel
from typing import Optional
from datetime import date as Date

class AppointmentBase(BaseModel):
    datetime: Optional[Date] = None
    name: Optional[str] = None
    description: Optional[str] = None