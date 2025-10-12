#!/usr/bin/env python3
"""
test_data_generator.py
Generate realistic test data for the Hybrid Project Management system.

This script creates sample CSV files, Excel templates, and mock data
for testing and demonstration purposes.

Usage:
    python test_data_generator.py
    python test_data_generator.py --weeks 24 --output test_data/
"""

import pandas as pd
import numpy as np
import os
import argparse
from datetime import datetime, timedelta
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils.dataframe import dataframe_to_rows

class ProjectDataGenerator:
    """Generate realistic project management test data"""
    
    def __init__(self, output_dir="test_data"):
        self.output_dir = output_dir
        self.ensure_output_dir()
    
    def ensure_output_dir(self):
        """Create output directory if it doesn't exist"""
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "csvs"), exist_ok=True)
    
    def generate_weekly_updates(self, weeks=12, start_date=None):
        """Generate realistic weekly update data"""
        if start_date is None:
            start_date = datetime.now() - timedelta(weeks=weeks)
        
        # Create realistic patterns
        base_tickets = 15
        seasonal_factor = np.sin(np.linspace(0, 2*np.pi, weeks)) * 3
        
        data = []
        csat_trend = 8.0  # Starting CSAT
        nps_trend = 50    # Starting NPS
        
        for i in range(weeks):
            week_start = start_date + timedelta(weeks=i)
            
            # Realistic ticket patterns
            tickets_opened = max(5, int(base_tickets + seasonal_factor[i] + np.random.normal(0, 2)))
            tickets_resolved = max(3, tickets_opened - np.random.randint(0, 3))
            
            # Realistic CSAT with slight improvement trend
            csat_trend += np.random.normal(0, 0.3)
            csat_trend = max(6.0, min(10.0, csat_trend))
            
            # Realistic NPS with some correlation to CSAT
            nps_trend += np.random.normal(0, 5)
            nps_trend = max(-50, min(100, nps_trend))
            
            # Add some variation
            csat = round(csat_trend + np.random.normal(0, 0.5), 1)
            nps = int(nps_trend + np.random.normal(0, 10))
            
            # Realistic notes
            if tickets_resolved > tickets_opened:
                notes = "Excellent week - caught up on backlog"
            elif tickets_opened > tickets_resolved + 3:
                notes = "High volume week - working through tickets"
            elif csat >= 9.0:
                notes = "Great customer feedback this week"
            elif csat <= 6.5:
                notes = "Some customer concerns - investigating"
            else:
                notes = "Normal operations"
            
            data.append({
                'Week Start': week_start.strftime('%Y-%m-%d'),
                'Tickets Opened': tickets_opened,
                'Tickets Resolved': tickets_resolved,
                'NPS': nps,
                'CSAT': csat,
                'Notes': notes
            })
        
        return pd.DataFrame(data)
    
    def generate_wbs_data(self):
        """Generate realistic Work Breakdown Structure data"""
        tasks = [
            {"name": "Project Initiation", "days": 5, "owner": "Project Manager"},
            {"name": "Requirements Gathering", "days": 10, "owner": "Business Analyst"},
            {"name": "System Design", "days": 15, "owner": "Solution Architect"},
            {"name": "Database Design", "days": 8, "owner": "Database Architect"},
            {"name": "Frontend Development", "days": 20, "owner": "Frontend Developer"},
            {"name": "Backend Development", "days": 25, "owner": "Backend Developer"},
            {"name": "API Development", "days": 12, "owner": "Backend Developer"},
            {"name": "Integration Testing", "days": 8, "owner": "QA Engineer"},
            {"name": "User Acceptance Testing", "days": 10, "owner": "QA Engineer"},
            {"name": "Deployment", "days": 3, "owner": "DevOps Engineer"},
            {"name": "Training", "days": 5, "owner": "Project Manager"},
            {"name": "Go-Live Support", "days": 7, "owner": "Support Team"}
        ]
        
        start_date = datetime.now()
        data = []
        
        for i, task in enumerate(tasks):
            task_id = f"T{i+1:03d}"
            planned_start = start_date + timedelta(days=i*2)
            planned_end = planned_start + timedelta(days=task["days"])
            
            # Simulate some tasks being completed or in progress
            if i < 8:  # First 8 tasks
                actual_start = planned_start
                if i < 5:  # First 5 tasks completed
                    actual_end = planned_end + timedelta(days=np.random.randint(-2, 3))
                    percent_complete = 100
                    status = "Completed"
                else:  # Tasks 6-8 in progress
                    actual_end = None
                    percent_complete = np.random.randint(30, 90)
                    status = "In Progress"
            else:  # Remaining tasks not started
                actual_start = None
                actual_end = None
                percent_complete = 0
                status = "Not Started"
            
            # Calculate RAG status
            if percent_complete == 100:
                rag_status = "Green"
            elif percent_complete >= 75:
                rag_status = "Green"
            elif percent_complete >= 50:
                rag_status = "Amber"
            else:
                rag_status = "Red"
            
            data.append({
                'WBS ID': task_id,
                'Task Name': task["name"],
                'Owner': task["owner"],
                'Planned Start': planned_start.strftime('%Y-%m-%d'),
                'Planned End': planned_end.strftime('%Y-%m-%d'),
                'Planned Days': task["days"],
                'Actual Start': actual_start.strftime('%Y-%m-%d') if actual_start else '',
                'Actual End': actual_end.strftime('%Y-%m-%d') if actual_end else '',
                'Actual Days': (actual_end - actual_start).days if actual_start and actual_end else '',
                '% Complete': percent_complete,
                'Status (RAG)': rag_status,
                'Dependencies': f"T{i:03d}" if i > 0 else ''
            })
        
        return pd.DataFrame(data)
    
    def generate_risk_issue_data(self):
        """Generate realistic risk and issue data"""
        risks = [
            {
                "type": "Risk",
                "description": "Key developer may leave during critical phase",
                "probability": 0.3,
                "impact": 4,
                "owner": "Project Manager",
                "mitigation": "Cross-train team members, prepare backup resources",
                "status": "Open"
            },
            {
                "type": "Risk", 
                "description": "Third-party API rate limits may impact performance",
                "probability": 0.4,
                "impact": 3,
                "owner": "Technical Lead",
                "mitigation": "Implement caching and request optimization",
                "status": "In Progress"
            },
            {
                "type": "Issue",
                "description": "Database performance degradation in test environment",
                "probability": 1.0,
                "impact": 2,
                "owner": "Database Administrator",
                "mitigation": "Optimize queries and add indexes",
                "status": "Closed"
            },
            {
                "type": "Risk",
                "description": "Budget constraints may limit scope",
                "probability": 0.2,
                "impact": 5,
                "owner": "Project Manager",
                "mitigation": "Prioritize features, prepare scope reduction plan",
                "status": "Open"
            },
            {
                "type": "Issue",
                "description": "User interface not meeting accessibility requirements",
                "probability": 1.0,
                "impact": 3,
                "owner": "Frontend Developer",
                "mitigation": "Redesign components for WCAG compliance",
                "status": "In Progress"
            }
        ]
        
        data = []
        for i, risk in enumerate(risks):
            score = risk["probability"] * risk["impact"]
            data.append({
                'ID': f"{'RISK' if risk['type'] == 'Risk' else 'ISSUE'}-{i+1:03d}",
                'Type (Risk/Issue)': risk["type"],
                'Description': risk["description"],
                'Probability (0-1)': risk["probability"],
                'Impact (1-5)': risk["impact"],
                'Score (P*I)': score,
                'Owner': risk["owner"],
                'Mitigation/Action': risk["mitigation"],
                'Status': risk["status"]
            })
        
        return pd.DataFrame(data)
    
    def generate_sprint_data(self):
        """Generate realistic sprint planning data"""
        sprints = []
        story_points_per_sprint = 20
        
        for sprint in range(1, 6):  # 5 sprints
            # Generate user stories for each sprint
            stories = [
                {"name": f"User Authentication Sprint {sprint}", "points": 5, "status": "Done"},
                {"name": f"Dashboard Features Sprint {sprint}", "points": 8, "status": "Done"},
                {"name": f"API Integration Sprint {sprint}", "points": 3, "status": "Done"},
                {"name": f"User Management Sprint {sprint}", "points": 5, "status": "Done"},
                {"name": f"Reporting Features Sprint {sprint}", "points": 5, "status": "In Progress"},
                {"name": f"Performance Optimization Sprint {sprint}", "points": 3, "status": "To Do"},
                {"name": f"Testing Sprint {sprint}", "points": 2, "status": "To Do"}
            ]
            
            for story in stories:
                sprints.append({
                    'Sprint': f"Sprint {sprint}",
                    'User Story': story["name"],
                    'Estimate (pts)': story["points"],
                    'Status': story["status"],
                    'Actual Effort (hrs)': np.random.randint(4, 12) if story["status"] == "Done" else '',
                    'Owner': np.random.choice(['Developer A', 'Developer B', 'Developer C', 'QA Engineer'])
                })
        
        return pd.DataFrame(sprints)
    
    def generate_project_overview(self):
        """Generate project overview data"""
        return pd.DataFrame([{
            'Project Name': 'Hybrid Project Management System',
            'Project Manager': 'John Smith',
            'Start Date': '2024-01-15',
            'Target Go-Live': '2024-06-30',
            'Budget': 150000,
            'Actual Cost': 125000,
            'Status': 'In Progress',
            'Health Score': 'Good'
        }])
    
    def create_sample_csv_files(self, weeks=12):
        """Create sample CSV files for testing"""
        weekly_data = self.generate_weekly_updates(weeks)
        
        # Split into individual weekly files
        for i, row in weekly_data.iterrows():
            filename = f"week_{i+1:02d}_{row['Week Start'].replace('-', '')}.csv"
            filepath = os.path.join(self.output_dir, "csvs", filename)
            
            # Create single-row DataFrame
            single_week = pd.DataFrame([row])
            single_week.to_csv(filepath, index=False)
        
        print(f"Created {len(weekly_data)} CSV files in {self.output_dir}/csvs/")
        return weekly_data
    
    def create_sample_excel_template(self):
        """Create a sample Excel template with all sheets"""
        filepath = os.path.join(self.output_dir, "sample_template.xlsx")
        
        with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
            # Project Overview
            self.generate_project_overview().to_excel(
                writer, sheet_name='Project_Overview', index=False
            )
            
            # WBS Task Plan
            self.generate_wbs_data().to_excel(
                writer, sheet_name='WBS_TaskPlan', index=False
            )
            
            # Risk Issue Log
            self.generate_risk_issue_data().to_excel(
                writer, sheet_name='Risk_Issue_Log', index=False
            )
            
            # Sprint Planner
            self.generate_sprint_data().to_excel(
                writer, sheet_name='Sprint_Planner', index=False
            )
            
            # Weekly Updates (empty template)
            weekly_template = pd.DataFrame(columns=[
                'Week Start', 'Tickets Opened', 'Tickets Resolved', 'NPS', 'CSAT', 'Notes'
            ])
            weekly_template.to_excel(writer, sheet_name='Weekly_Updates', index=False)
            
            # KPI Dashboard (empty template)
            kpi_template = pd.DataFrame(columns=['Metric', 'Value', 'Trend'])
            kpi_template.to_excel(writer, sheet_name='KPI_Dashboard', index=False)
        
        print(f"Created sample Excel template: {filepath}")
        return filepath
    
    def create_sample_config(self):
        """Create a sample configuration file"""
        config = {
            "EXCEL_PATH": "sample_template.xlsx",
            "WEEKLY_SHEET": "Weekly_Updates",
            "CSV_FOLDER": "./csvs",
            "START_ROW": 4,
            "BACKUP_ON_SAVE": True,
            "LOG_LEVEL": "INFO",
            "LOG_FILE": "weekly_update.log",
            "EMAIL_NOTIFICATIONS": {
                "ENABLED": False,
                "SMTP_SERVER": "smtp.gmail.com",
                "SMTP_PORT": 587,
                "EMAIL": "your.email@company.com",
                "PASSWORD": "your_app_password",
                "TO_EMAILS": ["manager@company.com", "team@company.com"]
            },
            "DATA_VALIDATION": {
                "MIN_CSAT": 0,
                "MAX_CSAT": 10,
                "MIN_NPS": -100,
                "MAX_NPS": 100,
                "MAX_TICKETS": 10000
            }
        }
        
        config_path = os.path.join(self.output_dir, "sample_config.json")
        import json
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)
        
        print(f"Created sample configuration: {config_path}")
        return config_path

def main():
    """Main function to generate test data"""
    parser = argparse.ArgumentParser(description='Generate test data for Hybrid Project Management')
    parser.add_argument('--weeks', type=int, default=12, help='Number of weeks of data to generate')
    parser.add_argument('--output', default='test_data', help='Output directory')
    
    args = parser.parse_args()
    
    print("Generating test data for Hybrid Project Management System...")
    
    generator = ProjectDataGenerator(args.output)
    
    # Generate all test data
    print("\nGenerating weekly updates data...")
    weekly_data = generator.create_sample_csv_files(args.weeks)
    
    print("\nCreating Excel template...")
    excel_file = generator.create_sample_excel_template()
    
    print("\nCreating sample configuration...")
    config_file = generator.create_sample_config()
    
    print(f"\nTest data generation complete!")
    print(f"Output directory: {args.output}")
    print(f"Generated {len(weekly_data)} weeks of data")
    print(f"Created Excel template with sample data")
    print(f"Created configuration template")
    
    print(f"\nTo test the automation:")
    print(f"   1. Copy the generated files to your automation directory")
    print(f"   2. Update the configuration file with your settings")
    print(f"   3. Run: python update_weekly.py")
    
    print(f"\nTo test Power BI:")
    print(f"   1. Open Power BI Desktop")
    print(f"   2. Import the Excel template and CSV folder")
    print(f"   3. Follow the Power BI setup guide")

if __name__ == "__main__":
    main()
