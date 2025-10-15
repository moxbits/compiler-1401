from sly import Parser
from lex.lexer import MiniCLexer
from utils.logger import SymbolStackLogger


# Mini C Parser class
# this class is responsible for parsing the input data based on
# sly library LALR algorithm
class MiniCParser(Parser):
    # parser constructor
    # it receives the symbol table object and generates it
    # while doing the parsing operations
    def __init__(self, symbolTable):
        super().__init__()
        self.symbolTable = symbolTable

    # Get list of defined tokens form our own defined Lexer class
    tokens = MiniCLexer.tokens

    # Sets compiler parsing debug file location
    debugfile = 'parser.out'

    # Adjusts terminals precedence
    precedence = (
        ('nonassoc', EQUAL, LESS_EQUAL, GREATER_EQUAL,
         NOT_EQUAL, GREATER_THAN, LESS_THAN),
        ('left', PLUS, MINUS),
        ('left', MULTIPLY, DIVIDE),
    )

    # first grammer rule
    # main function detection rule
    @_('VOID MAIN OPEN_PAREN CLOSE_PAREN OPEN_BRACE statements_block CLOSE_BRACE')
    def main_function_definition(self, p):
        return ('main_function_definition', p.statements_block)

    # a block of statements that contains a set of statements
    @_("statements_set")
    def statements_block(self, p):
        return p.statements_set

    # <empty> rule for blocks of statements because it can be null
    @_("")
    def statements_block(self, p):
        return []

    # statements handler
    # rule of containing one or many statements in a set of statements
    @_('statements_set statement')
    def statements_set(self, p):
        p.statements_set.append(p.statement)
        return p.statements_set

    # <empty> rule for sets of statements because it can be null
    @_('')
    def statements_set(self, p):
        return []

    # different valid statement rules
    # variable declarations are statements
    @_('variable_declaration')
    def statement(self, p):
        return p.variable_declaration

    # variable assignments are statements
    @_('assignment')
    def statement(self, p):
        return p.assignment

    # if blocks of code are statements
    @_('if_statement')
    def statement(self, p):
        return p.if_statement

    # while loop blocks of code are statements
    @_('while_loop_statement')
    def statement(self, p):
        return p.while_loop_statement

    # for loop blocks of code are statements
    @_('for_loop_statement')
    def statement(self, p):
        return p.for_loop_statement

    # switch case blocks of code are statements
    @_('switch_statement')
    def statement(self, p):
        return p.switch_statement

    # line of code containing a return keyword is a statement
    @_('return_statement')
    def statement(self, p):
        return p.return_statement

    # line of code containing a break keyword is a statement
    @_('break_statement')
    def statement(self, p):
        return p.break_statement

    # line of code containing a continue keyword is a statement
    @_('continue_statement')
    def statement(self, p):
        return p.continue_statement

    # increament and decreament are statements
    @_('increament_statement')
    def statement(self, p):
        return p.increament_statement

    @_('decreament_statement')
    def statement(self, p):
        return p.decreament_statement

    # for loop rules
    # for loop structure without curly braces and with only a single statement in front of it
    # for (part1; part2; part3) statement;
    @_('FOR OPEN_PAREN for_setup_1 SEMICOLON for_setup_2 SEMICOLON for_setup_3 CLOSE_PAREN statement')
    def for_loop_statement(self, p):
        return ('for_loop', ('for_loop_setup', p.for_setup_1, p.for_setup_2, p.for_setup_3), p.statement)

    # for loop with its complete structure
    # for (part1; part2; part3) { statements_block }
    @_('FOR OPEN_PAREN for_setup_1 SEMICOLON for_setup_2 SEMICOLON for_setup_3 CLOSE_PAREN OPEN_BRACE statements_block CLOSE_BRACE')
    def for_loop_statement(self, p):
        return ('for_loop', ('for_loop_setup', p.for_setup_1, p.for_setup_2, p.for_setup_3), p.statements_block)

    # for loop first setup part
    # when for loop first setup part is a variable declaration statement
    @_('variable_dec_expression')
    def for_setup_1(self, p):
        return ("for_setup_1", p.variable_dec_expression)

    # when for loop first setup part is a variable assignment statement
    @_('assignment_expression')
    def for_setup_1(self, p):
        return ("for_setup_1", p.assignment_expression)

    # when for loop first setup part is empty
    @_('')
    def for_setup_1(self, p):
        return []

    # for loop second setup part
    # for loop setup second part is a expression
    @_('expression')
    def for_setup_2(self, p):
        return ("for_setup_2", p.expression)

    # for loop setup second part can also be empty
    @_('')
    def for_setup_2(self, p):
        return []

    # for loop third setup part
    # for loop third setup part can be a increament expression
    @_('increament_expression')
    def for_setup_3(self, p):
        return ("for_setup_3", p.increament_expression)

    # for loop third setup part can be a decreament expression
    @_('decreament_expression')
    def for_setup_3(self, p):
        return ("for_setup_3", p.decreament_expression)

    # for loop third setup part can be a empty
    @_('')
    def for_setup_3(self, p):
        return []

    # variable declaration grammer rules
    @_('variable_dec_expression SEMICOLON')
    def variable_declaration(self, p):
        return p.variable_dec_expression

    @_('DATA_TYPE IDENTIFIER ASSIGN expression')
    def variable_dec_expression(self, p):
        if (p.DATA_TYPE != p.expression[0]):
            return f'ERROR: Value does not match the type at line {p.lineno}'
        for token in self.symstack:
            if token.type == "IDENTIFIER":
                token_value = p.expression

                sym_token = {
                    'name': token.value,
                    'lineNumber': token.lineno,
                    'index': token.index,
                    'type': p.DATA_TYPE,
                    'value': 'UNDEFINED',
                }

                if len(token_value) == 2:
                    sym_token['value'] = token_value[1]

                if self.symbolTable.search(sym_token) == False:
                    self.symbolTable.insert(sym_token)
                else:
                    SymbolStackLogger.log(
                        f"ERROR: Variable already defined at line {p.lineno}\n\n")
                    return ("SYNTAX ERROR", "identifier is already defined!")

        return ('var', p.IDENTIFIER, p.expression)

    @_('DATA_TYPE IDENTIFIER')
    def variable_dec_expression(self, p):
        for token in self.symstack:
            if token.type == "IDENTIFIER":
                sym_token = {
                    'name': token.value,
                    'type': token.type,
                    'value': 'UNDEFINED',
                    'lineNumber': token.lineno,
                    'index': token.index
                }

                if self.symbolTable.search(sym_token) == False:
                    self.symbolTable.insert(sym_token)
                else:
                    SymbolStackLogger.log(
                        f"ERROR: Variable already defined at line {p.lineno}\n\n")
                    return ("SYNTAX ERROR", "identifier is already defined!")

        return ('var', p.IDENTIFIER)

    # assignment detection rules
    @_('assignment_expression SEMICOLON')
    def assignment(self, p):
        return p.assignment_expression

    @_('IDENTIFIER ASSIGN expression')
    def assignment_expression(self, p):
        for token in self.symstack:
            if token.type == "IDENTIFIER":
                if self.symbolTable.search(token) == False:
                    SymbolStackLogger.log(
                        f"ERROR: Variable is not defined at line {p.lineno}\n\n")
                    return ("SYNTAX ERROR", "identifier is not defined!")

        return ('=', p.IDENTIFIER, p.expression)

    @_('IDENTIFIER PLUS_ASSIGN expression')
    def assignment_expression(self, p):
        for token in self.symstack:
            if token.type == "IDENTIFIER":
                if self.symbolTable.search(token) == False:
                    SymbolStackLogger.log(
                        f"ERROR: Variable is not defined at line {p.lineno}\n\n")
                    return ("SYNTAX ERROR", "identifier is not defined!")

        return ('+=', p.IDENTIFIER, p.expression)

    @_('IDENTIFIER MINUS_ASSIGN expression')
    def assignment_expression(self, p):
        for token in self.symstack:
            if token.type == "IDENTIFIER":
                if self.symbolTable.search(token) == False:
                    SymbolStackLogger.log(
                        f"ERROR: Variable is not defined at line {p.lineno}")
                    return ("SYNTAX ERROR", "identifier is not defined!")

        return ('-=', p.IDENTIFIER, p.expression)

    @_('IDENTIFIER MULT_ASSIGN expression')
    def assignment_expression(self, p):
        for token in self.symstack:
            if token.type == "IDENTIFIER":
                if self.symbolTable.search(token) == False:
                    SymbolStackLogger.log(
                        f"ERROR: Variable is not defined at line {p.lineno}")
                    return ("SYNTAX ERROR", "identifier is not defined!")

        return ('*=', p.IDENTIFIER, p.expression)

    @_('IDENTIFIER DIV_ASSIGN expression')
    def assignment_expression(self, p):
        for token in self.symstack:
            if token.type == "IDENTIFIER":
                if self.symbolTable.search(token) == False:
                    SymbolStackLogger.log(
                        f"ERROR: Variable is not defined at line {p.lineno}")
                    return ("SYNTAX ERROR", "identifier is not defined!")

        return ('/=', p.IDENTIFIER, p.expression)

    @_('IDENTIFIER MOD_ASSIGN expression')
    def assignment_expression(self, p):
        for token in self.symstack:
            if token.type == "IDENTIFIER":
                if self.symbolTable.search(token) == False:
                    SymbolStackLogger.log(
                        f"ERROR: Variable is not defined at line {p.lineno}")
                    return ("SYNTAX ERROR", "identifier is not defined!")

        return ('%=', p.IDENTIFIER, p.expression)

    @_('increament_expression SEMICOLON')
    def increament_statement(self, p):
        return p.increament_expression

    @_('decreament_expression SEMICOLON')
    def decreament_statement(self, p):
        return p.decreament_expression

    # continue keyword statement rule
    @_('CONTINUE SEMICOLON')
    def continue_statement(self, p):
        return ('continue', )

    # break keyword statement rule
    @_('BREAK SEMICOLON')
    def break_statement(self, p):
        return ('break', )

    # return statement rules
    @_('RETURN expression SEMICOLON')
    def return_statement(self, p):
        return ('return', p.expression)

    @_('RETURN SEMICOLON')
    def return_statement(self, p):
        return ('return', )

    # if and else statements rules
    # if without curly braces and with only a single statement
    @_('IF OPEN_PAREN expression CLOSE_PAREN statement')
    def if_statement(self, p):
        return ('if', p.expression, ('branch', p.statement))

    # if with its complete form
    @_('IF OPEN_PAREN expression CLOSE_PAREN OPEN_BRACE statements_block CLOSE_BRACE else_statement')
    def if_statement(self, p):
        return ('if', p.expression, ('branch', p.statements_block), p.else_statement)

    # else if grammer rule
    @_('ELSE IF OPEN_PAREN expression CLOSE_PAREN OPEN_BRACE statements_block CLOSE_BRACE else_statement')
    def else_statement(self, p):
        return ('else if', p.expression, ('branch', p.statements_block), p.else_statement)

    # else grammer rule
    @_('ELSE OPEN_BRACE statements_block CLOSE_BRACE')
    def else_statement(self, p):
        return ('else', ('branch', p.statements_block))

    # we can have no else if or else blocks
    @_('')
    def else_statement(self, p):
        return []

    # switch statement rules
    @_('SWITCH OPEN_PAREN IDENTIFIER CLOSE_PAREN OPEN_BRACE switch_block CLOSE_BRACE')
    def switch_statement(self, p):
        return ('switch', p.IDENTIFIER, p.switch_block)

    # switch block containing one or multiple case blocks
    @_('CASE literal COLON statements_block switch_block')
    def switch_block(self, p):
        return ('case', p.statements_block, p.switch_block)

    # switch block can contain a default block
    @_('DEFAULT COLON statements_block')
    def switch_block(self, p):
        return ('default', p.statements_block)

    # switch block can contain a statement block
    @_('statements_block')
    def switch_block(self, p):
        return p.statements_block

    # switch block can be empty
    @_("")
    def switch_block(self, p):
        return []

    # while loops rule
    # while (expression) { statements_block }
    @_('WHILE OPEN_PAREN expression CLOSE_PAREN OPEN_BRACE statements_block CLOSE_BRACE')
    def while_loop_statement(self, p):
        return ('while_loop', ('while_loop_setup', p.expression), p.statements_block)

    # expressions and their rules
    # separated expressions using comma
    @_('expression COMMA expression')
    def expression(self, p):
        return (p.expression0, p.expression1)

    # addition operator between expressions makes a valid expressions
    @_('expression PLUS expression')
    def expression(self, p):
        return ("+", p.expression0, p.expression1)

    # subtraction operator between expressions makes a valid expressions
    @_('expression MINUS expression')
    def expression(self, p):
        return ("-", p.expression0, p.expression1)

    # multiply operator between expressions makes a valid expressions
    @_('expression MULTIPLY expression')
    def expression(self, p):
        return ("*", p.expression0, p.expression1)

    # divide operator between expressions makes a valid expressions
    @_('expression DIVIDE expression')
    def expression(self, p):
        return ("/", p.expression0, p.expression1)

    # mod operator between expressions makes a valid expressions
    @_('expression MOD expression')
    def expression(self, p):
        return ("%", p.expression0, p.expression1)

    # less than expressions are valid expressions
    @_('expression LESS_THAN expression')
    def expression(self, p):
        return ("<", p.expression0, p.expression1)

    # less or equal expressions are valid expressions
    @_('expression LESS_EQUAL expression')
    def expression(self, p):
        return ("<=", p.expression0, p.expression1)

    # greater than expressions are valid expressions
    @_('expression GREATER_THAN expression')
    def expression(self, p):
        return (">", p.expression0, p.expression1)

    # greater or equal expressions are valid expressions
    @_('expression GREATER_EQUAL expression')
    def expression(self, p):
        return (">=", p.expression0, p.expression1)

    # equality expressions are valid expressions
    @_('expression EQUAL expression')
    def expression(self, p):
        return ("==", p.expression0, p.expression1)

    # not equal expressions are valid expressions
    @_('expression NOT_EQUAL expression')
    def expression(self, p):
        return ("!=", p.expression0, p.expression1)

    # and expressions are valid expressions
    @_('expression AND expression')
    def expression(self, p):
        return ("and", p.expression0, p.expression1)

    # or expressions are valid expressions
    @_('expression OR expression')
    def expression(self, p):
        return ("or", p.expression0, p.expression1)

    # not expressions are valid expressions
    @_('NOT expression')
    def expression(self, p):
        return ('not', p.expression)

    # expressions can be wrapped in parenthesis
    @_('OPEN_PAREN expression CLOSE_PAREN')
    def expression(self, p):
        return p.expression

    # expressions can be increament operations
    @_('increament_expression')
    def expression(self, p):
        return p.increament_expression

    # expressions can be decreament operations
    @_('decreament_expression')
    def expression(self, p):
        return p.decreament_expression

    # increament expressions rules
    @_('IDENTIFIER INCREAMENT')
    def increament_expression(self, p):
        return ('post_increament', p.IDENTIFIER)

    @_('INCREAMENT IDENTIFIER')
    def increament_expression(self, p):
        return ('pre_increament', p.IDENTIFIER)

    # decreament expressions rules
    @_('IDENTIFIER DECREAMENT')
    def decreament_expression(self, p):
        return ('post_decreament', p.IDENTIFIER)

    @_('DECREAMENT IDENTIFIER')
    def decreament_expression(self, p):
        return ('pre_decreament', p.IDENTIFIER)

    # expressions can be identifiers
    @_('IDENTIFIER')
    def expression(self, p):
        return p.IDENTIFIER

    # expressions can be literals
    @_('literal')
    def expression(self, p):
        return p.literal

    # literals
    # boolean values are literals
    @_('BOOLEAN')
    def literal(self, p):
        return ('boolean', p.BOOLEAN)

    # float values are literals
    @_('FLOAT')
    def literal(self, p):
        return ('float', p.FLOAT)

    # float values are literals
    @_('INTEGER')
    def literal(self, p):
        return ('int', p.INTEGER)

    # character values are literals
    @_('CHARACTER')
    def literal(self, p):
        return ('char', p.CHARACTER)

    # string values are literals
    @_('STRING')
    def literal(self, p):
        return ('String', p.STRING)

    # parser error handler
    # this will print where did the error happened and near which character it happened
    def error(self, token):
        print(
            f'SYNTAX ERROR at line {token.lineno} near character "{token.value}" ')
        SymbolStackLogger.log(
            f"SYNTAX ERROR at line {token.lineno} near character '{token.value}' ")
