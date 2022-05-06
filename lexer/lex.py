import re
from typing import Dict, Tuple

from utils.types import TokensList, SymbolTableData
from .token import Token, Type, DATA_TYPES, LITERALS_LIST 


# responsible for doing the lex operation on content of file
def lex_content(content: str) -> Tuple[TokensList, SymbolTableData]:
    index = 0
    tokens_list = list()
    content_length = len(content)

    # iterating over string data character by character to find tokens
    while index < content_length:
        # check for any token in current index
        result = get_token(content, index)

        # sets index to next position fo riteration
        index = result["next_position"]

        # token is found
        if result["token"]:
            # ignoring token if it is comments, tabs, spaces and new lines
            if result["token"].type not in [Type.BLOCK_COMMENT, Type.LINE_COMMENT, Type.TAB, Type.SPACE, Type.NEW_LINE]:
                # add token to tokens list
                tokens_list.append(result["token"])

    # checking if positioning error happend
    if index != content_length:
        raise Exception('Lexical error at position ' + str(index))

    # returning list of all identified tokens and generated symbol table
    return tokens_list, generate_symbol_table(tokens_list)


# used for finding a token inside the given string data 
def get_token(data: str, begin: int) -> Dict:
    if begin < 0 or begin >= len(data):
        raise IndexError(data, 'Index out of bounds: ' + begin)

    # checking all types of regexes on current chunk of data
    for type in Type:
        pattern = r'.{' + str(begin) + '}' + type.value
        match = re.match(pattern, data, re.DOTALL)

        # when a pattern matches
        if match:
            end = match.end(1)

            # is used to include the closing ' or " for character or string literals in their token index range 
            if type in [Type.STRING_LITERAL, Type.CHARACTER_LITERAL, Type.CHARACTER_LITERAL_INVALID]:
                end += 1

            return dict(token=Token(begin, end, data[begin:end], type), next_position=end)

    # when none of regex patterns match current data chunk
    return dict(token=None, next_position=begin + 1)


# generates symbol table with identifiers and their types and values
def generate_symbol_table(tokens: TokensList) -> SymbolTableData:
    sym_table = dict()

    for index, token in enumerate(tokens):
        if token.type.name == "IDENTIFIER":
            current_token_type = "undefined" 
            if token.value in sym_table.keys():
                if "type" in sym_table[token.value]:
                    current_token_type = sym_table[token.value]["type"]

            if index > 0 and (not (token.value in sym_table.keys())):
                last_token = tokens[index - 1]
                if last_token.type.name in DATA_TYPES:
                    current_token_type = last_token.type.name

            current_token_value = "undefined" 
            if token.value in sym_table.keys():
                if "value" in sym_table[token.value]:
                    current_token_value = sym_table[token.value]["value"]

            if index < len(tokens) - 2:
                next_token = tokens[index + 1]
                if next_token.type.name == "ASSIGNMENT":
                    val_token = tokens[index + 2]
                    if val_token.type.name in LITERALS_LIST:
                        current_token_value = val_token.value

            sym_table[token.value] = {
                "id": tokens.index(token) + 1,
                "name": token.value,
                "type": current_token_type,
                "value": current_token_value
            }
            
    return sym_table

