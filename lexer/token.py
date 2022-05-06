from enum import Enum

DATA_TYPES = ["CHAR", "STRING", "INT", "DOUBLE", "FLOAT", "LONG", "SHORT", "BOOLEAN"]
LITERALS_LIST = ["CHARACTER_LITERAL", "STRING_LITERAL", "INT_CONSTANT", "DOUBLE_CONSTANT", "TRUE", "FALSE", "NULL"]

class Type(Enum):
    # these patterns will be ignored
    SPACE = "( ).*"
    TAB = "(\\t).*"
    NEW_LINE = "(\\n).*"
    BLOCK_COMMENT = "(/\\*.*?\\*/).*"
    LINE_COMMENT = "(//(.*?)[\r$]?\n).*"

    # special syntax characters
    COMMA = "(,).*"
    SEMICOLON = "(;).*"
    OPEN_PAREN = "(\\().*"
    CLOSE_PAREN = "(\\)).*"
    OPEN_CURLY_BRACE = "(\\{).*"
    CLOSE_CURLY_BRACE = "(\\}).*"
    OPEN_BRACE = "(\\[).*"
    CLOSE_BRACE = "(\\]).*"

    # keywords
    VOID = "\\b(void)\\b.*"
    INT = "\\b(int)\\b.*"
    DOUBLE = "\\b(int|double)\\b.*"
    PUBLIC = "\\b(public)\\b.*"
    PRIVATE = "\\b(private)\\b.*"
    RETURN = "\\b(return)\\b.*"
    NEW = "\\b(new)\\b.*"
    CLASS = "\\b(class)\\b.*"
    IF = "\\b(if)\\b.*"
    ELSE = "\\b(else)\\b.*"
    WHILE = "\\b(while)\\b.*"
    STATIC = "\\b(static)\\b.*"
    STRING = "\\b(String)\\b.*"
    CHAR = "\\b(char)\\b.*"
    FINAL = "\\b(final)\\b.*"
    ABSTRACT = "\\b(abstract)\\b.*"
    CONTINUE = "\\b(continue)\\b.*"
    FOR = "\\b(for)\\b.*"
    SWITCH = "\\b(switch)\\b.*"
    ASSERT = "\\b(assert)\\b.*"
    DEFAULT = "\\b(default)\\b.*"
    GOTO = "\\b(goto)\\b.*"
    PACKAGE = "\\b(package)\\b.*"
    SYNCHRONIZED = "\\b(synchronized)\\b.*"
    BOOLEAN = "\\b(boolean)\\b.*"
    DO = "\\b(do)\\b.*"
    THIS = "\\b(this)\\b.*"
    BYTE = "\\b(byte)\\b.*"
    IMPORT = "\\b(import)\\b.*"
    THROWS = "\\b(throws)\\b.*"
    BREAK = "\\b(break)\\b.*"
    IMPLEMENTS = "\\b(implements)\\b.*"
    PROTECTED = "\\b(protected)\\b.*"
    THROW = "\\b(throw)\\b.*"
    CASE = "\\b(case)\\b.*"
    ENUM = "\\b(enum)\\b.*"
    INSTANCEOF = "\\b(instanceof)\\b.*"
    TRANSIENT = "\\b(transient)\\b.*"
    CATCH = "\\b(catch)\\b.*"
    EXTENDS = "\\b(extends)\\b.*"
    SHORT = "\\b(short)\\b.*"
    TRY = "\\b(try)\\b.*"
    INTERFACE = "\\b(interface)\\b.*"
    FINALLY = "\\b(finally)\\b.*"
    LONG = "\\b(long)\\b.*"
    STRICTFP = "\\b(strictfp)\\b.*"
    VOLATILE = "\\b(volatile)\\b.*"
    CONST = "\\b(const)\\b.*"
    FLOAT = "\\b(float)\\b.*"
    NATIVE = "\\b(native)\\b.*"
    super = "\\b(super)\\b.*"

    # constants and literals
    DOUBLE_CONSTANT = "\\b(\\d{1,9}\\.\\d{1,32})\\b.*"
    INT_CONSTANT = "\\b(\\d{1,9})\\b.*"
    FALSE = "\\b(false)\\b.*"
    TRUE = "\\b(true)\\b.*"
    NULL = "\\b(null)\\b.*"

    # operators
    POINT = "(\\.).*"
    PLUS = "(\\+{1}).*"
    MINUS = "(\\-{1}).*"
    MULTIPLY = "(\\*).*"
    DIVIDE = "(/).*"
    EQUAL = "(==).*"
    ASSIGNMENT = "(=).*"
    NOT_EQUAL = "(\\!=).*"
    CLOSE_CARET = "(>).*"
    OPEN_CARET = "(<).*"

    # identifiers, string and character literals
    IDENTIFIER = "\\b([a-zA-Z]{1}[0-9a-zA-Z_]{0,31})\\b.*"
    STRING_LITERAL = '\"(\\.|[^\\\n"])*\"'
    STRING_LITERAL_INVALID = r'\"(.[^\n\"]*)'
    CHARACTER_LITERAL = r"\'(.?|\\.)\'"
    CHARACTER_LITERAL_INVALID = r"\'(.[^\'\n]+)[\n\']"


# used for abstracting structure of a token which is found in data string
class Token:
    def __init__(self, begin: int, end: int, value: str, type: str):
        self.begin = begin
        self.end = end
        self.value = value
        self.type = type

    # string representation
    def __str__(self):
        return self.type.name + '   ' + self.value

    __repr__ = __str__
