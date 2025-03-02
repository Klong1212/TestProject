import unittest
from io import StringIO
import sys

# Assuming your fizz_buzz function is in a module called fizzbuzz_module
from Algorithms.fizzbuzz import fizz_buzz

class TestFizzBuzz(unittest.TestCase):

    def setUp(self):
        # Redirect stdout to capture print statements
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        # Reset stdout
        sys.stdout = sys.__stdout__

    def test_fizz_buzz(self):
        # Test the function with n=15 to cover all cases
        fizz_buzz(15)
        
        # Check printed output
        expected_output = "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n"
        self.assertEqual(self.captured_output.getvalue(), expected_output)
    
    def test_empty_range(self):
        # Test with n=0 (empty range)
        fizz_buzz(0)
        self.assertEqual(self.captured_output.getvalue(), "")
