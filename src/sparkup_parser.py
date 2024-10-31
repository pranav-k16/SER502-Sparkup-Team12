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
    'program : components'
    print("Program successfully parsed!")

def p_components(p):
    '''components : initialization computation FIN
                  | initialization FIN'''
    print("Components parsed")

def p_initialization(p):
    'initialization : LET IDENTIFIER ASSIGN expression'
    print(f"Initialization: {p[2]} = {p[4]}")

def p_computation(p):
    '''computation : statement computation
                   | statement'''
    print("Computation block parsed")

def p_statement(p):
    '''statement : print_statement
                 | assignment
                 | conditional
                 | loop
                 | initialization'''  # Add initialization to statement
    print("Statement parsed")

def p_print_statement(p):
    'print_statement : PRINT LPAREN expression RPAREN'
    print(f"Print statement: {p[3]}")

def p_assignment(p):
    'assignment : IDENTIFIER ASSIGN expression'
    print(f"Assignment: {p[1]} = {p[3]}")

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
                  | LPAREN expression RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = (p[2], p[1], p[3])  # Example tuple-based representation

def p_conditional(p):
    '''conditional : CHK LPAREN expression RPAREN LBRACE computation RBRACE
                   | CHK LPAREN expression RPAREN LBRACE computation RBRACE ALT LBRACE computation RBRACE'''
    print("Conditional statement parsed")

def p_loop(p):
    '''loop : WHILE LPAREN expression RPAREN LBRACE computation RBRACE
            | FOR LPAREN initialization SEMI expression SEMI assignment RPAREN LBRACE computation RBRACE'''
    print("Loop parsed")

# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}', line {p.lineno}")
    else:
        print("Syntax error at EOF")

# Building the parser
parser = yacc.yacc()
