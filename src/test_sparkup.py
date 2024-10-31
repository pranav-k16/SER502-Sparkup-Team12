from sparkup_lexer import lexer
from sparkup_parser import parser

# Example Sparkup code to parse
code = '''
let x = 10
while (x > 0) {
    print("x is greater than 0")
    let x = x - 1
}
for (let y = 0; y < 5; y = y + 1) {
    print("Value of y: ")
    print(y)
}
end
'''

# Tokenize input
lexer.input(code)
for token in lexer:
    print(token)

# Parse the input code
parser.parse(code)
