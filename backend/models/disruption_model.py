from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP
from database import Base
from sqlalchemy.sql import func

class Disruption(Base):
    __tablename__ = "disruptions"

    disruption_id = Column(Integer, primary_key=True, index=True)
    datetime = Column(DateTime)
    location = Column(String(100))
    created_at = Column(TIMESTAMP, server_default=func.now())