import sys
from os.path import exists

from utils.input import get_file_content
from utils.log import output_identified_tokens, output_symbol_table

from lexer.lex import lex_content


# command line arguments passed to compiler script
INPUT_ARGS = sys.argv[1:]


# doing lexing process and outputing the results
def operate_lexing(file_address: str):
    # generating output addresses for symbol table file and all tokens file
    address_component = file_address[:file_address.rindex(".")]
    output_addresses = dict(
        symbol_table= f"{address_component}_output_symbol_table.txt",
        all_tokens= f"{address_component}_output_all_tokens.txt",
    )

    # reading file content and doing lex operation on it
    file_content = get_file_content(file_address)
    identified_tokens, symbol_table = lex_content(file_content)

    # saving results to a file
    output_identified_tokens(identified_tokens, True, output_addresses["all_tokens"])
    output_symbol_table(symbol_table, True, output_addresses["symbol_table"])


# main section
if __name__ == "__main__":
    # iterating over all path arguments passed
    for input_arg in INPUT_ARGS:
        # doing compilation if the input path is valid
        if exists(input_arg):
            operate_lexing(input_arg) # lexer operations

    if len(input_arg) > 0:
        print("\n\nCompiler job is done successfully!!!")
    else:
        print("Error: no path arguments passed!!!")
        