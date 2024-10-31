import ply.lex as lex

# List of token names
tokens = (
    'INT', 'FLOAT', 'STRING', 'BOOL',
    'LET', 'PRINT', 'IF', 'ELSE', 'WHILE', 'FOR', 'END',
    'IDENTIFIER',
    'PLUS', 'MINUS', 'MULT', 'DIV',
    'EQUAL', 'NOTEQUAL', 'LESSTHAN', 'GREATERTHAN', 'LEQ', 'GEQ',
    'ASSIGN', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMI', 'QUESTION', 'COLON',
)

# Reserved words
reserved = {
    'let': 'LET',
    'print': 'PRINT',   
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'end': 'END',
    'true': 'BOOL',
    'false': 'BOOL'
}

# Regular expression rules for tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_EQUAL = r'=='
t_NOTEQUAL = r'!='
t_LESSTHAN = r'<'
t_GREATERTHAN = r'>'
t_LEQ = r'<='
t_GEQ = r'>='
t_ASSIGN = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMI = r';'
t_QUESTION = r'\?'
t_COLON = r':'

# Regular expressions for literals
def t_IDENTIFIER(t):
    r'[a-z][a-z0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # Remove quotes
    return t

# Ignored characters
t_ignore = ' \t'

# Define a rule for newlines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
