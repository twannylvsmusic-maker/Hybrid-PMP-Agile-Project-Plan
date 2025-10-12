#!/usr/bin/env python3
"""
test_automation.py
Comprehensive testing suite for the Hybrid Project Management automation system.

Features:
- Unit tests for all automation functions
- Integration tests for CSV processing
- Excel file validation tests
- Performance benchmarks
- Mock data generation

Usage:
    python test_automation.py
    python test_automation.py --verbose
    python test_automation.py --coverage
"""

import unittest
import pandas as pd
import numpy as np
import tempfile
import os
import shutil
import json
from datetime import datetime, timedelta
from unittest.mock import patch, MagicMock
import sys
sys.path.append('../automation')

# Import the automation module
try:
    from update_weekly import (
        read_all_weekly_csvs, 
        validate_data_quality, 
        analyze_trends,
        write_to_excel,
        CONFIG
    )
except ImportError:
    print("Warning: Could not import automation module. Some tests may fail.")
    print("Make sure to run tests from the project root directory.")

class TestDataValidation(unittest.TestCase):
    """Test data validation functions"""
    
    def setUp(self):
        """Set up test data"""
        self.valid_data = pd.DataFrame({
            'Week Start': pd.date_range('2024-01-01', periods=4, freq='W'),
            'Tickets Opened': [10, 12, 8, 15],
            'Tickets Resolved': [9, 11, 7, 14],
            'NPS': [50, 45, 55, 60],
            'CSAT': [8.5, 8.0, 9.0, 8.7],
            'Notes': ['Good week', 'Busy period', 'Excellent', 'Normal']
        })
        
        self.invalid_data = pd.DataFrame({
            'Week Start': ['invalid', '2024-01-08', '2024-01-15'],
            'Tickets Opened': [10, -5, 'invalid'],
            'Tickets Resolved': [9, 15, 8],
            'NPS': [150, -200, 50],  # Out of range
            'CSAT': [15, 5, -2],     # Out of range
            'Notes': ['Good', 'Bad', 'Normal']
        })
    
    def test_valid_data_quality(self):
        """Test validation with valid data"""
        issues = validate_data_quality(self.valid_data)
        self.assertEqual(len(issues), 0, "Valid data should have no quality issues")
    
    def test_invalid_data_quality(self):
        """Test validation with invalid data"""
        issues = validate_data_quality(self.invalid_data)
        self.assertGreater(len(issues), 0, "Invalid data should have quality issues")
        
        # Check for specific issues
        issue_text = '; '.join(issues)
        self.assertIn('Invalid CSAT values', issue_text)
        self.assertIn('Invalid NPS values', issue_text)
    
    def test_missing_data_detection(self):
        """Test detection of missing data"""
        data_with_missing = self.valid_data.copy()
        data_with_missing.loc[0, 'CSAT'] = np.nan
        data_with_missing.loc[1, 'NPS'] = np.nan
        
        issues = validate_data_quality(data_with_missing)
        self.assertGreater(len(issues), 0)
        self.assertIn('Missing values', '; '.join(issues))
    
    def test_future_date_detection(self):
        """Test detection of future dates"""
        future_data = self.valid_data.copy()
        future_data.loc[0, 'Week Start'] = datetime.now() + timedelta(days=30)
        
        issues = validate_data_quality(future_data)
        self.assertGreater(len(issues), 0)
        self.assertIn('Future dates detected', '; '.join(issues))

class TestTrendAnalysis(unittest.TestCase):
    """Test trend analysis functions"""
    
    def setUp(self):
        """Set up test data for trend analysis"""
        self.trending_data = pd.DataFrame({
            'Week Start': pd.date_range('2024-01-01', periods=8, freq='W'),
            'CSAT': [7.0, 7.5, 8.0, 8.5, 8.7, 9.0, 9.2, 9.5],  # Improving trend
            'Tickets Resolved': [5, 6, 7, 8, 9, 10, 11, 12]     # Increasing trend
        })
        
        self.declining_data = pd.DataFrame({
            'Week Start': pd.date_range('2024-01-01', periods=8, freq='W'),
            'CSAT': [9.0, 8.5, 8.0, 7.5, 7.0, 6.5, 6.0, 5.5],  # Declining trend
            'Tickets Resolved': [12, 11, 10, 9, 8, 7, 6, 5]     # Decreasing trend
        })
    
    def test_improving_trend_detection(self):
        """Test detection of improving trends"""
        trends = analyze_trends(self.trending_data)
        
        self.assertIn('CSAT', trends)
        self.assertEqual(trends['CSAT']['trend'], 'improving')
        
        self.assertIn('Resolution', trends)
        self.assertEqual(trends['Resolution']['trend'], 'improving')
    
    def test_declining_trend_detection(self):
        """Test detection of declining trends"""
        trends = analyze_trends(self.declining_data)
        
        self.assertIn('CSAT', trends)
        self.assertEqual(trends['CSAT']['trend'], 'declining')
    
    def test_insufficient_data(self):
        """Test handling of insufficient data"""
        insufficient_data = pd.DataFrame({
            'Week Start': [datetime.now()],
            'CSAT': [8.0]
        })
        
        trends = analyze_trends(insufficient_data)
        self.assertIn('error', trends)

class TestCSVProcessing(unittest.TestCase):
    """Test CSV processing functions"""
    
    def setUp(self):
        """Set up temporary directory for test files"""
        self.test_dir = tempfile.mkdtemp()
        self.csv_dir = os.path.join(self.test_dir, 'csvs')
        os.makedirs(self.csv_dir, exist_ok=True)
    
    def tearDown(self):
        """Clean up test files"""
        shutil.rmtree(self.test_dir)
    
    def create_test_csv(self, filename, data):
        """Helper method to create test CSV files"""
        filepath = os.path.join(self.csv_dir, filename)
        data.to_csv(filepath, index=False)
        return filepath
    
    def test_single_csv_processing(self):
        """Test processing of a single CSV file"""
        test_data = pd.DataFrame({
            'Week Start': ['2024-01-01', '2024-01-08'],
            'Tickets Opened': [10, 12],
            'Tickets Resolved': [9, 11],
            'NPS': [50, 45],
            'CSAT': [8.5, 8.0],
            'Notes': ['Good week', 'Busy period']
        })
        
        self.create_test_csv('test1.csv', test_data)
        
        result = read_all_weekly_csvs(self.csv_dir)
        
        self.assertEqual(len(result), 2)
        self.assertEqual(result['Tickets Opened'].sum(), 22)
        self.assertEqual(result['CSAT'].mean(), 8.25)
    
    def test_multiple_csv_processing(self):
        """Test processing of multiple CSV files"""
        # Create first CSV
        data1 = pd.DataFrame({
            'Week Start': ['2024-01-01'],
            'Tickets Opened': [10],
            'Tickets Resolved': [9],
            'NPS': [50],
            'CSAT': [8.5],
            'Notes': ['Week 1']
        })
        
        # Create second CSV
        data2 = pd.DataFrame({
            'Week Start': ['2024-01-08'],
            'Tickets Opened': [12],
            'Tickets Resolved': [11],
            'NPS': [45],
            'CSAT': [8.0],
            'Notes': ['Week 2']
        })
        
        self.create_test_csv('week1.csv', data1)
        self.create_test_csv('week2.csv', data2)
        
        result = read_all_weekly_csvs(self.csv_dir)
        
        self.assertEqual(len(result), 2)
        self.assertEqual(list(result['Week Start'].dt.date), 
                        [datetime(2024, 1, 1).date(), datetime(2024, 1, 8).date()])
    
    def test_duplicate_handling(self):
        """Test handling of duplicate entries"""
        data = pd.DataFrame({
            'Week Start': ['2024-01-01', '2024-01-01'],  # Duplicate date
            'Tickets Opened': [10, 15],
            'Tickets Resolved': [9, 12],
            'NPS': [50, 55],
            'CSAT': [8.5, 9.0],
            'Notes': ['First entry', 'Second entry']
        })
        
        self.create_test_csv('duplicates.csv', data)
        
        result = read_all_weekly_csvs(self.csv_dir)
        
        # Should keep only the last entry
        self.assertEqual(len(result), 1)
        self.assertEqual(result.iloc[0]['Tickets Opened'], 15)
        self.assertEqual(result.iloc[0]['Notes'], 'Second entry')
    
    def test_empty_directory(self):
        """Test handling of empty CSV directory"""
        result = read_all_weekly_csvs(self.csv_dir)
        
        self.assertTrue(result.empty)
        self.assertEqual(list(result.columns), 
                        ['Week Start', 'Tickets Opened', 'Tickets Resolved', 'NPS', 'CSAT', 'Notes'])
    
    def test_invalid_csv_files(self):
        """Test handling of invalid CSV files"""
        # Create a file that's not a CSV
        invalid_file = os.path.join(self.csv_dir, 'invalid.txt')
        with open(invalid_file, 'w') as f:
            f.write("This is not a CSV file")
        
        # Create a valid CSV
        valid_data = pd.DataFrame({
            'Week Start': ['2024-01-01'],
            'Tickets Opened': [10],
            'Tickets Resolved': [9],
            'NPS': [50],
            'CSAT': [8.5],
            'Notes': ['Valid data']
        })
        self.create_test_csv('valid.csv', valid_data)
        
        # Should process only the valid CSV
        result = read_all_weekly_csvs(self.csv_dir)
        self.assertEqual(len(result), 1)

class TestExcelIntegration(unittest.TestCase):
    """Test Excel file integration"""
    
    def setUp(self):
        """Set up test Excel file"""
        self.test_dir = tempfile.mkdtemp()
        self.excel_path = os.path.join(self.test_dir, 'test_template.xlsx')
        
        # Create a simple test Excel file
        test_data = pd.DataFrame({
            'Week Start': pd.date_range('2024-01-01', periods=3, freq='W'),
            'Tickets Opened': [10, 12, 8],
            'Tickets Resolved': [9, 11, 7],
            'NPS': [50, 45, 55],
            'CSAT': [8.5, 8.0, 9.0],
            'Notes': ['Week 1', 'Week 2', 'Week 3']
        })
        
        with pd.ExcelWriter(self.excel_path, engine='openpyxl') as writer:
            test_data.to_excel(writer, sheet_name='Weekly_Updates', index=False)
    
    def tearDown(self):
        """Clean up test files"""
        shutil.rmtree(self.test_dir)
    
    @patch('update_weekly.CONFIG', {
        'EXCEL_PATH': '',
        'WEEKLY_SHEET': 'Weekly_Updates',
        'BACKUP_ON_SAVE': False
    })
    def test_excel_write_functionality(self):
        """Test Excel writing functionality"""
        # Update config for test
        from update_weekly import CONFIG
        CONFIG['EXCEL_PATH'] = self.excel_path
        CONFIG['BACKUP_ON_SAVE'] = False
        
        new_data = pd.DataFrame({
            'Week Start': pd.date_range('2024-01-22', periods=2, freq='W'),
            'Tickets Opened': [15, 18],
            'Tickets Resolved': [14, 17],
            'NPS': [60, 65],
            'CSAT': [9.0, 9.2],
            'Notes': ['Week 4', 'Week 5']
        })
        
        # Test the write function
        written_rows = write_to_excel(self.excel_path, 'Weekly_Updates', new_data, 4)
        
        self.assertEqual(written_rows, 2)
        
        # Verify the data was written correctly
        result = pd.read_excel(self.excel_path, sheet_name='Weekly_Updates')
        self.assertGreaterEqual(len(result), 2)  # Should have at least the new data
    
    def test_excel_file_not_found(self):
        """Test handling of missing Excel file"""
        nonexistent_path = os.path.join(self.test_dir, 'nonexistent.xlsx')
        
        new_data = pd.DataFrame({
            'Week Start': ['2024-01-01'],
            'Tickets Opened': [10],
            'Tickets Resolved': [9],
            'NPS': [50],
            'CSAT': [8.5],
            'Notes': ['Test']
        })
        
        with self.assertRaises(FileNotFoundError):
            write_to_excel(nonexistent_path, 'Weekly_Updates', new_data, 4)

class TestConfiguration(unittest.TestCase):
    """Test configuration management"""
    
    def test_default_config_structure(self):
        """Test that default config has required keys"""
        required_keys = [
            'EXCEL_PATH', 'WEEKLY_SHEET', 'CSV_FOLDER', 'START_ROW',
            'BACKUP_ON_SAVE', 'LOG_LEVEL', 'LOG_FILE', 'EMAIL_NOTIFICATIONS',
            'DATA_VALIDATION'
        ]
        
        for key in required_keys:
            self.assertIn(key, CONFIG, f"Config missing required key: {key}")
    
    def test_data_validation_config(self):
        """Test data validation configuration"""
        validation_config = CONFIG['DATA_VALIDATION']
        
        self.assertIn('MIN_CSAT', validation_config)
        self.assertIn('MAX_CSAT', validation_config)
        self.assertIn('MIN_NPS', validation_config)
        self.assertIn('MAX_NPS', validation_config)
        
        # Test reasonable ranges
        self.assertGreaterEqual(validation_config['MAX_CSAT'], validation_config['MIN_CSAT'])
        self.assertGreaterEqual(validation_config['MAX_NPS'], validation_config['MIN_NPS'])

class TestPerformance(unittest.TestCase):
    """Test performance benchmarks"""
    
    def test_large_dataset_processing(self):
        """Test processing of large datasets"""
        # Create a large dataset
        large_data = pd.DataFrame({
            'Week Start': pd.date_range('2020-01-01', periods=200, freq='W'),
            'Tickets Opened': np.random.randint(5, 50, 200),
            'Tickets Resolved': np.random.randint(5, 50, 200),
            'NPS': np.random.randint(-100, 100, 200),
            'CSAT': np.random.uniform(0, 10, 200),
            'Notes': [f'Week {i}' for i in range(200)]
        })
        
        start_time = datetime.now()
        
        # Test data validation
        issues = validate_data_quality(large_data)
        
        # Test trend analysis
        trends = analyze_trends(large_data)
        
        end_time = datetime.now()
        processing_time = (end_time - start_time).total_seconds()
        
        # Should complete within reasonable time (adjust threshold as needed)
        self.assertLess(processing_time, 5.0, "Processing large dataset took too long")
        
        # Should handle large dataset without errors
        self.assertIsInstance(issues, list)
        self.assertIsInstance(trends, dict)

class MockDataGenerator:
    """Generate mock data for testing"""
    
    @staticmethod
    def generate_weekly_data(weeks=12, start_date=None):
        """Generate mock weekly data"""
        if start_date is None:
            start_date = datetime.now() - timedelta(weeks=weeks)
        
        data = []
        for i in range(weeks):
            week_start = start_date + timedelta(weeks=i)
            data.append({
                'Week Start': week_start.strftime('%Y-%m-%d'),
                'Tickets Opened': np.random.randint(5, 25),
                'Tickets Resolved': np.random.randint(4, 24),
                'NPS': np.random.randint(-50, 100),
                'CSAT': round(np.random.uniform(6, 10), 1),
                'Notes': f'Week {i+1} data'
            })
        
        return pd.DataFrame(data)
    
    @staticmethod
    def generate_risk_data(count=10):
        """Generate mock risk data"""
        data = []
        for i in range(count):
            data.append({
                'ID': f'RISK-{i+1:03d}',
                'Type (Risk/Issue)': np.random.choice(['Risk', 'Issue']),
                'Description': f'Mock risk/issue {i+1}',
                'Probability (0-1)': round(np.random.uniform(0, 1), 2),
                'Impact (1-5)': np.random.randint(1, 6),
                'Score (P*I)': 0,  # Will be calculated
                'Owner': f'Owner {np.random.randint(1, 6)}',
                'Mitigation/Action': f'Action {i+1}' if np.random.random() > 0.3 else '',
                'Status': np.random.choice(['Open', 'In Progress', 'Closed', 'Mitigated'])
            })
        
        df = pd.DataFrame(data)
        df['Score (P*I)'] = df['Probability (0-1)'] * df['Impact (1-5)']
        return df

def run_tests(verbose=False, coverage=False):
    """Run the test suite"""
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add test classes
    test_classes = [
        TestDataValidation,
        TestTrendAnalysis,
        TestCSVProcessing,
        TestExcelIntegration,
        TestConfiguration,
        TestPerformance
    ]
    
    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2 if verbose else 1)
    result = runner.run(test_suite)
    
    # Print summary
    print(f"\n{'='*50}")
    print(f"TEST SUMMARY")
    print(f"{'='*50}")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
    
    if result.failures:
        print(f"\nFAILURES:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback.split('AssertionError:')[-1].strip()}")
    
    if result.errors:
        print(f"\nERRORS:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback.split('Exception:')[-1].strip()}")
    
    return result.wasSuccessful()

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Run automation tests')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    parser.add_argument('--coverage', '-c', action='store_true', help='Run with coverage analysis')
    
    args = parser.parse_args()
    
    success = run_tests(verbose=args.verbose, coverage=args.coverage)
    
    if success:
        print(f"\n✅ All tests passed!")
        sys.exit(0)
    else:
        print(f"\n❌ Some tests failed!")
        sys.exit(1)
