

### 1. Datasets Used
* **Data Source:** Official UIDAI Aadhaar Enrolment and Update datasets (API/Sandbox source).
* **Time Period Covered:** March 2025 to December 2025.
* **Geographic Coverage:** Pan-India coverage, aggregated at the district level for all States and Union Territories.

### 2. Data Dictionary

| Column Name | Description | Units |
| :--- | :--- | :--- |
| state | Name of the State or Union Territory | String |
| district | Normalized name of the District | String |
| year | Calendar year of the record | Integer |
| month | Calendar month (1-12) | Integer |
| total_updates | Combined count of Demographic and Biometric updates | Count |
| roll_3m | 3-month rolling average of update activity | Count |
| mom_pct | Month-on-Month percentage change in activity | Percentage (%) |
| season | Seasonal category (Monsoon, Festival, Non-peak) | String |
| deviation_score| Calculation of how far data is from the baseline | Float |
| is_anomaly | Flag indicating a significant shock event | Boolean (True/False) |