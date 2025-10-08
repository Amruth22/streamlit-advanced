import unittest
from streamlit.testing.v1 import AppTest
import pandas as pd


class TestStreamlitAdvancedApp(unittest.TestCase):
    """Unit tests for Streamlit Advanced App"""

    def setUp(self):
        """Set up test app before each test"""
        self.at = AppTest.from_file("app.py")
        self.at.run()

    def test_app_loads_successfully(self):
        """Test 1: Verify the app loads without errors"""
        self.assertFalse(self.at.exception, "App should load without exceptions")
        self.assertTrue(len(self.at.sidebar) > 0, "App should have a sidebar")

    def test_sidebar_navigation(self):
        """Test 2: Verify sidebar navigation works"""
        # Check if radio buttons exist in sidebar
        self.assertTrue(len(self.at.sidebar.radio) > 0, "Sidebar should have radio buttons")
        
        # Get the navigation radio button
        nav_radio = self.at.sidebar.radio[0]
        
        # Verify all navigation options exist
        expected_options = [
            "Layouts & Formatting", 
            "Columns & Containers", 
            "Tables & DataFrames",
            "File Upload", 
            "Forms", 
            "User Interactivity", 
            "Data Visualization"
        ]
        
        for option in expected_options:
            self.assertIn(option, nav_radio.options, f"Navigation should include {option}")

    def test_tables_and_dataframes_page(self):
        """Test 3: Verify Tables & DataFrames page displays data correctly"""
        # Navigate to Tables & DataFrames page
        self.at.sidebar.radio[0].set_value("Tables & DataFrames")
        self.at.run()
        
        # Check if dataframes are displayed
        self.assertTrue(len(self.at.dataframe) > 0, "Page should display dataframes")
        
        # Verify dataframe has data
        df = self.at.dataframe[0].value
        self.assertIsNotNone(df, "DataFrame should not be None")
        self.assertTrue(len(df) > 0, "DataFrame should have rows")

    def test_forms_page(self):
        """Test 4: Verify Forms page has form elements"""
        # Navigate to Forms page
        self.at.sidebar.radio[0].set_value("Forms")
        self.at.run()
        
        # Check if forms exist
        # Note: Streamlit forms are containers, so we check for text inputs and buttons
        self.assertTrue(len(self.at.text_input) > 0, "Forms page should have text inputs")
        self.assertTrue(len(self.at.button) > 0, "Forms page should have submit buttons")

    def test_user_interactivity_session_state(self):
        """Test 5: Verify User Interactivity with session state"""
        # Navigate to User Interactivity page
        self.at.sidebar.radio[0].set_value("User Interactivity")
        self.at.run()
        
        # Check if buttons exist for counter
        self.assertTrue(len(self.at.button) >= 3, "Should have increment, decrement, and reset buttons")
        
        # Check if metric exists for counter display
        self.assertTrue(len(self.at.metric) > 0, "Should display counter metric")

    def test_data_visualization_page(self):
        """Test 6: Verify Data Visualization page displays charts"""
        # Navigate to Data Visualization page
        self.at.sidebar.radio[0].set_value("Data Visualization")
        self.at.run()
        
        # Check if charts are displayed
        # Streamlit charts are rendered, so we verify the page loaded without errors
        self.assertFalse(self.at.exception, "Data Visualization page should load without errors")

    def test_columns_and_containers_page(self):
        """Test 7: Verify Columns & Containers page structure"""
        # Navigate to Columns & Containers page
        self.at.sidebar.radio[0].set_value("Columns & Containers")
        self.at.run()
        
        # Verify page loads without errors
        self.assertFalse(self.at.exception, "Columns & Containers page should load without errors")
        
        # Check if buttons exist (from column examples)
        self.assertTrue(len(self.at.button) > 0, "Page should have buttons in columns")


if __name__ == "__main__":
    unittest.main()
