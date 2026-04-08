# Technical Architecture: The Golden Apiary & Pet Hotel

This document outlines the high-performance, 100% static architecture used to deliver live beekeeping telemetry and a multi-version design portfolio.

```mermaid
graph TD
    %% External Data Sources
    IMGW("IMGW-PIB\n(Weather API)")
    RSS("RSS Feeds\n(Bee Journals)")
    GNews("Google News\n(Local Alerts)")

    %% Automation Layer (GitHub Actions)
    subgraph GitHub_Actions [Automation & ETL]
        WeatherSync("Weather Sync\n(Every 3h)")
        NewsSync("News Sync\n(Daily)")
        AstroBuild("Astro Static Build")
    end

    %% Data Layer
    subgraph Data_Storage [Static Data Layer]
        TelemetryJSON("telemetry.json\n(30-day High-Res)")
        ArchiveJSON("archive.json\n(2-year Seasonal)")
        NewsJSON("news.json\n(Aggregated Feed)")
    end

    %% Frontend Layer
    subgraph Frontend [Astro SSG]
        V1_V3("V1-V3 Portfolios\n(Clean / Forest / Artistic)")
        V4("V4 Golden Apiary\n(Live Dashboard)")
        Charts("Chart.js\n(Beekeeping Metrics)")
    end

    %% Hosting
    GH_Pages("GitHub Pages\n(Static Hosting)")

    %% Flows
    IMGW -->|JSON| WeatherSync
    RSS -->|XML| NewsSync
    GNews -->|XML| NewsSync
    
    WeatherSync -->|Python ETL| TelemetryJSON
    WeatherSync -->|Midnight Rollover| ArchiveJSON
    NewsSync -->|Python Aggregator| NewsJSON
    
    TelemetryJSON --> AstroBuild
    ArchiveJSON --> AstroBuild
    NewsJSON --> AstroBuild
    
    AstroBuild -->|Build Artifacts| GH_Pages
    
    GH_Pages -->|Delivers| Frontend
```

### 1. The Data Pipeline (ETL)
The application uses a **"Static-Dynamic"** pattern. While the site is 100% static, it is rebuilt frequently to reflect fresh data.
- **Weather ETL (`fetch_weather.py`):** Fetches data from IMGW-PIB every 3 hours. It calculates specialized beekeeping metrics like **GDD (Growing Degree Days)** and **Delta T (Nectar Flow Index)**.
- **News Aggregator (`fetch_news.py`):** Runs daily to pull the latest industry updates and hyper-local alerts for the Wołomin area.
- **Midnight Rollover:** The system automatically summarizes hourly telemetry into daily historical records in `archive.json`.

### 2. Multi-Version Design Core
The project serves four distinct design identities from a single codebase:
- **V1 (Professional):** Trust-focused, clean layout.
- **V2 (Forest Boutique):** Luxury aesthetic with organic elements.
- **V3 (Experimental):** Broken grids and cinematic interactions.
- **V4 (Golden Apiary):** High-utility beekeeping dashboard with physics-based UI elements.

### 3. Beekeeping Intelligence (V4)
The V4 dashboard implements specific biological logic:
- **Foraging Window:** Logic-driven status (Optimal/Marginal/Restricted) based on temperature, wind (>20 km/h), and precipitation.
- **Thermal Envelope:** Comparative visualization of current temp vs. 24h rolling min/max.
- **Nectar Washout:** Tracking rainfall impact on nectar availability (48h recovery logic).

### 4. Technical Stack
- **Framework:** Astro (Static Site Generation)
- **Styling:** Tailwind CSS (Utility-first)
- **Visuals:** Chart.js (Telemetry), Mermaid.js (Architecture Diagrams)
- **Hosting:** GitHub Pages
- **Interactivity:** Vanilla JS (Magnetic physics, bee-cursor)
