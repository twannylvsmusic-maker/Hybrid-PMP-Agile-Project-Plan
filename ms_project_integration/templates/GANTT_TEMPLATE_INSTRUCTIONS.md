# 📊 Excel Gantt Chart Template Instructions

## Overview
This document provides instructions for creating and using the Excel Gantt Chart template. Since Excel files cannot be created directly, follow these steps to build your Gantt chart.

---

## 🎯 Creating the Gantt Chart Template

### Step 1: Create New Excel Workbook
1. Open Microsoft Excel
2. Create a new blank workbook
3. Save as `Gantt_Chart_Template.xlsx`
4. Rename Sheet1 to `Gantt Chart`

---

### Step 2: Set Up Column Headers (Row 1)

Create the following columns:

| Column | Header Name | Data Type | Description |
|--------|-------------|-----------|-------------|
| A | Task ID | Number | Unique identifier for each task |
| B | Task Name | Text | Description of the task |
| C | Duration (Days) | Number | Task duration in working days |
| D | Start Date | Date | Task start date |
| E | Finish Date | Date | Task completion date |
| F | Progress (%) | Number | Completion percentage (0-100) |
| G | Status | Dropdown | Not Started, In Progress, Completed, Blocked, On Hold |
| H | Dependencies | Text | Task dependencies (e.g., "2FS", "3,4") |
| I | Assigned To | Text | Resource/person assigned |
| J | Priority | Dropdown | High, Medium, Low |
| K | Notes | Text | Additional information |
| L | Critical Path | Text | Yes/No indicator |

---

### Step 3: Create Data Validation (Dropdowns)

#### Status Dropdown (Column G):
1. Select column G (starting from G2)
2. Data → Data Validation → List
3. Source: `Not Started,In Progress,Completed,Blocked,On Hold`

#### Priority Dropdown (Column J):
1. Select column J (starting from J2)
2. Data → Data Validation → List
3. Source: `High,Medium,Low`

---

### Step 4: Add Timeline Columns (Starting from Column M)

Create a timeline header starting in column M:

**Week-based Timeline:**
- M1: Week 1
- N1: Week 2
- O1: Week 3
- etc. (create 26 weeks)

**Or Date-based Timeline:**
- M1: Project start date
- N1: =M1+7 (one week later)
- O1: =N1+7
- Copy formula across

---

### Step 5: Create Gantt Chart Visual (Columns M onward)

For each task row, create conditional formatting to show the Gantt bar:

1. **Formula for each cell in the timeline:**
   ```excel
   =AND($D2<=M$1, $E2>=M$1)
   ```
   - This checks if the task is active during that week

2. **Apply Conditional Formatting:**
   - Select the timeline range (M2:AL100 or larger)
   - Home → Conditional Formatting → New Rule
   - Use a formula to determine which cells to format
   - Formula: `=AND($D2<=M$1, $E2>=M$1, $G2<>"Completed")`
   - Format: Fill color based on status

3. **Color Scheme:**
   - In Progress: Orange (#F59E0B)
   - Not Started: Gray (#9CA3AF)
   - Blocked: Red (#EF4444)
   - On Hold: Purple (#8B5CF6)
   - Completed: Green (#10B981) - lighter shade

---

### Step 6: Add Formulas

#### Auto-calculate Finish Date (if not manually entered):
In column E (Finish Date), use:
```excel
=WORKDAY($D2, $C2)
```
This calculates finish date based on start date and duration, skipping weekends.

#### Progress Bar in Excel:
In a helper column (optional), create a progress bar using REPT function:
```excel
=REPT("█", F2/10) & REPT("▫", (100-F2)/10)
```

---

### Step 7: Format the Timeline Area

1. **Weekend Shading:**
   - Identify weekend columns
   - Apply light gray background
   - Or use conditional formatting based on date

2. **Today Marker:**
   - Create conditional formatting for the current week/date
   - Format: Bold border or different background color

3. **Grid Lines:**
   - Apply all borders to the timeline area
   - Format → Cell → Border → All

---

### Step 8: Add Sample Data

Create sample tasks to test the template:

| Task ID | Task Name | Duration | Start Date | Finish Date | Progress | Status | Dependencies | Assigned To | Priority |
|---------|-----------|----------|------------|-------------|----------|--------|--------------|-------------|----------|
| 1 | Project Kickoff | 0 | 2024-10-20 | 2024-10-20 | 100 | Completed | - | PM Team | High |
| 2 | Requirements Gathering | 5 | 2024-10-21 | 2024-10-27 | 100 | Completed | 1FS | BA Team | High |
| 3 | Design Phase | 10 | 2024-10-28 | 2024-11-10 | 60 | In Progress | 2FS | Design Team | High |
| 4 | Development Sprint 1 | 14 | 2024-11-11 | 2024-11-30 | 0 | Not Started | 3FS | Dev Team | High |
| 5 | Testing Phase | 7 | 2024-12-01 | 2024-12-10 | 0 | Not Started | 4FS | QA Team | Medium |

---

### Step 9: Add Helper Formulas (Optional)

Create a summary section above or beside the main table:

```
Project Metrics:
- Total Tasks: =COUNTA(A2:A100)-COUNTBLANK(A2:A100)
- Completed: =COUNTIF(G2:G100,"Completed")
- In Progress: =COUNTIF(G2:G100,"In Progress")
- Overall Progress: =AVERAGE(F2:F100)
- Project Start: =MIN(D2:D100)
- Project End: =MAX(E2:E100)
```

---

### Step 10: Protect and Save

1. **Protect Formula Cells:**
   - Select cells with formulas
   - Format Cells → Protection → Locked
   - Review → Protect Sheet

2. **Save Template:**
   - Save as `Gantt_Chart_Template.xlsx`
   - Place in `ms_project_integration/templates/` folder

---

## 🚀 Using the Template

### Adding New Tasks:
1. Insert new row
2. Enter Task ID, Name, Duration, Start Date
3. Select Status and Priority from dropdowns
4. Enter Dependencies if applicable
5. Assign resources
6. Gantt chart will auto-update based on conditional formatting

### Updating Progress:
1. Update Progress (%) column
2. Change Status dropdown as needed
3. Colors will auto-update based on status

### Tracking Dependencies:
**Dependency Format:**
- `2FS` = Task depends on Task 2, Finish-to-Start
- `3SS` = Task depends on Task 3, Start-to-Start
- `4FF` = Task depends on Task 4, Finish-to-Finish
- `5SF` = Task depends on Task 5, Start-to-Finish
- `2,3` = Task depends on Tasks 2 and 3 (both must complete)

---

## 📊 Power BI Integration

Once template is created:
1. Open Power BI Desktop
2. Get Data → Excel
3. Select `Gantt_Chart_Template.xlsx`
4. Choose `Gantt Chart` sheet
5. Load data into Power BI
6. Use DAX measures from `Gantt_DAX_Measures.txt`
7. Apply M-Code queries from `Timeline_Queries.txt`

---

## 🔄 MS Project Integration

### Import from MS Project:
```bash
python ms_project_importer.py --input your_project.xml
```

### Export to MS Project:
```bash
python ms_project_exporter.py --input Gantt_Chart_Template.xlsx
```

---

## 💡 Tips for Best Results

1. **Keep it Simple:** Start with 10-20 tasks, expand as needed
2. **Update Weekly:** Refresh progress every week
3. **Use Dependencies:** Link related tasks for auto-scheduling
4. **Color Code:** Use status colors consistently
5. **Milestone Markers:** Set duration to 0 for milestones
6. **Critical Path:** Mark critical tasks for visibility
7. **Resource Balance:** Avoid overallocating team members

---

## 🆘 Troubleshooting

**Issue:** Gantt bars not showing  
**Solution:** Check conditional formatting rules are applied correctly

**Issue:** Dates calculating incorrectly  
**Solution:** Ensure WORKDAY formula is used and regional settings are correct

**Issue:** Timeline columns not wide enough  
**Solution:** Adjust column width to fit week/date labels

---

*For more help, see the full MS Project Integration documentation.*

