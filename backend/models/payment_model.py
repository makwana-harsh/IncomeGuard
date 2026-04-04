from sqlalchemy import Column, Integer, String, Float, ForeignKey, TIMESTAMP
from database import Base
from sqlalchemy.sql import func

class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, index=True)
    claim_id = Column(Integer, ForeignKey("claims.claim_id"))
    user_id = Column(Integer, ForeignKey("users.user_id"))
    amount = Column(Float)
    payment_status = Column(String(20))
    payment_method = Column(String(50))
    transaction_id = Column(String(100))
    created_at = Column(TIMESTAMP, server_default=func.now())