# Technical Methodology

### 1. Methodology: Why Rolling Median?
We chose the **3-month Rolling Median** as our baseline rather than a simple Mean. In Aadhaar data, manual entry errors or one-time massive events can skew the average. The Median provides a "Robust Baseline" that represents a true normal month, making shock detection much more accurate.

### 2. Detection Logic
* **Step 1:** Establish the baseline using a 3-month window.
* **Step 2:** Calculate the **Relative Deviation Score**: `(Actual - Baseline) / (Baseline + 1)`.
* **Step 3:** Trigger an Anomaly Flag if the score is > 1.0 (100% increase) or < -0.8 (80% decrease).

### 3. Known Limitations & Risks
* **False-Positive Risk:** Large-scale government registration camps or mandatory update deadlines may be flagged as shocks despite being planned.
* **Low Volume Districts:** Districts with very low activity (e.g., <10 updates/month) may show high percentage volatility that doesn't represent a real-world disaster.