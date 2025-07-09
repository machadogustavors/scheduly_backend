from pydantic import BaseModel
from typing import Optional
from datetime import datetime as Datetime

class AppointmentBase(BaseModel):
    datetime: Optional[Datetime] = None
    name: Optional[str] = None
    description: Optional[str] = None