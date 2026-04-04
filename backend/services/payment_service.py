from models.payment_model import Payment
import uuid

def make_payment(db, claim):
    payment = Payment(
        claim_id=claim.claim_id,
        user_id=claim.user_id,
        amount=claim.payout_amount,
        payment_status="success",
        payment_method="UPI",
        transaction_id=str(uuid.uuid4())
    )

    db.add(payment)
    db.commit()