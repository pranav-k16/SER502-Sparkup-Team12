grammar Sparkup;

// Parser rules
program        : components EOF ;
components     : initialization NEWLINE conclude* computation NEWLINE conclude* ;

initialization : 'let' variable_type variable_name '=' expression ;
computation    : operation+ ;
operation      : print_statement | assignment | conditional | loop ;

print_statement : 'print' '(' expression ')' ;
assignment      : variable_name '=' expression ;

expression     : intLiteral 
               | floatLiteral 
               | stringLiteral 
               | boolLiteral 
               | variable_name
               | arithmeticExpression
               | logicalExpression
               | ternaryExpression ;

arithmeticExpression : expression ( '+' | '-' | '*' | '/' ) expression ;
logicalExpression    : expression ( '&&' | '||' | '==' | '!=' | '>' | '<' | '>=' | '<=' ) expression
                     | 'not' expression ;
ternaryExpression    : expression '?' expression ':' expression ;

conditional  : 'if' '(' logicalExpression ')' '{' components '}' ('else' '{' components '}')? ;
loop         : 'while' '(' logicalExpression ')' '{' components '}'
             | 'for' '(' assignment ';' logicalExpression ';' assignment ')' '{' components '}' ;

conclude     : 'end' ;

// Lexer rules
variable_type : 'int' | 'float' | 'str' | 'bool' ;
variable_name : [a-z] [a-z0-9]* ;

intLiteral    : [0-9]+ ;
floatLiteral  : [0-9]+ '.' [0-9]+ ;
stringLiteral : '\'' .*? '\'' | '"' .*? '"' ;
boolLiteral   : 'true' | 'false' ;

NEWLINE       : '\r'? '\n' | '\r' ;
WS            : [ \t]+ -> skip ; // Skipping whitespaces
