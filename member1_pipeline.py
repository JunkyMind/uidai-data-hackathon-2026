import pandas as pd
import os
import glob

def run_m1_final_pipeline():
    data_path = '../data/'
    output_dir = '../outputs/'
    
    
    all_files = glob.glob(os.path.join(data_path, "api_data_aadhar_enrolment_*.csv"))
    if not all_files:
        print("Error: /data/folder not found ")
        return

    df_list = [pd.read_csv(f) for f in all_files]
    df = pd.concat(df_list, ignore_index=True)

  
    junk_val = ['100000', 100000]
    df = df[~df['state'].isin(junk_val)]
    df = df[~df['district'].isin(junk_val)]
    df = df[~df['pincode'].isin(junk_val)]

   
    df['date'] = pd.to_datetime(df['date'], dayfirst=True)
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['district'] = df['district'].str.strip().str.title()

    
    activity_cols = ['age_0_5', 'age_5_17', 'age_18_greater']
    master = df.groupby(['state', 'district', 'pincode', 'year', 'month'])[activity_cols].sum().reset_index()

  
    master['total_activity'] = master[activity_cols].sum(axis=1)
    
    
    master = master.sort_values(['pincode', 'year', 'month'])
    master['roll_3m'] = master.groupby('pincode')['total_activity'].transform(
        lambda x: x.rolling(3, min_periods=1).mean()
    )
    
    master['season'] = master['month'].apply(
        lambda m: 'Monsoon' if 6<=m<=9 else ('Festival' if 10<=m<=12 else 'Non-peak')
    )

    master.to_csv(os.path.join(output_dir, 'features_master.csv'), index=False)
    print("M1: Junk removed and Pincode aggregation fixed.")

if __name__ == "__main__":
    run_m1_final_pipeline()
