# ==========================================
# PROGRAM 1: STACK OPERATIONS
# ==========================================

stack = []

# Push operation
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

# Pop operation
stack.pop()

print("After pop:", stack)

# Peek operation
print("Top element:", stack[-1])


# ==========================================
# PROGRAM 2: INFIX TO POSTFIX
# ==========================================

def precedence(op):
    if op == '+' or op == '-':
        return 1

    if op == '*' or op == '/':
        return 2

    return 0


def infix_to_postfix(expression):
    stack = []
    result = ""

    for char in expression:

        # If operand, add directly to result
        if char.isalnum():
            result += char

        # If opening bracket
        elif char == '(':
            stack.append(char)

        # If closing bracket
        elif char == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()

            stack.pop()

        # If operator
        else:
            while stack and precedence(stack[-1]) >= precedence(char):
                result += stack.pop()

            stack.append(char)

    # Pop remaining operators
    while stack:
        result += stack.pop()

    return result


# Test expression
expr = "A+B*C"

print("Postfix:", infix_to_postfix(expr))