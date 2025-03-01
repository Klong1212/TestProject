#!/bin/python3

import unittest
from itertools import combinations

def is_alternating(s):
    """Check if a string alternates between two characters."""
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True

def alternate(s):
    """Find the longest alternating string with only two distinct characters."""
    unique_chars = set(s)
    max_length = 0

    for char1, char2 in combinations(unique_chars, 2):
        filtered = [c for c in s if c in (char1, char2)]
        if is_alternating(filtered):
            max_length = max(max_length, len(filtered))

    return max_length

class TestAlternate(unittest.TestCase):
    
    def test_simple_alternating(self):
        """Test with a simple alternating string."""
        self.assertEqual(alternate("abababab"), 8)
    
    def test_non_alternating(self):
        """Test with a non-alternating string."""
        self.assertEqual(alternate("aaa"), 0)
    
    def test_all_different_chars(self):
        """Test with a string containing all different characters."""
        self.assertEqual(alternate("abcdefghij"), 2)
    
    def test_potential_alternation(self):
        """Test with a string that has potential for alternation."""
        self.assertEqual(alternate("beabeefeab"), 5)
    
    def test_empty_string(self):
        """Test with an empty string."""
        self.assertEqual(alternate(""), 0)
    
    def test_complex_case(self):
        """Test with a complex string containing repeated characters."""
        self.assertEqual(alternate("asvkugfiugsalddlasguifgukvsa"), 8)
