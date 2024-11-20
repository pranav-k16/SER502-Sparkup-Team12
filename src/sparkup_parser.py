import ply.yacc as yacc
from sparkup_lexer import tokens

# Defining precedence rules
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULT', 'DIV'),
    ('left', 'GREATERTHAN', 'LESSTHAN', 'GEQ', 'LEQ'),
    ('left', 'EQUAL', 'NOTEQUAL')
)

# Grammar rules
def p_program(p):
    '''program : components FIN
               | components'''
    p[0] = p[1] if len(p) > 2 else p[1]
    print("Program successfully parsed!")

def p_components(p):
    '''components : components statement
                  | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]
    print("Components parsed")

def p_initialization(p):
    '''statement : LET variable_type IDENTIFIER ASSIGN expression'''
    p[0] = {'type': 'assignment', 'var': p[3], 'value': p[5]}
    print(f"Initialization: {p[3]} = {p[5]}")

def p_variable_type(p):
    '''variable_type : IDENTIFIER'''
    if p[1] in {'int', 'float', 'str', 'bool'}:
        p[0] = p[1]
    else:
        raise ValueError(f"Unknown variable type '{p[1]}'")

def p_assignment(p):
    '''statement : IDENTIFIER ASSIGN expression'''
    p[0] = {'type': 'assignment', 'var': p[1], 'value': p[3]}
    print(f"Assignment: {p[1]} = {p[3]}")

def p_print_statement(p):
    '''statement : PRINT LPAREN expression RPAREN'''
    p[0] = {'type': 'print', 'value': p[3]}
    print(f"Print statement: {p[3]}")

def p_conditional(p):
    '''statement : CHK LPAREN expression RPAREN LBRACE components RBRACE
                 | CHK LPAREN expression RPAREN LBRACE components RBRACE ALT LBRACE components RBRACE'''
    if len(p) == 8:
        p[0] = {'type': 'conditional', 'condition': p[3], 'then': p[6]}
    elif len(p) == 12:
        p[0] = {
            'type': 'conditional',
            'condition': p[3],
            'then': p[6],
            'else': p[10]
        }
    print("Conditional statement parsed")

def p_loop(p):
    '''statement : WHILE LPAREN expression RPAREN LBRACE components RBRACE
                 | FOR LPAREN statement SEMI expression SEMI statement RPAREN LBRACE components RBRACE'''
    if p[1] == 'while':
        p[0] = {'type': 'while', 'condition': p[3], 'body': p[6]}
        print("While loop parsed")
    elif p[1] == 'for':
        p[0] = {
            'type': 'for',
            'init': p[3],
            'condition': p[5],
            'update': p[7],
            'body': p[10]
        }
        print("For loop parsed")

def p_expression(p):
    '''expression : INT
                  | FLOAT
                  | STRING
                  | BOOL
                  | IDENTIFIER
                  | expression PLUS expression
                  | expression MINUS expression
                  | expression MULT expression
                  | expression DIV expression
                  | expression GREATERTHAN expression
                  | expression LESSTHAN expression
                  | expression GEQ expression
                  | expression LEQ expression
                  | expression EQUAL expression
                  | expression NOTEQUAL expression
                  | expression AND expression
                  | expression OR expression
                  | NOT expression
                  | LPAREN expression RPAREN'''
    if len(p) == 2:  # Literal or identifier
        p[0] = p[1]
    elif len(p) == 4:  # Binary operation or parentheses
        if p[1] == '(':
            p[0] = p[2]
        else:
            p[0] = (p[2], p[1], p[3])
    elif len(p) == 3:  # Logical NOT operation
        p[0] = ('not', p[2])


def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}', line {p.lineno}")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

