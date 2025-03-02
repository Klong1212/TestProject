def staircase(n, display="#"):
    """
    Prints a staircase pattern of height n using the specified display character.
    
    Args:
        n: A positive integer representing the height of the staircase (0 < n <= 30)
        display: A character to use for building the staircase (default: "#")
    
    Returns:
        None (prints the staircase pattern)
    """
    # Input validation
    if not (0 < n <= 30):
        raise ValueError("Height must be between 1 and 30 inclusive")
    
    if len(display) != 1:
        raise ValueError("Display character must be a single character")
    
    # Build and print the staircase
    for i in range(1, n + 1):
        print(display * i)
        
print(staircase(6))  # 6 ชั้น