from pprint import pprint
from beautifultable import BeautifulTable


# is used to save string data to a file
def save_file(path: str, content: str):
    file = open(path, "w+")
    file.write(content)
    file.close()
 

# generates string based table for all of identified tokens and saves them if needed
def output_identified_tokens(
    identified_tokens: list, 
    save_mode: bool = False,
    save_path: str = ""
) -> str:
    table = BeautifulTable()
    table.columns.header = ["id", "type", "value", "lineNumber", "index"]

    for token in identified_tokens:
        table.rows.append([identified_tokens.index(token) + 1, token.type, token.value, token.lineno, token.index])

    generated_string = str(table)

    print(f"\n\nAll Identified Tokens:\n{generated_string}")

    if save_mode:
        save_file(save_path, generated_string)

    return generated_string


# generates string based table for symbol table data and saves them if needed
def output_symbol_table(
    symbol_table: dict,
    save_mode: bool = False,
    save_path: str = ""
) -> str:
    table = BeautifulTable()
    table.columns.header = ["name", "type", "value", "lineNumber", "index"]

    for _, token in symbol_table.symbols.items():
        table.rows.append([token[key] for key in table.columns.header])

    generated_string = str(table)

    print(f"\n\nSymbol Table:\n{generated_string}")

    if save_mode:
        save_file(save_path, generated_string)

    return generated_string


# generates string based symbol stack data and saves them if needed
def output_symbol_parsing_stack(
    parse_stack_content: str,
    save_mode: bool = False,
    save_path: str = ""
) -> str:

    generated_string = parse_stack_content

    print(f"\n\nParse Stack Content:\n{generated_string}")

    if save_mode:
        save_file(save_path, generated_string)

    return generated_string


# generates string based parse tree data and saves them if needed
def output_parse_tree(
    parse_tree: tuple,
    save_mode: bool = False,
    save_path: str = ""
) -> str:
    generated_string = str(parse_tree)

    print("\n\nParse Tree Content:")
    pprint(parse_tree)

    if save_mode:
        save_file(save_path, generated_string)

    return generated_string
