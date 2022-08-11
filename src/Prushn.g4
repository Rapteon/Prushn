grammar Prushn;

program: question+;
question: QUESTION_BEGIN text QUESTION_MARK NEWLINE;

text: (WORD SPACE)+;
 
QUESTION_BEGIN: 'Q' NUMBER '.' SPACE;
NEWLINE: ('\r'?'\n')+;
QUESTION_MARK: '?';
fragment OPERATOR: '/' | '*' | '+' | '-' ;
fragment EXPONENT: '^';
fragment MONEY: '$' | '₹';
fragment BLOCK: '(' | ')' | '[' | ']' | '{' | '}';
fragment OTHER: '!' | '@' | '#' | '<' | '>' | '/' | ',' | '.' | '|' | '\\' | '=' | '_' | '`' | '~';
SPECIAL: OPERATOR | EXPONENT | MONEY | BLOCK | OTHER ;

ALPHABET: [a-zA-Z];
LETTER: ALPHABET | SPECIAL;
DIGIT: [0-9];
NUMBER: ([0-9]+)? '.'? DIGIT+;
WORD: (LETTER | NUMBER | SPECIAL)+;
SPACE: ' '+;