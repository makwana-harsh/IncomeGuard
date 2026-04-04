from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, TIMESTAMP, Time
from database import Base
from sqlalchemy.sql import func

class WeeklyPolicy(Base):
    __tablename__ = "weekly_policies"

    policy_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    week_start_date = Column(Date)
    week_end_date = Column(Date)
    location = Column(String(100))
    start_time = Column(Time)
    end_time = Column(Time)
    risk_score = Column(Float)
    premium_amount = Column(Float)
    policy_status = Column(String(20))
    created_at = Column(TIMESTAMP, server_default=func.now())