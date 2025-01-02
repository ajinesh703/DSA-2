def isPalindrome(x):
    # Negative numbers cannot be palindromes
    if x < 0:
        return False
    
    # Convert the number to a string
    x_str = str(x)
    
    # Check if the string is equal to its reverse
    return x_str == x_str[::-1]

# Example usage
x = 121
print("Is palindrome:", isPalindrome(x))  # Output: True
