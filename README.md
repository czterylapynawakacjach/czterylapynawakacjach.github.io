# Pet Hotel & Apiary Portfolio

A high-end, multi-version design portfolio built with **Astro**, **Tailwind CSS**, and **Python**. This project showcases different creative directions for a pet boarding business and an educational apiary, featuring advanced telemetry and cinematic interactivity.

## 🚀 Live Site
The site is automatically deployed to GitHub Pages via GitHub Actions.
URL: [https://czterylapynawakacjach.github.io/](https://czterylapynawakacjach.github.io/)

## 🎨 Design Versions
*   **V1 (Clean & Classic)**: A professional, trustworthy layout using standard web patterns and a calming blue palette.
*   **V2 (Forest Boutique)**: A luxurious, nature-inspired design with soft serif typography and organic elements.
*   **V3 (Artistic & Brave)**: An experimental broken-grid experience with cinematic interactions and animal-personality physics.
*   **V4 (The Golden Apiary)**: A high-energy, artisanal theme for an educational bee homestead, featuring a "Bee-Ops" telemetry dashboard.

## 🐝 "Bee-Ops" Dashboard (V4 Exclusive)
The apiary section features a semi-dynamic dashboard powered by a custom ETL pipeline:
*   **Data Source**: Live meteorological data from IMGW-PIB (Warsaw station).
*   **Update Cycle**: 3-hourly automated refresh via GitHub Actions.
*   **Metrics**: Growing Degree Days (GDD), Nectar Washout correlation, Foraging Window, and Barometric Panic signals.
*   **Visuals**: Custom **Chart.js** implementations with a "Forest Boutique" high-energy skin.

## 🛠️ Technical Stack
*   **Framework**: Astro (Static Site Generator)
*   **Styling**: Tailwind CSS
*   **Data Architecture**: 
    *   `telemetry.json`: High-resolution 3-hourly data (30-day window).
    *   `archive.json`: Daily summarized history (2-year archival).
*   **Automation**: 
    *   Python-based ETL script for weather processing.
    *   GitHub Actions for data synchronization and automatic site rebuilds.
*   **Interactivity**: Vanilla JS (Magnetic buttons, bee-cursor tracking, cinematic spotlights).
*   **Diagrams**: Mermaid.js for technical architectural documentation.

## 🌍 Multilingual
Fully localized in **Polish** (Primary) and **English** using a custom version-aware i18n routing system.

---
Built with 🐾 and 🐝 by Robert.
