import re

def is_valid_expression(expression):
    # Check for unsupported characters
    if not re.match(r'^[\d\s+\-*/()]+$', expression):
        return False
    return True

def check_unbalanced_parentheses(expression):
    # Check for unbalanced parentheses
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

def check_operand_error(expression):
    # Check for operand errors
    tokens = re.split(r'(\D)', expression)
    last_was_operator = True  # Assume we start with an operator for validation purposes
    for token in tokens:
        token = token.strip()
        if token == '':
            continue
        if token.isdigit():
            last_was_operator = False
        elif token in '+-*/':
            if last_was_operator:
                return True
            last_was_operator = True
        elif token in '()':
            continue
        else:
            return True
    return last_was_operator

def evaluate_expression(expression):
    try:
        # Evaluate the expression
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except SyntaxError:
        return "Error: Operand error"

def main():
    while True:
        expression = input("Enter an expression to evaluate or 'q' to quit): ").strip()
        if expression.lower() == 'q':
            break
        
        if not is_valid_expression(expression):
            print("Error: Unsupported character in expression")
            continue

        if not check_unbalanced_parentheses(expression):
            print("Error: Unbalanced parentheses")
            continue

        if check_operand_error(expression):
            print("Error: Operand error")
            continue

        result = evaluate_expression(expression)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
