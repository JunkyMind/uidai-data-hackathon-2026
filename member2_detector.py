import pandas as pd
import os

def run_m2_merged():
    input_file = '../outputs/features_master.csv'
    output_file = '../outputs/anomaly_output.csv'
    
    if not os.path.exists(input_file):
        print("Error: Run Member 1 script first.")
        return
        
    df = pd.read_csv(input_file)
    
    # Day 1: Baseline (Robust Median)
    df['baseline_med'] = df.groupby('district')['total_activity'].transform(lambda x: x.rolling(3, min_periods=1).median())
    
    # Day 2: Anomaly Detection
    df['deviation_score'] = (df['total_activity'] - df['baseline_med']) / (df['baseline_med'] + 1)
    df['is_anomaly'] = (df['deviation_score'] > 1.0) | (df['deviation_score'] < -0.8)
    
    df.to_csv(output_file, index=False)
    print(f"M2 Done: {df['is_anomaly'].sum()} shocks detected.")

if __name__ == "__main__":
    run_m2_merged()