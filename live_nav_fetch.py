import requests
import pandas as pd
import os

# Create raw directory if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

# Define the scheme codes to fetch
schemes = {
    "125497": "HDFC_Top_100",
    "119551": "SBI_Bluechip",
    "120503": "ICICI_Bluechip",
    "118632": "Nippon_Large_Cap",
    "119092": "Axis_Bluechip",
    "120841": "Kotak_Bluechip"
}

def fetch_and_save_nav(scheme_code, name):
    url = f"https://api.mfapi.in/mf/{scheme_code}"
    print(f"Fetching data for {name} ({scheme_code})...")
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "data" in data:
            df = pd.DataFrame(data["data"])
            file_path = f"data/raw/{name}_{scheme_code}.csv"
            df.to_csv(file_path, index=False)
            print(f"Saved: {file_path}")
        else:
            print(f"No NAV data found for {scheme_code}")
    else:
        print(f"Failed to fetch {scheme_code}. Status: {response.status_code}")

for code, name in schemes.items():
    fetch_and_save_nav(code, name)
    
print("Live NAV fetch complete.")
