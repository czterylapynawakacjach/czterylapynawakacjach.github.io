# Pet Hotel Website - Project Context

## 1. Project Overview & Goal
Build a modern, static, multilingual website for a dog/cat boarding hotel. This project has evolved into a **Design Portfolio** showcasing three distinct creative directions (v1, v2, v3) to allow the owner to choose their preferred brand identity.

## 2. Technical Stack
*   **Framework:** Astro (Static Site Generator)
*   **Styling:** Tailwind CSS (Utility-first)
*   **Typography:** Fraunces (Headings), Inter (Body) - via @fontsource
*   **Content:** File-based MDX for the blog and Markdown for supporting documents.
*   **Diagrams:** Mermaid.js (Client-side rendering for technical architecture).
*   **Hosting:** GitHub Pages (via GitHub Actions CI/CD)
*   **Interactivity:** Vanilla JS (Magnetic physics, eye-tracking, cinematic spotlights).
*   **Forms:** Formspree (Form-as-a-service) for contact/booking.

## 3. Site Structure & Features
*   **Root (/)**: Portfolio selection page to choose between Design Versions.
*   **Design Versions**:
    *   **V1 (Clean & Classic)**: Professional, trustworthy blue/white layout.
    *   **V2 (Forest Boutique)**: Luxurious, nature-inspired design with soft serifs and organic elements.
    *   **V3 (Artistic & Brave)**: Experimental broken-grid, cinematic interactions, and unique animal-personality physics.
    *   **V4 (The Golden Apiary)**: Fun, interactive artisanal experience with amber palette, hexagonal grids, and "alive" bee-based interactions.
*   **Supporting Docs**: Individual HTML pages converted from Markdown (Business Plan, Technical Architecture, etc.).
*   **Languages**: Polish (Primary/Default) and English. Managed via version-aware i18n routing.

## 4. Architectural Mandates
*   **100% Static:** The final build must be completely static (npm run build) to be hosted on GitHub Pages.
*   **Version Independence:** Each design version (v1, v2, v3) must remain visually and structurally isolated in its own layouts and components folder.
*   **i18n Routing:** Custom version-aware routing handling paths like `/v3/pl/blog/`.
*   **Mermaid Decoding:** Ensure Mermaid diagrams in docs decode HTML entities for correct syntax rendering (arrows, etc.).

## 5. Gemini CLI Instructions
*   **Maintain Multi-Version Sync:** When updating core content (e.g., `ui.ts` or blog posts), ensure all three design versions reflect the changes correctly.
*   **Brave Design Iteration:** When working on V3, prioritize "alive" and artistic interactions over standard web conventions.
*   **Surgical Refactoring:** Use the version-specific component/layout directories to avoid cross-version visual regressions.
