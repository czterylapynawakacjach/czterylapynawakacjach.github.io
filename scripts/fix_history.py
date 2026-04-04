import json
from datetime import datetime, timedelta

def fix_data():
    with open('src/data/telemetry.json', 'r') as f:
        telemetry = json.load(f)
    
    with open('src/data/archive.json', 'r') as f:
        archive = json.load(f)

    BASE_TEMP = 10.0

    # 1. Update Telemetry with 3-tier status and rolling_gdd
    for i in range(len(telemetry)):
        temp = float(telemetry[i]['temp'])
        humidity = float(telemetry[i]['humidity'])
        wind = float(telemetry[i]['wind'])
        rain = float(telemetry[i]['rain'])
        
        # 3-Tier Status Logic
        if rain > 0 or temp < 10:
            status = "Restricted"
        elif temp > 14 and wind < 20:
            status = "Optimal"
        else:
            status = "Marginal"
        
        telemetry[i]['status'] = status
        telemetry[i]['delta_t'] = round(temp * (1 - (humidity / 100)), 1)

        # Rolling GDD
        now_dt = datetime.fromisoformat(telemetry[i]['timestamp'].replace('Z', ''))
        window_start = now_dt - timedelta(hours=24)
        window = [t for t in telemetry[:i+1] if datetime.fromisoformat(t['timestamp'].replace('Z', '')) >= window_start]
        
        if window:
            r_max = max(t['temp'] for t in window)
            r_min = min(t['temp'] for t in window)
            telemetry[i]['rolling_gdd'] = round(max(((r_max + r_min) / 2) - BASE_TEMP, 0), 2)
        else:
            telemetry[i]['rolling_gdd'] = 0

    # 2. Update Archive with flight_hours and avg_delta_t
    for i in range(len(archive)):
        day = archive[i]['date']
        day_data = [t for t in telemetry if t['date'] == day]
        
        if day_data:
            optimal_slots = sum(1 for t in day_data if t['status'] == "Optimal")
            archive[i]['flight_hours'] = optimal_slots * 3
            archive[i]['avg_delta_t'] = round(sum(t.get('delta_t', 0) for t in day_data) / len(day_data), 1)
        else:
            # Fallback for days not in telemetry but in archive
            if 'flight_hours' not in archive[i]:
                archive[i]['flight_hours'] = 0
            if 'avg_delta_t' not in archive[i]:
                archive[i]['avg_delta_t'] = 0

    # 3. Save
    with open('src/data/telemetry.json', 'w') as f:
        json.dump(telemetry, f, indent=2)
    with open('src/data/archive.json', 'w') as f:
        json.dump(archive, f, indent=2)

if __name__ == "__main__":
    fix_data()
