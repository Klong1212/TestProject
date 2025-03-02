import unittest
from Algorithms.number_utils import is_prime_list

class TestIsPrimeList(unittest.TestCase):
    def test_all_primes(self):
        # Arrange
        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        
        # Act
        result = is_prime_list(prime_numbers)
        
        # Assert
        self.assertTrue(result, "Should return True for a list of all prime numbers")
    
    def test_some_non_primes(self):
        # Arrange
        mixed_numbers = [2, 3, 4, 5]  # 4 is not prime
        
        # Act
        result = is_prime_list(mixed_numbers)
        
        # Assert
        self.assertFalse(result, "Should return False if any number in the list is not prime")
    
    def test_edge_cases(self):
        # Arrange
        edge_cases = [0, 1, 2, 3]  # 0 and 1 are not prime
        
        # Act
        result = is_prime_list(edge_cases)
        
        # Assert
        self.assertFalse(result, "Should return False for lists containing 0 or 1")
    
    def test_negative_numbers(self):
        # Arrange
        negative_numbers = [-7, -5, -3, -2]  # Negative numbers are not prime
        
        # Act
        result = is_prime_list(negative_numbers)
        
        # Assert
        self.assertFalse(result, "Should return False for negative numbers")
    
    def test_large_primes(self):
        # Arrange
        large_primes = [10007, 10009, 10037]  # These are all prime
        
        # Act
        result = is_prime_list(large_primes)
        
        # Assert
        self.assertTrue(result, "Should correctly identify large prime numbers")
    
    def test_empty_list(self):
        # Arrange
        empty_list = []
        
        # Act
        result = is_prime_list(empty_list)
        
        # Assert
        self.assertTrue(result, "Should return True for an empty list (vacuously true)")
    
    def test_single_element(self):
        # Arrange: Test with single prime and non-prime numbers
        prime_list = [17]
        non_prime_list = [15]
        
        # Act
        prime_result = is_prime_list(prime_list)
        non_prime_result = is_prime_list(non_prime_list)
        
        # Assert
        self.assertTrue(prime_result, "Should return True for a list with a single prime number")
        self.assertFalse(non_prime_result, "Should return False for a list with a single non-prime number")
