from pydantic import BaseModel
from datetime import date

class PolicyCreate(BaseModel):
    user_id: int
    week_start_date: date
    week_end_date: date
    location: str
    planned_work_hours: int

class PremiumResponse(BaseModel):
    risk_score: float
    premium_amount: float