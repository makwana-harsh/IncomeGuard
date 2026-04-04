# IncomeGuard

Phase 1 
# Persona
We are building for food delivery partners working on platforms like Zomato and Swiggy in urban areas.

# Problem Definition
Delivery workers lose income due to external disruptions such as heavy rain, high temperature, and high wind speed. These events reduce their 
working hours, but there is no system to compensate for this loss.

# Weekly Premium Model
Premium is determined using AI-based risk scoring based on the worker’s operating zone.
High-risk areas (frequent rain/high temperature/high flood chances) have slightly higher premiums.
The system provides flexible weekly plans like :
- Basic plan -> ₹50/week Premium -> ₹250/day payout
- Standard plan -> ₹70/week Premium -> ₹400/day payout 
- Premium	plan -> ₹100/week Premium-> ₹700/day payout 

# Parametric Triggers
Claims are triggered automatically when predefined conditions are met:
- Rainfall 50–80mm → partial payout
- Rainfall > 80mm → full payout
- AQI > 400 → Pollution-based disruption payout
- Zone Status = CLOSED → Full payout (curfew/strike)

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
- Backend: FastAPI
- Frontend: React
- Database: MySQL
- APIs: open-meteo api
- ML: Python (Scikit-learn)



Phase 2

#### About Weekly Premium Model
Premium is determined using an AI-driven risk scoring system powered by a trained Random Forest model.
- The Random Forest model is trained on 4 years of historical weather data collected from 9 major Indian cities.
- ahmedabad, pune, mumbai, delhi, chennai, bangalore, jaipur, kolkata, hyderabad
- The dataset includes featues like:
  - Location relative max rain intensity
  - Location relative max rain hours
  - Location relative high wind speed
  - Location relative high rain + flood
  - Location relative extreme heat hours
  - Location relative extreme cold hours etc.
- Total 7500+ historical data samples enables the model to learn patterns between environmental conditions and potential income disruption risks.

# Risk Prediction Approach
- For each worker, the system fetches next week's weather forecast based on their operating location.
- The forecast data is:
  - Preprocessed
  - Normalized relative to the worker’s location
- The processed features are then passed into the trained Random Forest model.

# Risk Scoring
- The model outputs a risk score (0–1) indicating the probability of income disruption in the upcoming week.

# Premium Adjustment Logic
- The predicted risk score is used to dynamically adjust the weekly premium:
  - Low Risk → Lower premium
  - Moderate Risk → Standard premium
  - High Risk → Higher premium 

# Weekly Plans
The system provides flexible weekly plans like :
- Basic plan -> ₹50/week Premium -> ₹250/day payout
- Standard plan -> ₹70/week Premium -> ₹400/day payout 
- Premium	plan -> ₹100/week Premium-> ₹700/day payout 


#### About Parametric Triggers
In Phase 2, we transitioned from rule-based triggers to an AI-driven trigger mechanism using the same trained Random Forest model.

  # Previous Approach (Phase 1)
  - Fixed thresholds such as:
    - Rainfall > 80mm → payout
    - High temperature > 45 degree cel → payout
  This approach lacked flexibility and could not accurately capture real-world disruption patterns.
  
  # Updated Approach (Phase 2)
  We now use a machine learning-based trigger system:
  1. The system fetches real-time weather data for the worker’s location.
  2. Data is filtered specifically for the worker’s active working hours.
  3. Relevant features are extracted, such as:
     - Rainfall during working hours
     - Max rain intensity
     - High rain + flood
     - Extreme heat hours
     - Extreme cold hours
  4. The processed data is fed into the trained Random Forest model.
  
  # Decision Logic
  - The model predicts a risk probability of income disruption.
  - If : Risk Probability ≥ 0.85 (85%)
        → Claim is automatically triggered  
        → Payout is processed  
  - Otherwise:
        → No payout is initiated  
  
  # Key Advantages
  - Eliminates rigid thresholds and edge-case errors
  - Captures combined effects (e.g., heavy rain + flood hours+ High speed wind)
  - Personalized decision-making based on worker’s location and timing
  - More robust against manipulation and false claims
  
  # Automatic Payout
  - System uses actual observed data instead of forecast because claiming process is done after finishing the woking hours of worker
  - Ensures payouts are based on real disruptions experienced, not predictions
  - if predicted risk from the model is above or equal 85% then payout is processed.

#### Reason Behind Using the Same Model for Premium & Triggers
- The Random Forest model is trained on feature-based representations of weather conditions rather than time-specific sequences.
- Instead of depending on whether the data represents 7 days or 1 day, the model learns patterns from engineered features such as:
  - Location relative max rain hours
  - Location relative high wind speed
  - Location relative high rain + flood etc.

- Therefore, by extracting the same set of features from:
  - Weekly forecast data (for premium calculation)
  - Daily real-time data (for claim triggering), we ensure consistency in model input and predictions.

# Generalization Capability
- The model is trained on 7500+ real historical samples across diverse weather conditions and cities, enabling it to generalize well across different scenarios.
- This allows it to reliably predict disruption risk for both:
  - Aggregated weekly data
  - Single-day real-time data
    
# Forecast vs Real Data Usage
- When using forecast data:
  - The model predicts the expected risk of income loss
  - This is used for premium pricing

- When using real observed data:
  - The model predicts the actual likelihood of income disruption
  - This is used for claim triggering and payout decisions


#### System Workflow
1. User Onboarding
- A new user registers and creates an account on the platform.

2. Premium Discovery & Risk Assessment
- The user clicks on "Show Available Plans".
- The system collects:
  - Current working location
  - Daily working hours (start time – end time)

- This information is mandatory because:
  - Risk varies by location
  - Disruptions only matter during active working hours

- The system:
  - Fetches upcoming week's weather forecast for that entered location
  - Processes and normalizes the data relative to the selected location
  - Feeds it into the trained Random Forest model

- Based on predicted risk, the system dynamically suggests suitable weekly plans.
  
3. Plan Selection & Locking
- The user selects a weekly insurance plan (Basic / Standard / Premium).
- Once selected:
  - Plan is locked for 1 week
  - Location is locked for 1 week
  - Working hours are locked for 1 week

- This prevents:
  - Fraudulent manipulation
  - Frequent changes to exploit payouts

4. Daily Automated Monitoring
- For each day of the active week:
  - After the user’s working hours end:
    - The system automatically triggers evaluation

- The system:
  - Fetches real-time weather data (via API)
  - Filters data for the user’s working hours only
  - Extracts relevant features
  - Sends data to the Random Forest model

5. Claim Decision & Payout
- The model predicts disruption risk probability
- If: Risk ≥ 85%
  → Claim is automatically approved  
  → Payout is processed  
- Else:
  → Claim is rejected  

- This process runs daily during the policy week
  
6. Weekly Cycle Reset
- At the end of the week:
  - The policy expires
  - User can:
    - Select a new plan
    - Update location
    - Update working hours

#### Design Decisions & Justification

# Why Multiple Plans?
- Different users have different affordability levels
- Ensures inclusivity across income segments

# Why Capture Location?
- Gig workers operate in dynamic locations
- Risk varies significantly across cities and zones

# Why Capture Working Hours?
- Disruptions only matter if they occur during working time
- Prevents false payouts (e.g., rain at night when user is not working)

# Why Location-Normalized Features?
- Environmental conditions vary by city
- Example:
  - AQI 200 may be normal in Delhi
  - But severe in Pune
- Normalization ensures fair and accurate risk prediction

# Why Daily Evaluation Instead of Weekly?
- Ensures precise and fair payouts
- Captures real disruptions instead of aggregated assumptions

