def reverse_string(s):
    stack = []          # Initialize an empty stack
    reversed_str = ""   # Result string
    
    # Push each character into the stack
    for char in s:
        stack.append(char)
    
    # Pop characters to build the reversed string
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str

# Test
print(reverse_string("interview"))  # Output: "weivretni"
