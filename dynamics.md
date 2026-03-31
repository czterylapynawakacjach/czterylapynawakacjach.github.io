This summary is optimized for ingestion by a CLI or another LLM session. It encapsulates the full architectural vision, the specific Polish data requirements, and the technical implementation using **Astro**, **Tailwind**, and **GitHub Actions**.

---

# 🐝 Project: The "Bee-Ops" Dashboard (Wołomin, PL)

## 📖 Background & Purpose
The goal is to build a high-utility, data-driven website for a beekeeper in **Wołomin, Poland**. By treating the apiary as a "managed cluster," we use environmental telemetry to optimize **honey production** today and **queen breeding** tomorrow. 

The site uses a **Semi-Dynamic Architecture**: a static frontend powered by **Astro** and **Tailwind CSS**, with data-heavy "background" content updated via **GitHub Actions (ETL)**. This provides the speed of a static site with the utility of a live dashboard—without the cost of a running server.

---

## 📈 Beekeeping Metrics (The "KPIs")
* **Growing Degree Days (GDD):** Heat accumulation (Base $10\text{°C}$) to predict the bloom of nectar sources like Linden or Acacia.
* **Foraging Window:** Active uptime tracking. Logic: $T > 14\text{°C}$, Wind $< 20\text{ km/h}$, and $0\text{ mm}$ Rain.
* **Delta T ($\Delta T$):** The spread between dry/wet bulb temps. High $\Delta T$ dries out nectar; low $\Delta T$ makes nectar too watery for efficient honey curing.
* **Inspection Window:** Calculates Solar Noon $\pm 2$ hours, when foragers are away and the hive is most docile.

---

## 🛠️ Technical Architecture

### 1. The Stack
* **Frontend:** Astro + Tailwind CSS.
* **Backend (Serverless ETL):** GitHub Actions + Python.
* **Data Source:** IMGW-PIB (Official Polish Meteorological Data).
* **Storage:** `src/data/hive_metrics.json` (Git-backed database).

### 2. Data Fetcher (`scripts/fetch_weather.py`)
This script uses the IMGW-PIB name-based endpoint for maximum reliability.

```python
import requests
import json
from datetime import datetime

# Targeting the primary station for the Masovian Voivodeship
STATION_NAME = "warszawa" 
BASE_TEMP = 10.0

def fetch_imgw_data():
    url = f"https://danepubliczne.imgw.pl/api/data/synop/station/{STATION_NAME}"
    try:
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        data = r.json()
        
        t_max = float(data['temperatura'])
        wind = float(data['predkosc_wiatru']) * 3.6 # convert m/s to km/h
        rain = float(data['suma_opadu'])
        
        # Calculations
        gdd = max(t_max - BASE_TEMP, 0)
        is_flyable = t_max > 14 and wind < 20 and rain == 0
        
        return {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "temp": t_max,
            "wind": wind,
            "rain": rain,
            "gdd_gain": round(gdd, 2),
            "status": "Optimal" if is_flyable else "Restricted",
            "humidity": data['wilgotnosc_wzgledna'],
            "pressure": data['cisnienie']
        }
    except Exception as e:
        print(f"ETL Error: {e}")
        return None

# Script appends to src/data/hive_metrics.json
```

### 3. GitHub Action (`.github/workflows/data_sync.yml`)
Triggers the ETL and automatically redeploys the Astro site.

```yaml
name: Hive Telemetry Sync
on:
  schedule:
    - cron: '0 5 * * *' # 5 AM daily (CET)
  workflow_dispatch:

jobs:
  sync_and_deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Fetch & Process
        run: python scripts/fetch_weather.py
      - name: Commit Data
        run: |
          git config user.name "BeeBot"
          git add src/data/hive_metrics.json
          git commit -m "chore: update daily hive telemetry"
          git push
      # Astro build/deploy step follows...
```

---

## 🎨 Visualization & Astro Integration

### Tailwind-Powered Gauges
Since Astro components are server-rendered, we can pre-calculate the "Foraging Score" and use Tailwind to color-code the dashboard:
* **Success:** `text-green-500` (Optimal for honey).
* **Warning:** `text-amber-500` (Sub-optimal, high humidity).
* **Danger:** `text-red-500` (No flight, bees consuming honey stores).

### Visual Concepts
* **The "Flow Chart":** A simple line graph (using **Chart.js** or **SVG**) showing accumulated GDD vs. historical averages for the Wołomin region.
* **Queen Calendar:** A Gantt-style timeline component. Input: `grafting_date`. Output: A schedule of capping, emergence, and mating flights, styled with Tailwind's grid/flexbox.
* **Inspection Arc:** A CSS-based sun-path visualizer showing the "Gold Window" for hive work.

### Astro Component Snippet
```astro
---
import metrics from '../data/hive_metrics.json';
const today = metrics[metrics.length - 1];
---
<div class="p-6 bg-slate-900 rounded-xl border border-amber-500/20">
  <h2 class="text-amber-500 font-bold uppercase tracking-widest">Hive Status</h2>
  <p class="text-4xl font-black text-white">{today.temp}°C</p>
  <div class:list={['mt-2 font-semibold', today.status === 'Optimal' ? 'text-green-400' : 'text-red-400']}>
    Foraging: {today.status}
  </div>
</div>
```

---

## 🚀 Roadmap
1.  **Honey Production:** Focus on tracking GDD to time the placement of honey supers.
2.  **Queen Breeding:** Integrate weather-weighted mating flight predictions.
3.  **IoT Integration:** Future expansion for ESP32 load cells (weight) and microphones (acoustic swarm prediction).