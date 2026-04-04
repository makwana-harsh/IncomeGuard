from sqlalchemy import Column, Integer, String, TIMESTAMP
from database import Base
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    phone = Column(String(15), unique=True)
    email = Column(String(100), unique=True)
    password_hash = Column(String(255))
    vehicle_type = Column(String(50))
    platform = Column(String(50))
    created_at = Column(TIMESTAMP, server_default=func.now())