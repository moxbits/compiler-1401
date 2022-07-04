from sly.lex import Token


# this class is used to generate our symbol table
# it generates a built-in python dictionary and stores
# symbol table data as key-value pairs
class SymbolTable:
    # Initialize a empty dictionary for storing identifiers
    def __init__(self):
        self.symbols = {}

    # Insert tokens into symbols dictionary
    def insert(self, token):
        self.symbols[token['name']] = {
            'name': token['name'],
            'type': token['type'],
            'value': token['value'],
            'lineNumber': token['lineNumber'],
            'index': token['index']
        }

    # Searching if a token exists in symbols dictionary
    def search(self, token):
        if isinstance(token, Token):
            if token.value in self.symbols.keys():
                return True
        else:
            if token['value'] in self.symbols.keys():
                return True

        return False
