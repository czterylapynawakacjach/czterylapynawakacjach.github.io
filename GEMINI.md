# Pet Hotel Website - Project Context

## 1. Project Overview & Goal
Build a modern, static, multilingual website for a dog/cat boarding hotel. This project has evolved into a **Design Portfolio** showcasing four distinct creative directions (v1, v2, v3, v4) to allow the owner to choose their preferred brand identity.

## 2. Technical Stack
*   **Framework:** Astro (Static Site Generator)
*   **Styling:** Tailwind CSS (Utility-first)
*   **Typography:** Fraunces (Headings), Inter (Body) - via @fontsource
*   **Content:** File-based MDX for the blog and Markdown for supporting documents.
*   **Data Architecture (V4 Dashboard)**: 
    *   `telemetry.json`: 3-hourly high-resolution data (30-day window).
    *   `archive.json`: Daily summarized metrics (2-year history).
    *   **Logic**: Rolling 24h GDD calculation, midnight archival rollover.
*   **Diagrams:** Mermaid.js (Client-side rendering for technical architecture).
*   **Automation**: Python ETL script + GitHub Actions for 3-hourly sync and automatic site rebuilds.
*   **Interactivity:** Vanilla JS (Magnetic physics, bee-cursor, cinematic spotlights).
*   **Forms:** Formspree (Form-as-a-service) for contact/booking.

## 3. Site Structure & Features
*   **Root (/)**: Portfolio selection page to choose between Design Versions.
*   **Design Versions**:
    *   **V1 (Clean & Classic)**: Professional, trustworthy blue/white layout.
    *   **V2 (Forest Boutique)**: Luxurious, nature-inspired design with soft serifs and organic elements.
    *   **V3 (Artistic & Brave)**: Experimental broken-grid, cinematic interactions, and unique animal-personality physics.
    *   **V4 (The Golden Apiary)**: Fun, interactive artisanal theme with amber palette and a live "Bee-Ops" telemetry dashboard.
*   **Supporting Docs**: Individual HTML pages converted from Markdown (Business Plan, Technical Architecture, etc.).
*   **Languages**: Polish (Primary/Default) and English. Managed via version-aware i18n routing.

## 4. Architectural Mandates
*   **100% Static:** The final build must be completely static (npm run build) to be hosted on GitHub Pages.
*   **Semi-Dynamic Refresh:** The V4 dashboard relies on automated site rebuilds every 3 hours to reflect fresh JSON telemetry.
*   **Version Independence:** Each design version must remain visually and structurally isolated in its own layouts and components folder.
*   **i18n Routing:** Custom version-aware routing handling paths like `/v4/pl/bee-ops/`.
*   **Mermaid Decoding:** Ensure Mermaid diagrams in docs decode HTML entities for correct syntax rendering.

## 5. Gemini CLI Instructions
*   **Maintain Multi-Version Sync:** When updating core content (e.g., `ui.ts` or blog posts), ensure all design versions reflect the changes correctly.
*   **Data-Driven Iteration:** When working on V4 telemetry, ensure logic changes are reflected in the Python ETL and the Chart.js visualizers.
*   **Surgical Refactoring:** Use the version-specific directories to avoid cross-version visual regressions.
