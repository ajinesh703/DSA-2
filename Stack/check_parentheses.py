def is_balanced(expression):
    stack = []
    for char in expression:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

print(is_balanced("(a+b)*(c+d)"))   # True
print(is_balanced("((a+b)"))        # False
