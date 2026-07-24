import pandas as pd
import glob
import os

def explore_csv_files(directory_path="data/raw"):
    csv_files = glob.glob(f"{directory_path}/*.csv")
    if not csv_files:
        print("No CSV files found to explore yet. Run live_nav_fetch.py first, or add the 10 provided CSVs.")
        return
        
    for file in csv_files:
        print(f"\n--- Exploring {os.path.basename(file)} ---")
        try:
            df = pd.read_csv(file)
            print(f"Shape: {df.shape}")
            print("\nData Types:")
            print(df.dtypes)
            print("\nHead (first 3 rows):")
            print(df.head(3))
        except Exception as e:
            print(f"Error reading {file}: {e}")

def explore_fund_master(fund_master_path):
    if not os.path.exists(fund_master_path):
        print(f"\n{fund_master_path} not found. Skipping fund_master exploration.")
        return
        
    df = pd.read_csv(fund_master_path)
    print("\n--- Fund Master Exploration ---")
    for col in ['fund_house', 'category', 'sub_category', 'risk_grade']:
        if col in df.columns:
            print(f"Unique {col}s: {df[col].nunique()}")
            print(df[col].unique()[:5]) 

def validate_amfi_codes(fund_master_path, nav_history_path):
    if not os.path.exists(fund_master_path) or not os.path.exists(nav_history_path):
        return
        
    print("\n--- Validating AMFI Codes ---")
    funds_df = pd.read_csv(fund_master_path)
    nav_df = pd.read_csv(nav_history_path)
    
    if 'amfi_code' in funds_df.columns and 'amfi_code' in nav_df.columns:
        master_codes = set(funds_df['amfi_code'])
        history_codes = set(nav_df['amfi_code'])
        
        missing_in_history = master_codes - history_codes
        print(f"Total codes in master: {len(master_codes)}")
        print(f"Total codes in history: {len(history_codes)}")
        print(f"Orphaned codes (in master but no history): {len(missing_in_history)}")

if __name__ == "__main__":
    explore_csv_files()
    # Replace these paths once you have the actual CSV files provided by your team
    explore_fund_master("data/raw/fund_master.csv")
    validate_amfi_codes("data/raw/fund_master.csv", "data/raw/nav_history.csv")
