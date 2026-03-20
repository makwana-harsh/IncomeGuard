# IncomeGuard


# Persona
We are building for food delivery partners working on platforms like Zomato and Swiggy in urban areas.

# Problem Definition
Delivery workers lose income due to external disruptions such as heavy rain, pollution, and curfews. These events reduce their 
working hours, but there is no system to compensate for this loss.

# Weekly Premium Model
Premium is determined using AI-based risk scoring based on the worker’s operating zone.
High-risk areas (frequent rain/pollution) have slightly higher premiums.
The system provides flexible weekly plans:
Plan	    Premium (per week)	Payout (per day)	Max Coverage
Basic	           ₹20	              ₹300	      3 days/week
Standard	       ₹30	              ₹500	      3 days/week
Premium	         ₹50	              ₹800	      4 days/week

# Parametric Triggers
Claims are triggered automatically when predefined conditions are met:
Rainfall 50–80mm → partial payout
Rainfall > 80mm → full payout
AQI > 400 → Pollution-based disruption payout
Zone Status = CLOSED → Full payout (curfew/strike)

# Claim Logic
When a trigger is activated:
- System detects disruption
- Claim is automatically generated
- Fraud checks are applied
- Payout is processed if valid

# Adversarial Defense & Anti-Spoofing Strategy
The system uses a multi-layer fraud detection approach:
- Multi-signal validation (weather + location + activity)
- Behavioral analysis (historical activity vs current)
- Peer comparison (compare with other workers in same zone)
- Anomaly detection (sudden claim spikes)
- Location consistency checks
- Rate limiting (weekly payout caps)
- Risk scoring for each claim
This ensures that coordinated fraud attacks such as GPS spoofing 
and mass fake claims are detected and prevented.

# AI/ML Usage
- Risk scoring for premium calculation
- Fraud detection via anomaly detection
- Behavioral pattern analysis

# System Workflow
1. User registers
2. Selects plan
3. System monitors environment
4. Trigger detected
5. Claim auto-created
6. Fraud check
7. Payout processed

# Tech Stack
Backend: FastAPI
Frontend: React
Database: MySQL
APIs: Weather API, AQI API
ML: Python (Scikit-learn)

