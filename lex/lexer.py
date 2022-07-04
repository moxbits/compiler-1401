from sly import Lexer


# our defined lexer class based on sly Lexer class
# this will do all of our lexing operations and
# all of our tokens are defined here
class MiniJAVALexer(Lexer):
    # List of valid tokens
    tokens = {
        # identifiers
        IDENTIFIER,

        # main function tokens
        MAIN,
        VOID,
        RETURN,

        # flow control tokens
        IF,
        ELSE,
        SWITCH,
        CASE,
        DEFAULT,
        FOR,
        WHILE,
        BREAK,
        CONTINUE,

        # data type and literals tokens
        DATA_TYPE,
        INTEGER,
        STRING,
        CHARACTER,
        BOOLEAN,
        FLOAT,

        # arithmetic operators tokens
        INCREAMENT,
        DECREAMENT,
        PLUS,
        MINUS,
        DIVIDE,
        MULTIPLY,
        MOD,

        # logical operators token
        NOT,
        OR,
        AND,
        EQUAL,
        LESS_EQUAL,
        GREATER_EQUAL,
        NOT_EQUAL,
        GREATER_THAN,
        LESS_THAN,

        # assignment operators
        PLUS_ASSIGN,
        MINUS_ASSIGN,
        MULT_ASSIGN,
        DIV_ASSIGN,
        MOD_ASSIGN,
        ASSIGN,

        # special characters
        OPEN_PAREN,
        CLOSE_PAREN,
        OPEN_BRACE,
        CLOSE_BRACE,
        COMMA,
        COLON,
        SEMICOLON
    }

    # Ignore whitespaces, tabs and comments
    ignore = '[ \t]'
    ignore_comments = r'\/\/.*'
    ignore_multiline_comments = r'\/\*[^*]*\*+(?:[^/*][^*]*\*+)*\/'

    # Ignore new lines and count line numbers
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    # special tokens that represent special characters
    COMMA = r','
    COLON = r':'
    SEMICOLON = r';'
    OPEN_BRACE = r'{'
    CLOSE_BRACE = r'}'
    OPEN_PAREN = r'\('
    CLOSE_PAREN = r'\)'

    # Relation operations
    EQUAL = r'\=\='
    NOT_EQUAL = r'\!\='
    GREATER_EQUAL = r'>='
    LESS_EQUAL = r'<='
    GREATER_THAN = r'>'
    LESS_THAN = r'<'

    # assignment operators
    PLUS_ASSIGN = r'\+\='
    MINUS_ASSIGN = r'\-\='
    MULT_ASSIGN = r'\*\='
    DIV_ASSIGN = r'\/\='
    MOD_ASSIGN = r'\%\='
    ASSIGN = r'\='

    # arithmetic operators
    INCREAMENT = r'\+\+'
    DECREAMENT = r'\-\-'
    PLUS = r'\+'
    MINUS = r'\-'
    MULTIPLY = r'\*'
    DIVIDE = r'\/'
    MOD = r'\%'

    # Logical operators
    AND = r'\&\&'
    OR = r'\|\|'
    NOT = r'\!(?!\W)'

    # String and Character literals
    CHARACTER = r'\'(.?|\\.)\''
    STRING = r'(\".*\")'

    # Identifiers and keywords
    IDENTIFIER = r'[a-zA-Z_]+[a-zA-Z0-9_]*'
    IDENTIFIER['if'] = IF
    IDENTIFIER['else'] = ELSE
    IDENTIFIER['for'] = FOR
    IDENTIFIER['while'] = WHILE
    IDENTIFIER['switch'] = SWITCH
    IDENTIFIER['case'] = CASE
    IDENTIFIER['break'] = BREAK
    IDENTIFIER['void'] = VOID
    IDENTIFIER['main'] = MAIN
    IDENTIFIER['default'] = DEFAULT
    IDENTIFIER['continue'] = CONTINUE
    IDENTIFIER['return'] = RETURN

    # different data types
    IDENTIFIER['int'] = DATA_TYPE
    IDENTIFIER['long'] = DATA_TYPE
    IDENTIFIER['float'] = DATA_TYPE
    IDENTIFIER['double'] = DATA_TYPE
    IDENTIFIER['char'] = DATA_TYPE
    IDENTIFIER['String'] = DATA_TYPE
    IDENTIFIER['boolean'] = DATA_TYPE

    # boolean values
    IDENTIFIER['true'] = BOOLEAN
    IDENTIFIER['false'] = BOOLEAN

    # Floating point numbers token
    # it will return a token with a float number value
    @_(r'-?\d+\.\d+')
    def FLOAT(self, t):
        t.value = float(t.value)
        return t

    # Integer numbers token
    # it will return a token with a integer number value
    @_(r'-?\d+')
    def INTEGER(self, t):
        t.value = int(t.value)
        return t

    # specify number of column for characters
    def find_column(self, text, token):
        last_cr = text.rfind('\n', 0, token.index)
        if last_cr < 0:
            last_cr = 0
        column = (token.index - last_cr) + 1
        return column

    # Simple error handling
    def error(self, t):
        print(f'ERROR! Line {self.lineno}: Bad Character {t.value[0]}')
        # Move on to next characters
        self.index += 1
