# 📖 User Manual - Hybrid PMP + Agile Project Management

## 🎯 Introduction

Welcome to the Hybrid PMP + Agile Project Management system! This comprehensive solution combines traditional PMP methodologies with Agile practices, enhanced with automation and Business Intelligence capabilities.

## 📚 Table of Contents

1. [Getting Started](#getting-started)
2. [Core Components](#core-components)
3. [Excel Template Guide](#excel-template-guide)
4. [Power BI Dashboards](#power-bi-dashboards)
5. [Automation Features](#automation-features)
6. [Best Practices](#best-practices)
7. [Troubleshooting](#troubleshooting)
8. [Advanced Features](#advanced-features)

## 🚀 Getting Started

### System Overview
The Hybrid Project Management system consists of:

- **Excel Template**: Multi-sheet project planning and tracking
- **Power BI Dashboards**: Advanced analytics and visualization
- **Automation Scripts**: Weekly data processing and updates
- **Testing Framework**: Validation and quality assurance

### Quick Start Checklist
- [ ] Set up Python environment and dependencies
- [ ] Configure automation settings
- [ ] Import Excel template
- [ ] Install and configure Power BI
- [ ] Run initial data import
- [ ] Test automation scripts
- [ ] Create first project plan

## 🏗️ Core Components

### 1. Project Overview Sheet
**Purpose**: High-level project information and status

**Key Fields**:
- Project Name and Manager
- Start/End Dates and Budget
- Current Status and Health Score
- Key Stakeholders

**Best Practices**:
- Update weekly with current status
- Maintain accurate budget tracking
- Document major milestones

### 2. WBS Task Plan Sheet
**Purpose**: Detailed work breakdown structure

**Key Fields**:
- Task ID and Description
- Owner and Dependencies
- Planned vs Actual Dates
- Completion Percentage
- RAG Status (Red/Amber/Green)

**Best Practices**:
- Keep tasks granular (1-5 days)
- Update progress weekly
- Maintain dependency relationships
- Use consistent naming conventions

### 3. Sprint Planner Sheet
**Purpose**: Agile sprint planning and tracking

**Key Fields**:
- Sprint Number and Stories
- Story Points and Status
- Actual Effort Tracking
- Velocity Metrics

**Best Practices**:
- Plan 1-2 week sprints
- Estimate story points consistently
- Track actual effort for accuracy
- Review velocity trends

### 4. Risk/Issue Log Sheet
**Purpose**: Risk and issue management

**Key Fields**:
- Risk/Issue ID and Type
- Description and Owner
- Probability and Impact
- Mitigation Actions
- Status Tracking

**Best Practices**:
- Review weekly in team meetings
- Escalate high-risk items
- Document mitigation actions
- Close resolved items promptly

### 5. Weekly Updates Sheet
**Purpose**: Weekly performance metrics

**Key Fields**:
- Week Start Date
- Tickets Opened/Resolved
- CSAT and NPS Scores
- Notes and Observations

**Best Practices**:
- Update every Friday
- Maintain consistent metrics
- Document notable events
- Track trends over time

### 6. KPI Dashboard Sheet
**Purpose**: Key performance indicators

**Key Metrics**:
- Project Health Score
- CSAT Trends
- Risk Counts
- Progress Percentage

**Best Practices**:
- Review weekly with stakeholders
- Focus on actionable metrics
- Track trends over time
- Address red indicators promptly

## 📊 Excel Template Guide

### Navigation Tips
- **Sheet Tabs**: Click to switch between sheets
- **Data Entry**: Start from row 2 (row 1 contains headers)
- **Formulas**: Protected cells with formulas are read-only
- **Validation**: Dropdown lists ensure consistent data entry

### Data Entry Guidelines

#### Project Overview
1. Enter basic project information
2. Set realistic start/end dates
3. Define budget constraints
4. Assign project manager

#### WBS Task Planning
1. Break down project into tasks
2. Assign owners and dependencies
3. Estimate durations
4. Set milestone dates

#### Risk Management
1. Identify potential risks early
2. Assess probability and impact
3. Assign owners and actions
4. Review and update regularly

#### Weekly Updates
1. Collect metrics from your systems
2. Enter data consistently
3. Add context in notes
4. Review trends

### Formula Usage
The template includes many automated formulas:

- **RAG Status**: Automatically calculated based on completion percentage
- **Trend Analysis**: Compares current vs previous periods
- **Risk Scores**: Calculated from probability × impact
- **KPI Calculations**: Aggregated from various data sources

### Conditional Formatting
Color coding helps identify issues:

- **Green**: On track, good performance
- **Amber**: At risk, needs attention
- **Red**: Off track, requires immediate action

## 📈 Power BI Dashboards

### Dashboard Overview
Three main dashboards provide different perspectives:

1. **Executive Dashboard**: High-level metrics for leadership
2. **Operational Dashboard**: Detailed metrics for teams
3. **Risk Management Dashboard**: Focused on risk tracking

### Key Visualizations

#### Executive Dashboard
- **KPI Cards**: Project health, CSAT, risks, progress
- **Trend Charts**: Performance over time
- **Status Indicators**: Color-coded health metrics

#### Operational Dashboard
- **Performance Metrics**: Resolution efficiency, velocity
- **Quality Indicators**: CSAT trends, NPS analysis
- **Resource Utilization**: Team workload and capacity

#### Risk Management Dashboard
- **Risk Overview**: Counts and distributions
- **Issue Tracking**: Active issues and resolutions
- **Trend Analysis**: Risk patterns over time

### Interactive Features
- **Slicers**: Filter data by date, team, or project
- **Drill-through**: Click to see detailed information
- **Tooltips**: Hover for additional context
- **Bookmarks**: Save specific views for reporting

### Data Refresh
- **Automatic**: Daily refresh for CSV data
- **Manual**: Excel data refreshed on demand
- **Scheduled**: Weekly refresh for comprehensive updates

## 🤖 Automation Features

### Weekly Data Processing
The automation system:

1. **Reads CSV files** from the weekly_csvs folder
2. **Validates data quality** and reports issues
3. **Updates Excel template** with new data
4. **Sends notifications** on completion or errors
5. **Creates backups** before making changes

### Configuration Options
Customize automation behavior:

- **File paths**: Specify Excel and CSV locations
- **Validation rules**: Set acceptable data ranges
- **Email notifications**: Configure alerts and reports
- **Backup settings**: Control backup frequency

### Scheduling
Set up automated execution:

- **Windows**: Task Scheduler for weekly runs
- **macOS/Linux**: Cron jobs for scheduled execution
- **Manual**: Run scripts on demand for testing

### Error Handling
Robust error management:

- **Logging**: Detailed logs for troubleshooting
- **Validation**: Data quality checks before processing
- **Notifications**: Email alerts for issues
- **Recovery**: Automatic retry and backup restoration

## 💡 Best Practices

### Project Planning
1. **Start with Project Overview**: Define scope and constraints
2. **Create Detailed WBS**: Break down into manageable tasks
3. **Identify Dependencies**: Map task relationships
4. **Assign Owners**: Ensure accountability
5. **Set Milestones**: Define key checkpoints

### Agile Integration
1. **Plan Sprints**: Use 1-2 week iterations
2. **Estimate Consistently**: Use story points or hours
3. **Track Velocity**: Monitor team performance
4. **Review Regularly**: Conduct sprint retrospectives
5. **Adapt Plans**: Adjust based on learnings

### Risk Management
1. **Identify Early**: Conduct risk assessment sessions
2. **Assess Objectively**: Use probability and impact scales
3. **Plan Mitigation**: Define specific actions
4. **Monitor Continuously**: Review weekly
5. **Communicate**: Share status with stakeholders

### Data Quality
1. **Enter Consistently**: Use standardized formats
2. **Validate Input**: Check data ranges and formats
3. **Update Regularly**: Maintain current information
4. **Document Changes**: Track modifications
5. **Review Trends**: Analyze patterns over time

### Team Collaboration
1. **Assign Roles**: Define responsibilities clearly
2. **Communicate Regularly**: Hold weekly status meetings
3. **Share Information**: Use centralized dashboards
4. **Document Decisions**: Record important choices
5. **Learn Continuously**: Improve processes based on experience

## 🔧 Troubleshooting

### Common Issues

#### Excel Problems
**Issue**: Formulas not calculating
- **Solution**: Check for circular references, verify data types

**Issue**: Conditional formatting not working
- **Solution**: Ensure formulas reference correct cells

**Issue**: Data validation errors
- **Solution**: Check dropdown lists and input ranges

#### Power BI Problems
**Issue**: Data not refreshing
- **Solution**: Check file paths, verify data sources

**Issue**: Measures showing errors
- **Solution**: Review DAX syntax, check relationships

**Issue**: Visualizations not displaying
- **Solution**: Verify data types, check for null values

#### Automation Problems
**Issue**: Script fails to run
- **Solution**: Check Python installation, verify dependencies

**Issue**: CSV files not processed
- **Solution**: Verify file format, check column headers

**Issue**: Email notifications not sent
- **Solution**: Check SMTP settings, verify credentials

### Getting Help
1. **Check Logs**: Review automation and system logs
2. **Verify Configuration**: Ensure settings are correct
3. **Test with Sample Data**: Use provided test data
4. **Document Issues**: Record error messages and steps
5. **Contact Support**: Reach out for assistance

## 🚀 Advanced Features

### Custom Dashboards
Create specialized dashboards for:
- **Team Performance**: Individual contributor metrics
- **Quality Assurance**: Testing and defect tracking
- **Resource Planning**: Capacity and utilization
- **Financial Tracking**: Budget and cost analysis

### Integration Options
Connect with external systems:
- **JIRA**: Import issue and project data
- **ServiceNow**: Sync incident and change data
- **SharePoint**: Collaborate on documents
- **Teams**: Share reports and updates

### Advanced Analytics
Leverage additional capabilities:
- **Predictive Analytics**: Forecast trends and outcomes
- **Anomaly Detection**: Identify unusual patterns
- **Correlation Analysis**: Find relationships between metrics
- **Scenario Planning**: Model different outcomes

### Customization
Tailor the system to your needs:
- **Additional Metrics**: Define custom KPIs
- **Modified Dashboards**: Adjust visualizations
- **Extended Automation**: Add new processing steps
- **Integration Scripts**: Connect with other tools

## 📞 Support and Resources

### Documentation
- **Setup Guide**: Initial installation and configuration
- **Power BI Guide**: Dashboard creation and management
- **Excel Formulas**: Advanced formula usage
- **API Reference**: Automation script documentation

### Training Resources
- **Video Tutorials**: Step-by-step demonstrations
- **Webinars**: Live training sessions
- **User Guides**: Detailed feature documentation
- **Best Practices**: Recommended approaches

### Community
- **User Forums**: Connect with other users
- **Knowledge Base**: Searchable help articles
- **Feature Requests**: Suggest improvements
- **Bug Reports**: Report issues and problems

### Professional Services
- **Consulting**: Custom implementation support
- **Training**: On-site user training
- **Development**: Custom feature development
- **Support**: Ongoing technical assistance

---

## 🎉 Conclusion

The Hybrid PMP + Agile Project Management system provides a comprehensive solution for modern project management. By combining traditional PMP methodologies with Agile practices and enhanced with automation and analytics, it helps teams deliver projects more effectively.

Remember:
- **Start Simple**: Begin with basic features and expand
- **Stay Consistent**: Maintain regular updates and reviews
- **Learn Continuously**: Adapt and improve your processes
- **Collaborate Effectively**: Use the system to enhance team communication
- **Measure Success**: Track metrics that matter to your organization

**Happy Project Managing!** 🚀

---

**Version**: 2.0  
**Last Updated**: 2025-01-11  
**For Support**: Contact your system administrator or refer to the documentation wiki
