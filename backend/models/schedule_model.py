from sqlalchemy import Column, Integer, String, Date, ForeignKey, Time
from database import Base

class DailySchedule(Base):
    __tablename__ = "daily_schedule"

    schedule_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    date = Column(Date)
    start_time = Column(Time)
    end_time = Column(Time)  
    location = Column(String(100))