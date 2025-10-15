import sys
from os.path import exists

from utils.symbolTable import SymbolTable

from lex.lexer import MiniCLexer
from lex.generator import generate_tokens_list

from parse.parser import MiniCParser
from parse.parsetree import parse_tree_generator

from utils.input import get_file_content
from utils.logger import SymbolStackLogger
from utils.output import output_identified_tokens, output_symbol_parsing_stack, output_parse_tree, output_symbol_table


# command line arguments passed to compiler script
INPUT_ARGS = sys.argv[1:]


# doing lexing and parsing processes and outputing the results
def operate_compilation(file_address: str):
    # generating symbol table instance
    symbol_table = SymbolTable()

    # generating lexer instance
    lexer = MiniCLexer()

    # generating parser instance
    parser = MiniCParser(symbol_table)

    # generating output addresses for symbol table file and all tokens file
    address_component = file_address[:file_address.rindex(".")]
    output_addresses = dict(
        symbol_table=f"{address_component}_output_symbol_table.txt",
        all_tokens=f"{address_component}_output_all_tokens.txt",
        symbol_parsing_stack=f"{address_component}_output_parsing_stack.txt",
        parsing_tree_stack=f"{address_component}_output_parsing_tree.txt",
    )

    # reading file content and doing lex and parse operations on it
    file_content = get_file_content(file_address)

    identified_tokens = generate_tokens_list(lexer.tokenize(file_content))
    parse_tree_nodes = parser.parse(lexer.tokenize(file_content))
    parse_tree = parse_tree_generator(parse_tree_nodes)

    # printing and saving results to a file
    output_identified_tokens(identified_tokens, True,
                             output_addresses["all_tokens"])
    output_symbol_parsing_stack(
        SymbolStackLogger.stack_content_str, True, output_addresses["symbol_parsing_stack"])
    output_parse_tree(parse_tree, True, output_addresses["parsing_tree_stack"])
    output_symbol_table(symbol_table, True, output_addresses["symbol_table"])


# main section
if __name__ == "__main__":
    # iterating over all path arguments passed
    for input_arg in INPUT_ARGS:
        # doing compilation if the input path is valid
        if exists(input_arg):
            operate_compilation(input_arg)  # compiler operations
        else:
            print(f"Error: {input_arg} is not a valid file path!!!")

    if len(input_arg) > 0:
        print("\n\nCompiler job is done!!!")
    else:
        print("Error: no path arguments passed!!!")
