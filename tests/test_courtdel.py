import unittest
from Algorithms.courtdel import alternatingCharacters

class TestAlternatingCharacters(unittest.TestCase):
    
    def test_basic_examples(self):
        """Test with basic examples"""
        self.assertEqual(alternatingCharacters("AAAA"), 3)  # Need to delete 3 A's
        self.assertEqual(alternatingCharacters("BBBBB"), 4)  # Need to delete 4 B's
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)  # Already alternating
        self.assertEqual(alternatingCharacters("BABABA"), 0)  # Already alternating
        
    def test_mixed_repeats(self):
        """Test with strings having different sections of repeats"""
        self.assertEqual(alternatingCharacters("AAABBB"), 4)  # Delete 2 A's and 2 B's
        self.assertEqual(alternatingCharacters("AABBAABB"), 4)  # Delete 1 A and 1 B
        self.assertEqual(alternatingCharacters("AABBAA"), 3)  # Delete 1 A, 1 B, and 1 A
        
    def test_edge_cases(self):
        """Test edge cases"""
        self.assertEqual(alternatingCharacters("A"), 0)  # Single character
        self.assertEqual(alternatingCharacters("AB"), 0)  # Already alternating
        self.assertEqual(alternatingCharacters("ABBBBAAAA"), 6)  # Multiple deletions
        self.assertEqual(alternatingCharacters(""),0)
        
    def test_longer_strings(self):
        """Test with longer strings"""
        self.assertEqual(alternatingCharacters("AABABBAABBABABAA"), 5)
        self.assertEqual(alternatingCharacters("AAAAAAAAAAAA"),11)
        
    def test_hackerrank_examples(self):
        """Test with examples from HackerRank problem"""
        self.assertEqual(alternatingCharacters("AAAA"), 3)
        self.assertEqual(alternatingCharacters("BBBBB"), 4)
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)
        self.assertEqual(alternatingCharacters("BABABA"), 0)
        self.assertEqual(alternatingCharacters("AAABBB"), 4)
