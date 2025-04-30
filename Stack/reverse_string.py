def reverse_string(text):
    stack = list(text)  # Push all characters to stack
    reversed_text = ""

    while stack:
        reversed_text += stack.pop()  # Pop one by one

    return reversed_text

print(reverse_string("Ajinesh"))  # Output: hsenijA
