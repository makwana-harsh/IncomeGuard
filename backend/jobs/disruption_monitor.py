from sqlalchemy.orm import Session
from database import SessionLocal
from utils.weather_api import get_weather
from models.schedule_model import DailySchedule
from services.claim_service import create_claim
from services.payment_service import make_payment
from datetime import date

RAIN_THRESHOLD = 50
TEMP_THRESHOLD = 42

def run_disruption_monitor():
    db: Session = SessionLocal()

    today = date.today()

    schedules = db.query(DailySchedule).filter(DailySchedule.date == today).all()

    for schedule in schedules:
        weather = get_weather(schedule.location)

        disruption_type = None
        payout = 0

        if weather["rain"] > RAIN_THRESHOLD:
            disruption_type = "heavy_rain"
            payout = 300

        elif weather["temperature"] > TEMP_THRESHOLD:
            disruption_type = "extreme_heat"
            payout = 250

        if disruption_type:
            claim = create_claim(db, schedule.user_id, disruption_type, payout)
            if claim:
                make_payment(db, claim)

    db.close()