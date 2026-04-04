from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, TIMESTAMP
from database import Base
from sqlalchemy.sql import func

class Claim(Base):
    __tablename__ = "claims"

    claim_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    policy_id = Column(Integer, ForeignKey("weekly_policies.policy_id"))
    date = Column(Date)
    disruption_type = Column(String(50))
    payout_amount = Column(Float)
    claim_status = Column(String(20))
    created_at = Column(TIMESTAMP, server_default=func.now())