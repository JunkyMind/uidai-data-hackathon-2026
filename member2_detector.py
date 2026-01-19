import pandas as pd
import os

def run_m2_final_detector():
    input_path = '../outputs/features_master.csv'
    output_path = '../outputs/anomaly_output.csv'

    if not os.path.exists(input_path):
        print("Error: features_master.csv not found")
        return

    df = pd.read_csv(input_path)

   
    df['baseline_med'] = df.groupby('pincode')['total_activity'].transform(
        lambda x: x.rolling(3, min_periods=1).median()
    )

    
    df['deviation_score'] = (df['total_activity'] - df['baseline_med']) / (df['baseline_med'] + 1)
    
    
    df['is_anomaly'] = (df['deviation_score'] > 1.0) | (df['deviation_score'] < -0.8)

    df.to_csv(output_path, index=False)
    print(f"M2: Analysis complete. {df['is_anomaly'].sum()} shocks detected at pincode level.")

if __name__ == "__main__":
    run_m2_final_detector()
