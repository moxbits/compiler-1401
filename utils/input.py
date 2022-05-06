# used for reading content of a file
def get_file_content(file_address: str) -> str:
    file = open(file_address, 'r')
    file_content = file.read()
    file.close()
    return file_content