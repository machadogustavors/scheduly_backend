from datetime import datetime

from src.lib.models import AppointmentBase

class Appointment(AppointmentBase):
    id: str
    created_at: datetime