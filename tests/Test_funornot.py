import unittest
from Algorithms.Fun0rNot import funnyString

class TestFunnyString(unittest.TestCase):
    
    def test_funny_string_examples(self):
        """Test examples of strings that should be funny"""
        self.assertEqual(funnyString("acxz"), "Funny")
        self.assertNotEqual(funnyString("bcxz"), "Funny")
        self.assertEqual(funnyString("aaaa"), "Funny")  # Same character repeated is always funny
        self.assertEqual(funnyString("a"), "Funny")  # Single character is funny by default
        self.assertEqual(funnyString("ab"), "Funny")  # Two characters are always funny
        
    def test_not_funny_string_examples(self):
        """Test examples of strings that should not be funny"""
        self.assertNotEqual(funnyString("abcd"), "Not Funny")
        self.assertNotEqual(funnyString("lmnop"), "Not Funny")
        
    def test_hackerrank_examples(self):
        """Test with examples provided in HackerRank problem"""
        self.assertEqual(funnyString("acxz"), "Funny")
        self.assertEqual(funnyString("bcxz"), "Not Funny")
        
    def test_palindrome_strings(self):
        """Test with palindrome strings which should always be funny"""
        self.assertEqual(funnyString("racecar"), "Funny")
        self.assertEqual(funnyString("madam"), "Funny")
        self.assertEqual(funnyString("level"), "Funny")
        
    def test_edge_cases(self):
        """Test edge cases"""
        self.assertEqual(funnyString("z"), "Funny")  # Single character
        self.assertEqual(funnyString("ab"), "Funny")  # Two characters
        self.assertEqual(funnyString("abcba"), "Funny")  # Palindrome
        
    def test_long_string(self):
        """Test with a longer string"""
        self.assertEqual(funnyString("abcdefghijklmnopqrstuvwxyz"), "Not Funny")