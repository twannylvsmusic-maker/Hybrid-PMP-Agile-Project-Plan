# Scheduling the Weekly Automation

## Windows Task Scheduler
1. Open **Task Scheduler** → *Create Task...*
2. **Triggers** → *New...* → Weekly on Friday 5:00 PM.
3. **Actions** → *New...* → Program/script: `python`
   - **Add arguments**: `update_weekly.py`
   - **Start in**: full path to `.../Hybrid_ProjectPlan_Package/automation`
4. **Conditions**: Check "Wake the computer..." (optional)
5. **Settings**: Allow task to run on demand.

## macOS / Linux (cron)
1. Run `crontab -e`
2. Add a line to run every Friday at 5:00 PM:
   ```
   0 17 * * FRI cd /path/to/Hybrid_ProjectPlan_Package/automation && /usr/bin/python3 update_weekly.py
   ```

## Notes
- Ensure `pip install openpyxl pandas` before first run.
- Place weekly CSV files into `automation/weekly_csvs/`.
- The script writes into `Hybrid_ProjectPlan_Template.xlsx` → **Weekly_Updates** sheet, triggering KPI updates.