import unittest
from io import StringIO
import sys
from Algorithms.staircase import staircase  # Assuming the function is in a module called staircase_module

class TestStaircase(unittest.TestCase):
    def setUp(self):
        # Redirect stdout to capture print statements
        self.captured_output = StringIO()
        self.old_stdout = sys.stdout
        sys.stdout = self.captured_output

    def tearDown(self):
        # Reset stdout
        sys.stdout = self.old_stdout

    def test_staircase_default_character(self):
        # Arrange
        n = 4
        expected_output = "#\n##\n###\n####\n"
        
        # Act
        staircase(n)
        
        # Assert
        self.assertEqual(self.captured_output.getvalue(), expected_output)
    
    def test_staircase_custom_character(self):
        # Arrange
        n = 3
        display = "*"
        expected_output = "*\n**\n***\n"
        
        # Act
        staircase(n, display)
        
        # Assert
        self.assertEqual(self.captured_output.getvalue(), expected_output)
    
    def test_staircase_boundary_values(self):
        # Arrange
        # Test n=1 (minimum valid value)
        expected_output = "#\n"
        
        # Act
        staircase(1)
        
        # Assert
        self.assertEqual(self.captured_output.getvalue(), expected_output)
        
        # Clear captured output for next test
        self.captured_output = StringIO()
        sys.stdout = self.captured_output
        
        # Arrange
        # Test n=30 (maximum valid value)
        expected_first_line = "#\n"
        expected_last_line = "#" * 30
        
        # Act
        staircase(30)
        output_lines = self.captured_output.getvalue().split('\n')
        
        # Assert
        self.assertEqual(output_lines[0], "#")  # First line has 1 character
        self.assertEqual(output_lines[29], "#" * 30)  # Last line has 30 characters
    
    def test_invalid_input(self):
        # Arrange & Act & Assert
        with self.assertRaises(ValueError):
            staircase(0)  # n is too small
            
        with self.assertRaises(ValueError):
            staircase(31)  # n is too large
            
        with self.assertRaises(ValueError):
            staircase(4, "##")  # display is not a single character