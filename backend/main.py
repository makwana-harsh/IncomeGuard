from fastapi import FastAPI
from database import engine, Base
from apscheduler.schedulers.background import BackgroundScheduler
from jobs.disruption_monitor import run_disruption_monitor
from fastapi.middleware.cors import CORSMiddleware

from models import user_model, policy_model, schedule_model, claim_model, payment_model
from routes import auth_routes, policy_routes, schedule_routes


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
app.include_router(policy_routes.router, prefix="/policy", tags=["Policy"])
app.include_router(schedule_routes.router, prefix="/schedule", tags=["Schedule"])

scheduler = BackgroundScheduler()
scheduler.add_job(run_disruption_monitor, "interval", hours=3)
scheduler.start()

@app.get("/")
def root():
    return {"message": "API Running"}

