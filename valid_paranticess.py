"""Valid Parentheses

Write is_valid(s) to return True if all brackets close correctly, otherwise False.

The string contains only: ( ) [ ] { }

Rules:
* Match each opening bracket with the same type.
* Close brackets in the correct order.
* An empty string is valid.

Examples:
is_valid("()") → True
is_valid("()[]{}") → True
is_valid("(]") → False
is_valid("([)]") → False
is_valid("{[]}") → True
is_valid("((") → False

Hint: when you see a closing bracket, which opening bracket should it match?"""

def is_valid(s):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}'
    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return bracket_map
            else:
                stack.append(char)
    return not stack

print(is_valid("()"))

