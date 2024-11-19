import sys
import os

# Add the src folder to the Python path
script_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(script_dir, "../src")
sys.path.insert(0, src_path)

from sparkup_lexer import lexer
from sparkup_parser import parser

# Execution context (global variables)
execution_context = {}

def evaluate_expression(expression):
    """Evaluate an expression recursively."""
    if isinstance(expression, tuple):  # Binary or ternary operation
        op = expression[0]
        if op in ('+', '-', '*', '/', '<', '>', '<=', '>=', '==', '!='):
            left_val = evaluate_expression(expression[1])
            right_val = evaluate_expression(expression[2])
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            elif op == '*':
                return left_val * right_val
            elif op == '/':
                if right_val == 0:
                    raise ValueError("Division by zero")
                return left_val / right_val
            elif op == '<':
                return left_val < right_val
            elif op == '>':
                return left_val > right_val
            elif op == '<=':
                return left_val <= right_val
            elif op == '>=':
                return left_val >= right_val
            elif op == '==':
                return left_val == right_val
            elif op == '!=':
                return left_val != right_val
    elif isinstance(expression, str):  # Variable reference or string literal
        if expression in execution_context:
            return execution_context[expression]
        elif expression.startswith('"') and expression.endswith('"'):  # String literal
            return expression[1:-1]  # Remove quotes
        else:
            return expression  # Treat as plain string if not a variable
    else:  # Literal value (int, float, bool)
        return expression

def execute_statement(statement):
    """Execute a single parsed statement."""
    if statement['type'] == 'assignment':
        execution_context[statement['var']] = evaluate_expression(statement['value'])
    elif statement['type'] == 'print':
        value = evaluate_expression(statement['value'])
        print(value)
    elif statement['type'] == 'conditional':
        condition = evaluate_expression(statement['condition'])
        if condition:
            execute_program(statement['then'])
        elif 'else' in statement:
            execute_program(statement['else'])
    elif statement['type'] == 'while':
        while evaluate_expression(statement['condition']):
            execute_program(statement['body'])
    elif statement['type'] == 'for':
        execute_statement(statement['init'])
        while evaluate_expression(statement['condition']):
            execute_program(statement['body'])
            execute_statement(statement['update'])

def execute_program(program):
    """Execute the parsed program."""
    for statement in program:
        execute_statement(statement)

def load_skp_file(filename):
    """Load and read a .skp file."""
    if not filename.endswith('.skp'):
        raise ValueError("Invalid file extension. Please use a .skp file.")
    with open(filename, 'r') as file:
        code = file.read()
    return code

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: skp data/test.skp")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        code = load_skp_file(filename)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Tokenizing and parsing
    lexer.input(code)
    program = parser.parse(code)

    if program:
        print("Program parsed successfully. Executing...")
        execute_program(program)
    else:
        print("Parsing failed.")

