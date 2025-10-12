HYBRID PMP + AGILE PROJECT PLAN — PACKAGE

Files
-----
1) Hybrid_ProjectPlan_Model.docx          — Narrative model and guidance
2) Hybrid_ProjectPlan_Template.xlsx       — Multi-tab template with formulas (no macros)
3) Hybrid_ProjectPlan_Deck.pptx           — Portfolio-themed summary deck
4) Weekly_Updates_Import.bas              — Optional VBA macro (import weekly CSV)
   
How to Use
----------
1. Open the Excel template and complete the "Project_Overview" and "WBS_TaskPlan" tabs.
2. Use "Sprint_Planner" to prioritize and plan in iterations.
3. Log risks/issues and communications in their respective tabs.
4. Paste your weekly metrics into "Weekly_Updates" (or import via the macro below).
5. Review KPIs on "KPI_Dashboard" and capture deltas in "Gap_Analysis_Feed".

Weekly Email Updates (Option)
-----------------------------
A. Outlook Rule (recommended):
   - Create a rule to automatically save weekly metrics attachments (CSV) from your reporting inbox
     into a folder on your machine, e.g., C:\Project\WeeklyUpdates\
   - Use a consistent CSV with columns: Week Start, Tickets Opened, Tickets Resolved, NPS, CSAT, Notes

B. Importing into Excel:
   - In Excel, press ALT+F11 → File → Import File... → choose Weekly_Updates_Import.bas
   - Back in Excel, add a button (Developer tab) and assign macro: ImportWeeklyUpdates
   - Run macro and select the weekly CSV. KPI_Dashboard will update automatically.

Notes
-----
- This template is macro-free by default for easier sharing. The .bas macro is optional.
- You can also map a Power Query to your updates folder if desired (not included here).
- Targets are placeholders; adjust KPI targets to your PMO standards.

Version
-------
Generated on 2025-10-11