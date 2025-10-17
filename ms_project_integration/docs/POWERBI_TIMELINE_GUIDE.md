# 📊 Power BI Timeline & Gantt Dashboard Guide

## Complete Guide to Building Power BI Dashboards for MS Project Integration

---

## 📋 Table of Contents

1. [Dashboard Overview](#dashboard-overview)
2. [Data Source Setup](#data-source-setup)
3. [Page 1: Executive Timeline](#page-1-executive-timeline)
4. [Page 2: Gantt Chart View](#page-2-gantt-chart-view)
5. [Page 3: Critical Path Analysis](#page-3-critical-path-analysis)
6. [Page 4: Resource Management](#page-4-resource-management)
7. [Page 5: Milestone Tracker](#page-5-milestone-tracker)
8. [Interactive Features](#interactive-features)
9. [Publishing and Sharing](#publishing-and-sharing)

---

## 🎯 Dashboard Overview

### Purpose
Create interactive, real-time dashboards that visualize:
- Project timeline and progress
- Gantt chart with task dependencies
- Critical path analysis
- Resource allocation and workload
- Milestone tracking and alerts

### Dashboard Structure
**5 Main Pages:**
1. Executive Timeline (High-level overview)
2. Gantt Chart View (Detailed task timeline)
3. Critical Path Analysis (Risk management)
4. Resource Management (Team allocation)
5. Milestone Tracker (Key deliverables)

---

## 🔌 Data Source Setup

### Step 1: Connect to Excel Gantt Chart

1. Open Power BI Desktop
2. **Home** → **Get Data** → **Excel**
3. Navigate to `Gantt_Chart_Template.xlsx`
4. Select **Gantt Chart** sheet
5. Click **Transform Data**

### Step 2: Apply Power Query Transformations

In Power Query Editor, apply transformations from `powerbi/Timeline_Queries.txt`:

#### A. Add Calculated Columns
```m
// Add Task Duration Days
= Table.AddColumn(#"Changed Type", "Task Duration Days", 
  each Duration.Days([Finish Date] - [Start Date]))

// Add Is Milestone
= Table.AddColumn(#"Previous Step", "Is Milestone", 
  each if [Duration (Days)] = 0 then "Yes" else "No")

// Add Is Overdue
= Table.AddColumn(#"Previous Step", "Is Overdue", 
  each if [Finish Date] < Date.From(DateTime.LocalNow()) 
  and [Status] <> "Completed" then "Yes" else "No")

// Add Is Active
= Table.AddColumn(#"Previous Step", "Is Active", 
  each if [Start Date] <= Date.From(DateTime.LocalNow()) 
  and [Finish Date] >= Date.From(DateTime.LocalNow()) 
  and [Status] <> "Completed" then "Yes" else "No")
```

### Step 3: Create Supporting Queries

Create additional queries for:
- Timeline Date Table
- Task Status Summary
- Resource Allocation Analysis
- Critical Path Tasks
- Milestone Tracker

*(Copy from `Timeline_Queries.txt`)*

### Step 4: Load DAX Measures

After loading data:
1. Go to **Modeling** tab
2. Click **New Measure**
3. Add measures from `Gantt_DAX_Measures.txt`

**Essential Measures:**
- Overall Project Progress
- Total Tasks, Completed Tasks, In Progress Tasks
- Critical Tasks Count
- Days Until Completion
- Schedule Performance Index
- Resource Utilization

### Step 5: Close & Apply
Click **Close & Apply** to load all data into Power BI.

---

## 📈 Page 1: Executive Timeline

### Page Theme
- **Background**: Light (#F9FAFB)
- **Accent Color**: Blue (#3B82F6)

### Visualizations

#### 1.1 Project KPI Cards (Top Row)

**A. Project Progress Card**
- Visual: Card
- Field: [Overall Project Progress]
- Format: `0%`
- Title: "Project Progress"
- Data Label: Large, Bold

**B. Tasks Completed Card**
- Visual: Card
- Field: [Completed Tasks] / [Total Tasks]
- Format: `00/00`
- Title: "Tasks Completed"

**C. Days to Completion Card**
- Visual: Card
- Field: [Days Until Completion]
- Format: `0 "days"`
- Title: "Days Remaining"
- Conditional Formatting:
  - Green if > 30 days
  - Orange if 7-30 days
  - Red if < 7 days

**D. Critical Tasks Card**
- Visual: Card
- Field: [Critical Tasks Count]
- Title: "Critical Tasks"
- Color: Red accent

#### 1.2 Timeline Gantt Visual (Center)

**Visual: Gantt Chart** (from marketplace)
- **Task**: Task Name
- **Start Date**: Start Date
- **Duration**: Task Duration Days
- **Resource**: Assigned To
- **Completion**: Progress (%)
- **Legend**: Status

**Formatting:**
- Bar Colors: Match status colors
- Show Today line
- Show dependency lines
- Grid: Weekly intervals

#### 1.3 Status Breakdown (Right Side)

**Visual: Donut Chart**
- **Legend**: Status
- **Values**: Count of Task ID
- **Colors**:
  - Completed: Green (#10B981)
  - In Progress: Orange (#F59E0B)
  - Not Started: Gray (#9CA3AF)
  - Blocked: Red (#EF4444)
  - On Hold: Purple (#8B5CF6)

#### 1.4 Priority Distribution (Right Side - Bottom)

**Visual: Stacked Bar Chart**
- **Axis**: Priority
- **Values**: Count of Tasks
- **Legend**: Status
- **Sort**: High → Medium → Low

### Slicers (Left Panel)

1. **Date Range Slicer**
   - Field: Start Date
   - Style: Between

2. **Status Slicer**
   - Field: Status
   - Style: Dropdown

3. **Assigned To Slicer**
   - Field: Assigned To
   - Style: List

---

## 📊 Page 2: Gantt Chart View

### Detailed Task Timeline

#### 2.1 Full Gantt Chart (Main Visual)

**Visual: Gantt Chart (Custom Visual)**
- **Task**: Task Name
- **Start**: Start Date
- **End**: Finish Date
- **Duration**: Duration (Days)
- **Progress**: Progress (%)
- **Parent**: Dependencies (for hierarchy)
- **Resource**: Assigned To

**Features:**
- Zoom capability (daily/weekly/monthly view)
- Scroll for long task lists
- Hover tooltips with task details
- Dependency lines visible
- Critical path highlighted in red

#### 2.2 Task Details Table (Bottom)

**Visual: Table**
- Task ID
- Task Name
- Duration (Days)
- Start Date
- Finish Date
- Progress (%)
- Status
- Assigned To
- Priority
- Notes (in tooltip)

**Formatting:**
- Conditional formatting on Progress column
- Status icons
- Priority color coding

#### 2.3 Filter Panel (Top)

**Filters:**
- Date Range
- Status (multi-select)
- Priority
- Assigned To
- Is Critical Path

---

## 🔴 Page 3: Critical Path Analysis

### Focus on Project Risks

#### 3.1 Critical Path KPIs (Top Row)

**A. Critical Tasks Card**
- Value: [Critical Tasks Count]
- Title: "Tasks on Critical Path"

**B. Critical Path Progress**
- Value: [Critical Path Progress]
- Format: Percentage
- Title: "Critical Path Progress"

**C. At-Risk Tasks**
- Value: [Critical Tasks At Risk]
- Title: "At-Risk Critical Tasks"
- Color: Red

**D. Critical Path Status**
- Value: [Critical Path Status]
- Title: "Overall Status"
- Dynamic color based on value

#### 3.2 Critical Path Timeline (Center)

**Visual: Gantt Chart**
- Filter: Critical Path = "Yes"
- Highlight: Red bars
- Show: Dependencies clearly
- Today marker: Bold line

#### 3.3 Critical Task Table (Bottom)

**Visual: Table**
- Filter: Critical Path = "Yes"
- Columns:
  - Task Name
  - Start Date
  - Finish Date
  - Progress
  - Days Remaining
  - Assigned To
  - Status

**Sort**: By Finish Date (earliest first)

**Conditional Formatting:**
- Row highlight if Overdue
- Progress bar visual
- Status icons

#### 3.4 Risk Indicators (Right Side)

**Visual: Card/Gauge**
- Overdue Critical Tasks
- Critical Tasks Due This Week
- Blocked Critical Tasks

**Color Coding:**
- Green: All on track
- Yellow: 1-2 at risk
- Red: 3+ at risk

---

## 👥 Page 4: Resource Management

### Team Workload and Allocation

#### 4.1 Resource KPIs (Top Row)

**A. Total Resources**
- Value: [Total Resources]
- Title: "Team Members"

**B. Average Utilization**
- Value: [Average Resource Utilization]
- Format: "0.0 days"
- Title: "Avg Workload per Person"

**C. Overallocated Resources**
- Value: [Overallocated Resources]
- Title: "Overallocated Team Members"
- Alert color if > 0

#### 4.2 Resource Allocation Chart (Center - Large)

**Visual: Stacked Bar Chart**
- **Axis**: Assigned To
- **Values**: Duration (Days)
- **Legend**: Status
- **Sort**: By total duration (descending)

**Data Labels**: Show total days

**Reference Line**: Add line at 40 days (overallocation threshold)

#### 4.3 Resource Timeline (Center - Bottom)

**Visual: Matrix or Gantt**
- **Rows**: Assigned To
- **Columns**: Week/Month
- **Values**: Task count or duration
- **Heat Map**: Color intensity by workload

#### 4.4 Resource Details Table (Right)

**Visual: Table**
Source: Resource Allocation Analysis query

Columns:
- Assigned To
- Total Tasks
- In Progress Tasks
- Completed Tasks
- Total Duration (Days)
- Utilization Level
- Completion Rate

**Conditional Formatting:**
- Utilization Level colors:
  - Green: Moderately Allocated
  - Orange: Fully Allocated
  - Red: Overallocated

---

## 🎯 Page 5: Milestone Tracker

### Key Deliverable Monitoring

#### 5.1 Milestone KPIs (Top Row)

**A. Total Milestones**
- Value: [Total Milestones]
- Title: "Total Milestones"

**B. Completed Milestones**
- Value: [Completed Milestones]
- Title: "Completed"
- Color: Green

**C. Upcoming Milestones**
- Value: [Upcoming Milestones]
- Title: "Upcoming (30 Days)"
- Color: Blue

**D. Milestone Completion Rate**
- Value: [Milestone Completion Rate]
- Format: Percentage
- Title: "Completion Rate"

#### 5.2 Milestone Timeline (Center)

**Visual: Timeline or Scatter Chart**
- **X-axis**: Finish Date
- **Y-axis**: Milestone Name
- **Size**: Importance/Priority
- **Color**: Status (Completed/Upcoming/Overdue)

**Markers:**
- Diamond shapes for milestones
- Today line
- Labels on hover

#### 5.3 Next Milestone Card (Top Right)

**Visual: Card with Details**
- Title: "Next Milestone"
- Milestone Name: [Next Milestone]
- Date: [Next Milestone Date]
- Days Until: Calculated
- Format: Large, prominent

#### 5.4 Milestone Details Table (Bottom)

**Visual: Table**
Filter: Is Milestone = "Yes"

Columns:
- Milestone Name
- Target Date
- Status
- Days Until/Since
- Assigned To
- Dependencies Met

**Conditional Formatting:**
- Green: Completed
- Blue: Upcoming
- Red: Overdue
- Orange: Due This Week

#### 5.5 Milestone Progress Gauge (Right)

**Visual: Gauge**
- Value: [Milestone Completion Rate]
- Min: 0%
- Max: 100%
- Target: 100%
- Color Zones:
  - Red: 0-40%
  - Yellow: 40-70%
  - Green: 70-100%

---

## 🎨 Interactive Features

### Cross-Page Filtering

Enable across all pages:
1. **View** → **Sync Slicers**
2. Select slicers to sync:
   - Date Range
   - Status
   - Priority
   - Assigned To

### Drill-Through Pages

Create drill-through for task details:
1. Create new page: "Task Detail"
2. Add drill-through field: Task Name
3. Show comprehensive task information

### Tooltips

Custom tooltips for visuals:
1. Create tooltip page
2. Add relevant metrics
3. Assign to visuals

### Bookmarks

Create bookmarks for views:
- All Tasks View
- Critical Path Only
- Current Sprint/Phase
- Overdue Tasks
- Resource-Specific Views

---

## 🚀 Publishing and Sharing

### Step 1: Save and Publish

1. **File** → **Save As**
2. Save locally: `Project_Timeline_Dashboard.pbix`
3. **Home** → **Publish**
4. Select workspace
5. Click **Publish**

### Step 2: Schedule Refresh

In Power BI Service:
1. Go to dataset settings
2. **Scheduled Refresh** → **Configure**
3. Set frequency: Daily at 8 AM
4. Add data source credentials
5. Apply

### Step 3: Create App

1. In Power BI Service workspace
2. **Create App**
3. Include all dashboard pages
4. Set permissions
5. Publish app

### Step 4: Share with Team

- **Option A**: Share dashboard link
- **Option B**: Embed in SharePoint/Teams
- **Option C**: Export to PowerPoint for presentations

---

## 💡 Best Practices

1. **Performance**: Limit data to relevant date range
2. **Colors**: Use consistent color scheme across pages
3. **Filters**: Make filters prominent and easy to use
4. **Labels**: Clear, concise titles
5. **Mobile**: Test mobile layout
6. **Refresh**: Schedule daily updates
7. **Security**: Set appropriate permissions

---

## 🔧 Advanced Features

### Custom Visuals to Consider

1. **Gantt Chart** (from marketplace)
2. **Timeline Slicer**
3. **Advanced Card** (by OKViz)
4. **Zebra BI Tables**
5. **Infographic Designer**

### AI Insights

Enable:
- **Analyze** → **Explain the increase/decrease**
- **Quick Insights** on datasets
- **Q&A** visual for natural language queries

---

## 📱 Mobile Layout

Optimize for mobile:
1. **View** → **Mobile Layout**
2. Rearrange visuals vertically
3. Prioritize KPIs at top
4. Test on Power BI mobile app

---

**Your Power BI Timeline Dashboard is now complete!** 🎉

For ongoing maintenance and updates, see the MS Project Setup Guide and User Manual.

