def calculate_risk_and_premium(location, planned_work_hours):
    risk_score = 1.0

    # Example rule logic
    if planned_work_hours > 50:
        risk_score += 0.2
    if planned_work_hours > 70:
        risk_score += 0.3

    # Location risk (mock for now)
    risky_locations = ["Mumbai", "Chennai", "Kolkata"]
    if location in risky_locations:
        risk_score += 0.3

    base_premium = 50
    premium = base_premium * risk_score

    return risk_score, premium