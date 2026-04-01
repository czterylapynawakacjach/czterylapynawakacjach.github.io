import requests
import json
import os
from datetime import datetime

# Targeting the primary station for the Masovian Voivodeship
STATION_NAME = "warszawa" 
BASE_TEMP = 10.0
DATA_FILE = "src/data/hive_metrics.json"
MAX_ENTRIES = 40 # 5 days * 8 entries (every 3 hours)

def fetch_imgw_data():
    url = f"https://danepubliczne.imgw.pl/api/data/synop/station/{STATION_NAME}"
    try:
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        data = r.json()
        
        t_max = float(data['temperatura'])
        wind = float(data['predkosc_wiatru']) * 3.6 # convert m/s to km/h
        rain = float(data['suma_opadu'] or 0)
        
        # Calculations
        gdd = max(t_max - BASE_TEMP, 0)
        is_flyable = t_max > 14 and wind < 20 and rain == 0
        
        new_entry = {
            "timestamp": datetime.now().isoformat(),
            "date": datetime.now().strftime("%Y-%m-%d"),
            "temp": t_max,
            "wind": round(wind, 1),
            "rain": rain,
            "gdd_gain": round(gdd, 2),
            "status": "Optimal" if is_flyable else "Restricted",
            "humidity": data['wilgotnosc_wzgledna'],
            "pressure": data['cisnienie']
        }
        return new_entry
    except Exception as e:
        print(f"ETL Error: {e}")
        return None

def update_data():
    new_data = fetch_imgw_data()
    if not new_data:
        return

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            try:
                history = json.load(f)
            except json.JSONDecodeError:
                history = []
    else:
        history = []

    # Append new data
    history.append(new_data)
    
    # Keep only last MAX_ENTRIES
    if len(history) > MAX_ENTRIES:
        history = history[-MAX_ENTRIES:]

    with open(DATA_FILE, 'w') as f:
        json.dump(history, f, indent=2)
    
    print(f"Successfully updated hive metrics at {new_data['timestamp']}")

if __name__ == "__main__":
    update_data()
