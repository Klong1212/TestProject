def is_prime_list(numbers):
    """
    Check if all numbers in the given list are prime.
    
    Args:
        numbers: A list of integers
        
    Returns:
        bool: True if all numbers in the list are prime, False otherwise
    """
    for num in numbers:
        # Handle edge cases
        if num <= 1:
            return False
            
        # Check if the number is prime
        is_prime = True
        for n in range(2, int(num**0.5) + 1):
            if num % n == 0:
                is_prime = False
                break
                
        # If any number is not prime, return False
        if not is_prime:
            return False
            
    # All numbers are prime
    return True