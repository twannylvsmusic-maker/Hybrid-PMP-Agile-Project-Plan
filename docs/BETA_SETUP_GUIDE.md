# 🚀 Beta Setup Guide - Hybrid PMP + Agile Project Management

## 📋 Overview
This guide will help you set up and configure the enhanced Hybrid Project Management system for beta testing.

## 🎯 What's New in Beta Version

### ✨ Enhanced Features
- **Advanced Automation**: Robust error handling, email notifications, trend analysis
- **Power BI Analytics**: 12+ new DAX measures, advanced dashboards, predictive analytics
- **Excel Improvements**: 20+ new formulas, data validation, conditional formatting
- **Testing Framework**: Comprehensive test suite with mock data generation
- **Configuration Management**: JSON-based config with validation

### 🔧 Technical Improvements
- **Error Handling**: Comprehensive logging and email notifications
- **Data Validation**: Quality checks and anomaly detection
- **Performance**: Optimized processing for large datasets
- **Security**: Enhanced file handling and backup systems

## 📦 Prerequisites

### System Requirements
- **Windows 10/11** or **macOS 10.15+** or **Linux Ubuntu 18.04+**
- **Python 3.8+** with pip
- **Excel 2016+** or **Office 365**
- **Power BI Desktop** (latest version)
- **Git** (for version control)

### Software Dependencies
```bash
# Python packages
pandas>=1.5.0
openpyxl>=3.0.0
python-dateutil>=2.8.0

# Optional for email notifications
secure-smtplib>=0.1.0
```

## 🛠️ Installation Steps

### Step 1: Download and Extract
```bash
# Clone or download the project
git clone <repository-url>
cd Hybrid_ProjectPlan_Package_plus_Automation_BI

# Or extract from ZIP file
unzip Hybrid_ProjectPlan_Package_plus_Automation_BI.zip
```

### Step 2: Python Environment Setup
```bash
# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r automation/requirements.txt
```

### Step 3: Configuration Setup
```bash
# Navigate to automation directory
cd automation

# Run the script once to generate default config
python update_weekly.py

# Edit the generated config.json file
notepad config.json  # Windows
nano config.json     # macOS/Linux
```

### Step 4: Test Installation
```bash
# Run the test suite
python ../testing/test_automation.py --verbose

# Generate sample data for testing
python ../testing/test_data_generator.py --weeks 8
```

## ⚙️ Configuration Guide

### Basic Configuration
Edit `automation/config.json`:

```json
{
  "EXCEL_PATH": "../Hybrid_ProjectPlan_Template.xlsx",
  "WEEKLY_SHEET": "Weekly_Updates",
  "CSV_FOLDER": "./weekly_csvs",
  "START_ROW": 4,
  "BACKUP_ON_SAVE": true,
  "LOG_LEVEL": "INFO",
  "LOG_FILE": "weekly_update.log"
}
```

### Email Notifications (Optional)
```json
{
  "EMAIL_NOTIFICATIONS": {
    "ENABLED": true,
    "SMTP_SERVER": "smtp.gmail.com",
    "SMTP_PORT": 587,
    "EMAIL": "your.email@company.com",
    "PASSWORD": "your_app_password",
    "TO_EMAILS": ["manager@company.com", "team@company.com"]
  }
}
```

### Data Validation Settings
```json
{
  "DATA_VALIDATION": {
    "MIN_CSAT": 0,
    "MAX_CSAT": 10,
    "MIN_NPS": -100,
    "MAX_NPS": 100,
    "MAX_TICKETS": 10000
  }
}
```

## 📊 Power BI Setup

### Step 1: Install Power BI Desktop
- Download from [Microsoft Power BI](https://powerbi.microsoft.com/desktop/)
- Install and launch Power BI Desktop

### Step 2: Import Data Sources
1. **Weekly Updates (CSV Folder)**:
   - Get Data → Folder → Select `automation/weekly_csvs/`
   - Use the M code from `powerbi/Queries_M_Code.txt`

2. **Excel Template**:
   - Get Data → Excel → Select `Hybrid_ProjectPlan_Template.xlsx`
   - Import sheets: WBS_TaskPlan, Risk_Issue_Log, Project_Overview

### Step 3: Create Enhanced Calendar Table
```dax
Calendar = 
ADDCOLUMNS(
    CALENDAR(DATE(2024,1,1), DATE(2030,12,31)),
    "Year", YEAR([Date]),
    "Quarter", "Q" & QUARTER([Date]),
    "Month", FORMAT([Date], "YYYY-MM"),
    "Month Name", FORMAT([Date], "MMMM"),
    "Week Number", WEEKNUM([Date]),
    "Weekday", FORMAT([Date], "dddd"),
    "Is Weekend", IF(WEEKDAY([Date]) IN {1,7}, "Weekend", "Weekday"),
    "Fiscal Year", IF(MONTH([Date]) >= 4, YEAR([Date]), YEAR([Date]) - 1),
    "Days Since Start", DATEDIFF(DATE(2024,1,1), [Date], DAY)
)
```

### Step 4: Add Enhanced DAX Measures
Copy all measures from `powerbi/DAX_Measures.txt` into your Power BI model.

### Step 5: Create Dashboards
Follow the dashboard layouts in `powerbi/Advanced_PowerBI_Guide.md`.

## 📋 Excel Template Setup

### Step 1: Enable Macros (Optional)
1. Open Excel → File → Options → Trust Center → Trust Center Settings
2. Macro Settings → Enable all macros
3. Import `Weekly_Updates_Import.bas` if using VBA automation

### Step 2: Apply Enhanced Formulas
1. Open `Hybrid_ProjectPlan_Template.xlsx`
2. Apply formulas from `excel_enhancements/Excel_Formulas_Guide.md`
3. Set up conditional formatting rules
4. Configure data validation

### Step 3: Test Template
1. Enter sample data in each sheet
2. Verify formulas calculate correctly
3. Test automation features

## 🔄 Automation Setup

### Windows Task Scheduler
1. Open Task Scheduler
2. Create Task → Name: "Weekly Project Update"
3. Triggers → Weekly on Friday 5:00 PM
4. Actions → Start program: `python`
5. Add arguments: `update_weekly.py`
6. Start in: Full path to automation directory

### macOS/Linux Cron
```bash
# Edit crontab
crontab -e

# Add weekly task
0 17 * * FRI cd /path/to/automation && python update_weekly.py
```

### Manual Testing
```bash
# Test with sample data
cd automation
python update_weekly.py

# Check logs
tail -f weekly_update.log
```

## 🧪 Testing Your Setup

### Run Test Suite
```bash
cd testing
python test_automation.py --verbose
```

### Generate Test Data
```bash
python test_data_generator.py --weeks 12 --output test_data/
```

### Verify Power BI
1. Refresh data sources
2. Check for errors in queries
3. Verify measures calculate correctly
4. Test dashboard interactions

## 🚨 Troubleshooting

### Common Issues

#### Python Import Errors
```bash
# Ensure you're in the right directory
cd automation
python -c "import update_weekly; print('Import successful')"
```

#### Excel File Not Found
- Check file paths in config.json
- Ensure Excel file exists and is not open
- Verify file permissions

#### Power BI Connection Errors
- Check file paths in Power Query
- Ensure CSV files are in correct format
- Verify Excel file is not corrupted

#### Email Notifications Not Working
- Check SMTP settings in config.json
- Use app passwords for Gmail
- Verify firewall settings

### Log Files
- **Automation logs**: `automation/weekly_update.log`
- **Power BI logs**: Check Power BI Desktop → File → Options → Diagnostics
- **Excel errors**: Check Excel status bar for formula errors

### Performance Issues
- **Large datasets**: Use incremental refresh in Power BI
- **Slow Excel**: Optimize formulas, limit volatile functions
- **Memory issues**: Increase Python memory limits

## 📈 Beta Testing Guidelines

### What to Test
1. **Automation Scripts**: Weekly data processing
2. **Power BI Dashboards**: Data refresh and visualization
3. **Excel Formulas**: Calculation accuracy
4. **Error Handling**: System behavior under failure conditions
5. **Performance**: Processing time with large datasets

### Feedback Areas
1. **User Experience**: Ease of setup and use
2. **Functionality**: Feature completeness
3. **Performance**: Speed and reliability
4. **Documentation**: Clarity and completeness
5. **Bug Reports**: Issues and unexpected behavior

### Reporting Issues
1. **Bug Reports**: Include error messages, logs, and steps to reproduce
2. **Feature Requests**: Describe desired functionality
3. **Performance Issues**: Include system specs and data volumes
4. **Documentation**: Suggest improvements

## 🔄 Updates and Maintenance

### Regular Maintenance
- **Weekly**: Review logs and performance
- **Monthly**: Update dependencies and security patches
- **Quarterly**: Review and optimize configurations

### Backup Strategy
- **Automated**: Excel backups created automatically
- **Manual**: Regular backup of configuration and data
- **Version Control**: Track changes to templates and scripts

### Monitoring
- **Log Monitoring**: Watch for errors and performance issues
- **Data Quality**: Regular validation of input data
- **System Health**: Monitor disk space and system resources

## 📞 Support and Resources

### Documentation
- `docs/BETA_SETUP_GUIDE.md` - This guide
- `powerbi/Advanced_PowerBI_Guide.md` - Power BI setup
- `excel_enhancements/Excel_Formulas_Guide.md` - Excel formulas
- `testing/` - Testing and validation tools

### Community Resources
- **GitHub Issues**: Report bugs and request features
- **Documentation Wiki**: Community-maintained guides
- **User Forums**: Connect with other users

### Professional Support
- **Setup Assistance**: Help with initial configuration
- **Custom Development**: Tailored enhancements
- **Training**: User training and best practices

---

## 🎉 Welcome to Beta Testing!

You're now ready to start beta testing the enhanced Hybrid Project Management system. Remember to:

1. **Start Small**: Begin with a pilot project
2. **Test Thoroughly**: Use the provided test data and scripts
3. **Document Issues**: Keep detailed records of any problems
4. **Provide Feedback**: Share your experience and suggestions
5. **Stay Updated**: Check for updates and improvements

**Happy Project Managing!** 🚀

---

**Version**: Beta 2.0  
**Last Updated**: 2025-01-11  
**Compatibility**: Windows 10+, macOS 10.15+, Linux Ubuntu 18.04+
