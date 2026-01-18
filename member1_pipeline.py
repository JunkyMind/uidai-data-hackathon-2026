import pandas as pd
import os
import glob

def run_m1_merged():
    data_path = '../data/'
    output_path = '../outputs/features_master.csv'
    
    # Day 1: Merge Cleaning
    files = glob.glob(os.path.join(data_path, "api_data_aadhar_enrolment_*.csv"))
    if not files:
        print("Error: No enrolment files found in /data/")
        return
        
    df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
    df['date'] = pd.to_datetime(df['date'], dayfirst=True)
    df['district'] = df['district'].str.strip().str.title()
    
    # Day 2: Features
    # Aggregating by month
    master = df.groupby(['state', 'district', df['date'].dt.year.rename('year'), df['date'].dt.month.rename('month')]).sum(numeric_only=True).reset_index()
    
    # Total activity based on your file's age columns
    master['total_activity'] = master[['age_0_5', 'age_5_17', 'age_18_greater']].sum(axis=1)
    
    # Rolling and Seasons
    master['roll_3m'] = master.groupby('district')['total_activity'].transform(lambda x: x.rolling(3, min_periods=1).mean())
    master['season'] = master['month'].apply(lambda m: 'Monsoon' if 6<=m<=9 else ('Festival' if 10<=m<=12 else 'Non-peak'))
    
    master.to_csv(output_path, index=False)
    print("M1 Done: features_master.csv created.")

if __name__ == "__main__":
    run_m1_merged()