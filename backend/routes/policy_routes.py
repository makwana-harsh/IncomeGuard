from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.policy_model import WeeklyPolicy
from schemas.policy_schema import PolicyCreate
from services.premium_calculator import calculate_risk_and_premium

router = APIRouter()

@router.post("/create-policy")
def create_policy(policy: PolicyCreate, db: Session = Depends(get_db)):
    
    risk_score, premium = calculate_risk_and_premium(
        policy.location,
        policy.planned_work_hours
    )

    new_policy = WeeklyPolicy(
        user_id=policy.user_id,
        week_start_date=policy.week_start_date,
        week_end_date=policy.week_end_date,
        location=policy.location,
        start_time=policy.start_time,
        end_time=policy.end_time,
        risk_score=risk_score,
        premium_amount=premium,
        policy_status="active"
    )

    db.add(new_policy)
    db.commit()
    db.refresh(new_policy)

    return {
        "message": "Policy created",
        "risk_score": risk_score,
        "premium": premium,
        "policy_id": new_policy.policy_id
    }