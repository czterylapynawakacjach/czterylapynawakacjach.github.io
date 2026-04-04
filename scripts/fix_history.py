import json
from datetime import datetime, timedelta

def fix_data():
    with open('src/data/telemetry.json', 'r') as f:
        telemetry = json.load(f)
    
    with open('src/data/archive.json', 'r') as f:
        archive = json.load(f)

    # 1. Update Telemetry with rolling_gdd and delta_t
    BASE_TEMP = 10.0
    for i in range(len(telemetry)):
        # Delta T Calculation
        temp = float(telemetry[i]['temp'])
        humidity = float(telemetry[i]['humidity'])
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

    # 2. Add April 3rd to Archive
    apr3_data = [t for t in telemetry if t['date'] == '2026-04-03']
    if apr3_data:
        t_max = max(t['temp'] for t in apr3_data)
        t_min = min(t['temp'] for t in apr3_data)
        avg_p = sum(float(t['pressure']) for t in apr3_data) / len(apr3_data)
        avg_h = sum(float(t['humidity']) for t in apr3_data) / len(apr3_data)
        total_r = sum(t['rain'] for t in apr3_data)
        
        daily_gdd = round(max(((t_max + t_min) / 2) - BASE_TEMP, 0), 2)
        last_cumulative = archive[-1]['cumulative_gdd'] if archive else 0
        
        # Check if already exists
        if not any(a['date'] == '2026-04-03' for a in archive):
            archive.append({
                "date": "2026-04-03",
                "t_max": t_max,
                "t_min": t_min,
                "avg_pressure": round(avg_p, 1),
                "total_rain": round(total_r, 1),
                "avg_humidity": round(avg_h, 1),
                "daily_gdd": daily_gdd,
                "cumulative_gdd": round(last_cumulative + daily_gdd, 2)
            })

    # 3. Save
    with open('src/data/telemetry.json', 'w') as f:
        json.dump(telemetry, f, indent=2)
    with open('src/data/archive.json', 'w') as f:
        json.dump(archive, f, indent=2)

if __name__ == "__main__":
    fix_data()
