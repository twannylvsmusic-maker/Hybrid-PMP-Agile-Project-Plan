# 🚀 MS Project Integration Setup Guide

## Welcome to MS Project Integration!

This guide will walk you through setting up the MS Project integration module for your Hybrid PMP + Agile Project Management System.

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Excel Gantt Chart Setup](#excel-gantt-chart-setup)
5. [MS Project XML Import](#ms-project-xml-import)
6. [MS Project XML Export](#ms-project-xml-export)
7. [Power BI Integration](#power-bi-integration)
8. [Automation](#automation)
9. [Troubleshooting](#troubleshooting)

---

## ✅ Prerequisites

### Required Software:
- **Python 3.8+** (for automation scripts)
- **Microsoft Excel** (2016 or later recommended)
- **Power BI Desktop** (latest version)

### Optional Software:
- **Microsoft Project** (for XML file generation - 2010 or later)
- **Git** (for version control)

### Python Packages:
```bash
pip install openpyxl pandas python-dateutil lxml
```

Or install from requirements file:
```bash
pip install -r ms_project_integration/requirements.txt
```

---

## 📦 Installation

### Step 1: Verify Python Installation
```bash
python --version
```
Should show Python 3.8 or higher.

### Step 2: Install Dependencies
```bash
cd ms_project_integration
pip install -r requirements.txt
```

### Step 3: Verify Installation
```bash
python scripts/ms_project_importer.py --help
python scripts/ms_project_exporter.py --help
python scripts/gantt_calculator.py --help
```

All commands should display help text without errors.

### Step 4: Create Required Directories
```bash
mkdir -p imports
mkdir -p exports
mkdir -p logs
mkdir -p temp
```

---

## ⚙️ Configuration

### Edit Configuration File

Open `scripts/config_msproject.json` and customize:

```json
{
  "paths": {
    "excel_template": "../templates/Gantt_Chart_Template.xlsx",
    "default_import_path": "./imports/",
    "default_export_path": "./exports/",
    "temp_directory": "./temp/"
  },
  "gantt_settings": {
    "start_column": "H",
    "timeline_weeks": 26,
    "timeline_mode": "weeks",
    "weekend_shading": true,
    "today_marker": true,
    "show_dependencies": true,
    "critical_path_highlight": true
  },
  "working_days": {
    "monday": true,
    "tuesday": true,
    "wednesday": true,
    "thursday": true,
    "friday": true,
    "saturday": false,
    "sunday": false
  }
}
```

### Key Settings to Adjust:

1. **excel_template**: Path to your Gantt chart template
2. **timeline_weeks**: Number of weeks to display (default: 26 = 6 months)
3. **working_days**: Adjust for your team's work schedule
4. **status_colors**: Customize visual appearance

---

## 📊 Excel Gantt Chart Setup

### Create Your Gantt Chart Template

Follow the instructions in:
- `templates/GANTT_TEMPLATE_INSTRUCTIONS.md`

### Quick Setup Steps:

1. **Open Excel** and create new workbook
2. **Add columns** as specified in instructions:
   - Task ID, Task Name, Duration, Start Date, Finish Date
   - Progress, Status, Dependencies, Assigned To, Priority
3. **Add timeline columns** starting from column M
4. **Set up conditional formatting** for Gantt bars
5. **Add sample data** to test
6. **Save as** `Gantt_Chart_Template.xlsx`

### Template Location:
Place the template in:
```
ms_project_integration/templates/Gantt_Chart_Template.xlsx
```

---

## 📥 MS Project XML Import

### Export from MS Project

1. Open your project in MS Project
2. File → Save As
3. Choose location
4. File type: **XML Format (*.xml)**
5. Save the file

### Import to Excel Gantt Chart

```bash
python scripts/ms_project_importer.py --input path/to/your_project.xml
```

**Options:**
```bash
python scripts/ms_project_importer.py --input project.xml --output custom_output.xlsx
```

### What Gets Imported:
- ✅ Task names and IDs
- ✅ Start and finish dates
- ✅ Duration (converted to days)
- ✅ Progress/percent complete
- ✅ Priority levels
- ✅ Resource assignments
- ✅ Dependencies (predecessors)
- ✅ Notes
- ✅ Milestone markers
- ✅ Critical path indicators

### Import Output:
- Excel file saved to `imports/` folder
- Log file created in `logs/` folder
- Console output shows import summary

---

## 📤 MS Project XML Export

### Export from Excel to MS Project XML

```bash
python scripts/ms_project_exporter.py --input Gantt_Chart_Template.xlsx
```

**Options:**
```bash
python scripts/ms_project_exporter.py --input my_gantt.xlsx --output my_project.xml --sheet "Gantt Chart"
```

### What Gets Exported:
- ✅ All tasks with metadata
- ✅ Dates and duration
- ✅ Progress tracking
- ✅ Priority levels
- ✅ Dependencies
- ✅ Notes and descriptions
- ✅ MS Project-compatible XML format

### Opening in MS Project:
1. Open Microsoft Project
2. File → Open
3. Select the exported XML file
4. File will load with all tasks and dependencies

---

## 📊 Power BI Integration

### Step 1: Load Gantt Data into Power BI

1. Open Power BI Desktop
2. **Get Data** → Excel
3. Select `Gantt_Chart_Template.xlsx`
4. Choose **Gantt Chart** sheet
5. Click **Load**

### Step 2: Add DAX Measures

1. Click on **Modeling** tab
2. Select **New Measure**
3. Copy DAX formulas from `powerbi/Gantt_DAX_Measures.txt`
4. Create each measure one by one

**Key Measures to Add:**
- Overall Project Progress
- Critical Tasks Count
- Tasks Completion Rate
- Schedule Performance Index
- Days Until Completion

### Step 3: Apply Power Query Transformations

1. **Transform Data** → Advanced Editor
2. Copy relevant queries from `powerbi/Timeline_Queries.txt`
3. Apply transformations
4. Close & Apply

### Step 4: Create Visualizations

**Recommended Visuals:**

1. **Gantt Chart Visual** (use custom visual from marketplace)
   - X-axis: Timeline dates
   - Y-axis: Task names
   - Values: Start date, Finish date, Progress

2. **Project Timeline Card**
   - Display: Project Start Date, End Date, Duration

3. **Task Status Breakdown** (Donut chart)
   - Values: Task count by Status

4. **Critical Path Table**
   - Filter: Critical Path = "Yes"
   - Show: Task Name, Progress, Finish Date

5. **Resource Allocation** (Bar chart)
   - X-axis: Assigned To
   - Y-axis: Total Duration (Days)

### Step 5: Create Dashboard Pages

Create the following pages:

1. **Overview Dashboard**
   - Project metrics cards
   - Gantt chart visual
   - Status breakdown

2. **Critical Path Analysis**
   - Critical tasks table
   - Critical path timeline
   - Risk indicators

3. **Resource Management**
   - Resource allocation chart
   - Workload distribution
   - Utilization metrics

4. **Milestone Tracker**
   - Milestone timeline
   - Completion status
   - Upcoming milestones

---

## 🤖 Automation

### Timeline Calculations

Recalculate dates based on dependencies:

```bash
python scripts/gantt_calculator.py --input Gantt_Chart_Template.xlsx --recalculate
```

This will:
- Update start/finish dates based on dependencies
- Calculate critical path
- Identify slack time
- Mark critical tasks

### Scheduling Regular Updates

**Windows (Task Scheduler):**
1. Open Task Scheduler
2. Create New Task
3. Trigger: Weekly (e.g., every Monday)
4. Action: Run Python script
   ```
   python C:\path\to\gantt_calculator.py --input C:\path\to\Gantt_Chart_Template.xlsx --recalculate
   ```

**macOS/Linux (cron):**
```bash
# Edit crontab
crontab -e

# Add weekly calculation (every Monday at 9 AM)
0 9 * * 1 cd /path/to/ms_project_integration && python scripts/gantt_calculator.py --input templates/Gantt_Chart_Template.xlsx --recalculate
```

### Batch Processing

Process multiple projects:

```bash
# Import multiple MS Project files
for file in imports/*.xml; do
    python scripts/ms_project_importer.py --input "$file"
done
```

---

## 🆘 Troubleshooting

### Common Issues and Solutions

#### Issue: "Module not found" error
**Solution:**
```bash
pip install --upgrade openpyxl pandas lxml python-dateutil
```

#### Issue: XML import fails
**Cause:** MS Project XML version incompatibility  
**Solution:** 
- Export from MS Project as XML 2010+ format
- Check XML structure is valid
- Review error log in `logs/` folder

#### Issue: Dates calculating incorrectly
**Cause:** Working days configuration  
**Solution:** 
- Check `working_days` in `config_msproject.json`
- Ensure weekend days are set to `false`

#### Issue: Gantt chart not displaying in Excel
**Cause:** Conditional formatting not applied  
**Solution:**
- Re-apply conditional formatting rules
- Check that timeline columns are properly configured
- Verify date formats are consistent

#### Issue: Power BI not loading data
**Cause:** File path or sheet name incorrect  
**Solution:**
- Update file path in Power Query
- Verify sheet name is "Gantt Chart"
- Refresh data source

#### Issue: Critical path not identifying correctly
**Cause:** Dependencies not properly formatted  
**Solution:**
- Use standard dependency format: "2FS", "3SS", etc.
- Ensure Task IDs are sequential
- Run gantt_calculator.py to recalculate

---

## 📝 Best Practices

1. **Regular Updates**: Update progress weekly
2. **Dependency Tracking**: Always link related tasks
3. **Critical Path Focus**: Monitor critical tasks closely
4. **Resource Balance**: Avoid overallocation
5. **Milestone Markers**: Use 0-duration tasks for milestones
6. **Backup**: Save versions before major changes
7. **Documentation**: Keep notes on task changes

---

## 🎯 Next Steps

After setup is complete:

1. ✅ Create your first Gantt chart
2. ✅ Import existing MS Project file (if applicable)
3. ✅ Set up Power BI dashboard
4. ✅ Configure automation
5. ✅ Review user guides for daily operations

### Additional Resources:

- **User Guide**: `docs/GANTT_CHART_USER_GUIDE.md`
- **Power BI Guide**: `docs/POWERBI_TIMELINE_GUIDE.md`
- **Template Instructions**: `templates/GANTT_TEMPLATE_INSTRUCTIONS.md`

---

## 🤝 Support

For issues or questions:
- Check troubleshooting section above
- Review log files in `logs/` directory
- Consult main project documentation

---

**You're all set! Start managing your projects with hybrid MS Project integration.** 🚀

