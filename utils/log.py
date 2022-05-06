from beautifultable import BeautifulTable

from utils.types import SymbolTableData, TokensList


# is used to save string data to a file
def save_file(path: str, content: str):
    file = open(path, "w+")
    file.write(content)
    file.close()
 

# generates string based table for all of identified tokens and saves them if needed
def output_identified_tokens(
    identified_tokens: TokensList, 
    save_mode: bool = False,
    save_path: str = ""
) -> str:
    table = BeautifulTable()
    table.columns.header = ["id", "type", "value"]

    for token in identified_tokens:
        table.rows.append([identified_tokens.index(token) + 1, token.type.name, token.value])

    generated_string = str(table)

    print(f"\n\nAll Identified Tokens:\n{generated_string}")

    if save_mode:
        save_file(save_path, generated_string)

    return generated_string


# generates string based table for symbol table data and saves them if needed
def output_symbol_table(
    symbol_table: SymbolTableData,
    save_mode: bool = False,
    save_path: str = ""
) -> str:
    table = BeautifulTable()
    table.columns.header = ["id", "name", "type", "value"]

    for _, token in symbol_table.items():
        table.rows.append([token[key] for key in table.columns.header])

    generated_string = str(table)

    print(f"\n\nSymbol Table:\n{generated_string}")

    if save_mode:
        save_file(save_path, generated_string)

    return generated_string
