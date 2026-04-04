from pydantic import BaseModel
from datetime import date, time

class ScheduleCreate(BaseModel):
    user_id: int
    date: date
    start_time: time
    end_time: time
    location: str