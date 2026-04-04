from models.claim_model import Claim
from models.policy_model import WeeklyPolicy
from datetime import date

def create_claim(db, user_id, disruption_type, payout_amount):
    policy = db.query(WeeklyPolicy).filter(
        WeeklyPolicy.user_id == user_id,
        WeeklyPolicy.policy_status == "active"
    ).first()

    if not policy:
        return

    claim = Claim(
        user_id=user_id,
        policy_id=policy.policy_id,
        date=date.today(),
        disruption_type=disruption_type,
        payout_amount=payout_amount,
        claim_status="approved"
    )

    db.add(claim)
    db.commit()
    db.refresh(claim)

    return claim