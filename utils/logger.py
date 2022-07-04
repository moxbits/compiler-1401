# this class is used to log symbol stack status
# during parsing operations and store shift, reduce and errors
# that happened during parsing operations
class SymbolStackLogger:
    # final string result that stores symbol state data
    stack_content_str = ""

    # adding a new chunk of data to stack content
    def log(content):
        SymbolStackLogger.stack_content_str = SymbolStackLogger.stack_content_str + content
