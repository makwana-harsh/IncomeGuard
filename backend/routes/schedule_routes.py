from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.schedule_model import DailySchedule
from schemas.schedule_schema import ScheduleCreate

router = APIRouter()

@router.post("/add")
def add_schedule(schedule: ScheduleCreate, db: Session = Depends(get_db)):
    new_schedule = DailySchedule(
        user_id=schedule.user_id,
        date=schedule.date,
        start_time=schedule.start_time,
        end_time=schedule.end_time,
        location=schedule.location
    )

    db.add(new_schedule)
    db.commit()
    db.refresh(new_schedule)

    return {"message": "Schedule added"}
    

@router.get("/{user_id}")
def get_schedule(user_id: int, db: Session = Depends(get_db)):
    schedules = db.query(DailySchedule).filter(DailySchedule.user_id == user_id).all()
    return schedules