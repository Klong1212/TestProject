import unittest
import string
from Algorithms.eyncrip import caesarCipher

class TestCaesarCipher(unittest.TestCase):
    
    def test_basic_rotation(self):
        """Test basic rotations with different values of k"""
        self.assertEqual(caesarCipher("abc", 1), "bcd")
        self.assertEqual(caesarCipher("xyz", 1), "yza")
        self.assertEqual(caesarCipher("ABC", 3), "DEF")
        self.assertEqual(caesarCipher("XYZ", 3), "ABC")
        
    def test_preserve_case(self):
        """Test that the function preserves case correctly"""
        self.assertEqual(caesarCipher("AbC", 1), "BcD")
        self.assertEqual(caesarCipher("xYz", 5), "cDe")
        
    def test_special_characters(self):
        """Test that non-alphabetic characters remain unchanged"""
        self.assertEqual(caesarCipher("a-b-c", 1), "b-c-d")
        self.assertEqual(caesarCipher("Hello, World!", 4), "Lipps, Asvph!")
        self.assertEqual(caesarCipher("123!@#", 10), "123!@#")
        
    def test_large_rotation(self):
        """Test with large rotation values (greater than 26)"""
        self.assertEqual(caesarCipher("abc", 27), "bcd")  # 27 % 26 = 1
        self.assertEqual(caesarCipher("xyz", 52), "xyz")  # 52 % 26 = 0
        self.assertEqual(caesarCipher("ABC", 29), "DEF")  # 29 % 26 = 3
        
    def test_empty_string(self):
        """Test with an empty string"""
        self.assertEqual(caesarCipher("", 5), "")
        
    def test_complex_examples(self):
        """Test with more complex examples"""
        self.assertEqual(caesarCipher("middle-Outz", 2), "okffng-Qwvb")
        self.assertEqual(caesarCipher("Always-Look-on-the-Bright-Side-of-Life", 5), 
                         "Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj")
        
    def test_zero_rotation(self):
        """Test with zero rotation (should return the same string)"""
        self.assertEqual(caesarCipher("Hello, World!", 0), "Hello, World!")
