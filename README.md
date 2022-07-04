# Mini JAVA Compiler

## Description

Mini JAVA Compiler is the compiler of a simple mini programming language similar to JAVA programming language. In this project we are going to implement a Lexer and a Parser for this Mini JAVA Compiler.

Currently, only lexer and parser sections are implemented and it will generate four different output files for each input file: one for symbol table, one for all of identified tokens, another one for all of parsing steps and symbols stack status on each of those steps and a file containing parse tree data in a python tuple styled nested representation.

## Running instructions

First you need to have python installed on your machine. if you don't have python installed head over to [python's official homepage](https://www.python.org/) and download the latest version installer then execute it.

### Using regular python interpreter

In order to run mini java compiler you need to install required python packages. For installing required packages you can open project directory inside your operating system command line and use the following command:

```
pip install -r requirements.txt
```

after that you can use the `compiler.py` script file in the following form:

```
python compiler.py input_file_path [more_input_files ...]
```

For example:

```
python compiler.py path/to/file.txt             # using a single file
python compiler.py file1.txt file2.txt ...      # using multiple files
```

after running the compiler you will get two new files as outputs in the same path that your input file was and their names is based on your input file name. For example:

```
file.txt ->
    file_output_all_tokens.txt
    file_output_symbol_table.txt
    file_output_parsing_stack.txt",
    file_output_parsing_tree.txt",
```

### Using virtual environment

Using virtual environment requires you to install it in your machine. Instructions are available at this page: [Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html)

For creating a virtual environment in order to run this project head over to this project directory and open it in your system command line and execute the following command:

```
python -m venv mini-java-compiler-env
```

after that you need to activate the created environment

#### in linux

```
source mini-java-compiler-env/bin/activate
```

#### in windows

```
mini-java-compiler-env\Scripts\activate.bat
```

After activating virtual environment, rest of the running process is exactly the same as using regular python interpreter.

## Example of compilation using a simple input file

### input.txt content:

```
void main() {
     int c = 5;
     int a = 10;
     boolean d = true; // sdfjklasdhfjsdfhjs

     /* sdfsfasdfasdf */

     /*
          int adolf = 2;
          char cosmic = 'b';
     */

     while ( a > 8 ) {
          if ( 5 == 5 ) {
               char c = 'a';
               String b = "hello";
          }
     }
}
```

### output

```
WARNING: 81 shift/reduce conflicts
WARNING: 25 reduce/reduce conflicts
Parser debugging for MiniJAVAParser written to parser.out


All Identified Tokens:
+----+--------------+---------+------------+-------+
| id |     type     |  value  | lineNumber | index |
+----+--------------+---------+------------+-------+
| 1  |     VOID     |  void   |     1      |   0   |
+----+--------------+---------+------------+-------+
| 2  |     MAIN     |  main   |     1      |   5   |
+----+--------------+---------+------------+-------+
| 3  |  OPEN_PAREN  |    (    |     1      |   9   |
+----+--------------+---------+------------+-------+
| 4  | CLOSE_PAREN  |    )    |     1      |  10   |
+----+--------------+---------+------------+-------+
| 5  |  OPEN_BRACE  |    {    |     1      |  12   |
+----+--------------+---------+------------+-------+
| 6  |  DATA_TYPE   |   int   |     2      |  19   |
+----+--------------+---------+------------+-------+
| 7  |  IDENTIFIER  |    c    |     2      |  23   |
+----+--------------+---------+------------+-------+
| 8  |    ASSIGN    |    =    |     2      |  25   |
+----+--------------+---------+------------+-------+
| 9  |   INTEGER    |    5    |     2      |  27   |
+----+--------------+---------+------------+-------+
| 10 |  SEMICOLON   |    ;    |     2      |  28   |
+----+--------------+---------+------------+-------+
| 11 |  DATA_TYPE   |   int   |     3      |  35   |
+----+--------------+---------+------------+-------+
| 12 |  IDENTIFIER  |    a    |     3      |  39   |
+----+--------------+---------+------------+-------+
| 13 |    ASSIGN    |    =    |     3      |  41   |
+----+--------------+---------+------------+-------+
| 14 |   INTEGER    |   10    |     3      |  43   |
+----+--------------+---------+------------+-------+
| 15 |  SEMICOLON   |    ;    |     3      |  45   |
+----+--------------+---------+------------+-------+
| 16 |  DATA_TYPE   | boolean |     4      |  52   |
+----+--------------+---------+------------+-------+
| 17 |  IDENTIFIER  |    d    |     4      |  60   |
+----+--------------+---------+------------+-------+
| 18 |    ASSIGN    |    =    |     4      |  62   |
+----+--------------+---------+------------+-------+
| 19 |   BOOLEAN    |  true   |     4      |  64   |
+----+--------------+---------+------------+-------+
| 20 |  SEMICOLON   |    ;    |     4      |  68   |
+----+--------------+---------+------------+-------+
| 21 |    WHILE     |  while  |     10     |  195  |
+----+--------------+---------+------------+-------+
| 22 |  OPEN_PAREN  |    (    |     10     |  201  |
+----+--------------+---------+------------+-------+
| 23 |  IDENTIFIER  |    a    |     10     |  203  |
+----+--------------+---------+------------+-------+
| 24 | GREATER_THAN |    >    |     10     |  205  |
+----+--------------+---------+------------+-------+
| 25 |   INTEGER    |    8    |     10     |  207  |
+----+--------------+---------+------------+-------+
| 26 | CLOSE_PAREN  |    )    |     10     |  209  |
+----+--------------+---------+------------+-------+
| 27 |  OPEN_BRACE  |    {    |     10     |  211  |
+----+--------------+---------+------------+-------+
| 28 |      IF      |   if    |     11     |  223  |
+----+--------------+---------+------------+-------+
| 29 |  OPEN_PAREN  |    (    |     11     |  226  |
+----+--------------+---------+------------+-------+
| 30 |   INTEGER    |    5    |     11     |  228  |
+----+--------------+---------+------------+-------+
| 31 |    EQUAL     |   ==    |     11     |  230  |
+----+--------------+---------+------------+-------+
| 32 |   INTEGER    |    5    |     11     |  233  |
+----+--------------+---------+------------+-------+
| 33 | CLOSE_PAREN  |    )    |     11     |  235  |
+----+--------------+---------+------------+-------+
| 34 |  OPEN_BRACE  |    {    |     11     |  237  |
+----+--------------+---------+------------+-------+
| 35 |  DATA_TYPE   |  char   |     12     |  254  |
+----+--------------+---------+------------+-------+
| 36 |  IDENTIFIER  |    c    |     12     |  259  |
+----+--------------+---------+------------+-------+
| 37 |    ASSIGN    |    =    |     12     |  261  |
+----+--------------+---------+------------+-------+
| 38 |  CHARACTER   |   'a'   |     12     |  263  |
+----+--------------+---------+------------+-------+
| 39 |  SEMICOLON   |    ;    |     12     |  266  |
+----+--------------+---------+------------+-------+
| 40 |  DATA_TYPE   | String  |     13     |  283  |
+----+--------------+---------+------------+-------+
| 41 |  IDENTIFIER  |    b    |     13     |  290  |
+----+--------------+---------+------------+-------+
| 42 |    ASSIGN    |    =    |     13     |  292  |
+----+--------------+---------+------------+-------+
| 43 |    STRING    | "hello" |     13     |  294  |
+----+--------------+---------+------------+-------+
| 44 |  SEMICOLON   |    ;    |     13     |  301  |
+----+--------------+---------+------------+-------+
| 45 | CLOSE_BRACE  |    }    |     14     |  313  |
+----+--------------+---------+------------+-------+
| 46 | CLOSE_BRACE  |    }    |     15     |  320  |
+----+--------------+---------+------------+-------+
| 47 | CLOSE_BRACE  |    }    |     16     |  322  |
+----+--------------+---------+------------+-------+


Parse Stack Content:
Parser Shift operation: VOID 'void'
[$end, Token(type='VOID', value='void', lineno=1, index=0)]

Parser Shift operation: MAIN 'main'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5)]

Parser Shift operation: OPEN_PAREN '('
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9)]

Parser Shift operation: CLOSE_PAREN ')'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10)]

Parser Shift operation: OPEN_BRACE '{'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12)]

Parser Reduce operation:
Used rule: statements_set ->
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set]

Parser Shift operation: DATA_TYPE 'int'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='DATA_TYPE', value='int', lineno=2, index=19)]

Parser Shift operation: IDENTIFIER 'c'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='DATA_TYPE', value='int', lineno=2, index=19), Token(type='IDENTIFIER', value='c', lineno=2, index=23)]

Parser Shift operation: ASSIGN '='
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='DATA_TYPE', value='int', lineno=2, index=19), Token(type='IDENTIFIER', value='c', lineno=2, index=23), Token(type='ASSIGN', value='=', lineno=2, index=25)]

Parser Shift operation: INTEGER '5'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='DATA_TYPE', value='int', lineno=2, index=19), Token(type='IDENTIFIER', value='c', lineno=2, index=23), Token(type='ASSIGN', value='=', lineno=2, index=25), Token(type='INTEGER', value=5, lineno=2, index=27)]

Parser Reduce operation:
Used rule: literal -> INTEGER
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='DATA_TYPE', value='int', lineno=2, index=19), Token(type='IDENTIFIER', value='c', lineno=2, index=23), Token(type='ASSIGN', value='=', lineno=2, index=25), literal]

Parser Reduce operation:
Used rule: expression -> literal
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='DATA_TYPE', value='int', lineno=2, index=19), Token(type='IDENTIFIER', value='c', lineno=2, index=23), Token(type='ASSIGN', value='=', lineno=2, index=25), expression]

Parser Reduce operation:
Used rule: variable_dec_expression -> DATA_TYPE IDENTIFIER ASSIGN expression
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, variable_dec_expression]

Parser Shift operation: SEMICOLON ';'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, variable_dec_expression, Token(type='SEMICOLON', value=';', lineno=2, index=28)]

Parser Reduce operation:
Used rule: variable_declaration -> variable_dec_expression SEMICOLON
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, variable_declaration]

Parser Reduce operation:
Used rule: statement -> variable_declaration
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, statement]

Parser Reduce operation:
Used rule: statements_set -> statements_set statement
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set]

Parser Shift operation: DATA_TYPE 'int'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='DATA_TYPE', value='int', lineno=3, index=35)]

Parser Shift operation: IDENTIFIER 'a'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='DATA_TYPE', value='int', lineno=3, index=35), Token(type='IDENTIFIER', value='a', lineno=3, index=39)]

Parser Shift operation: ASSIGN '='
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='DATA_TYPE', value='int', lineno=3, index=35), Token(type='IDENTIFIER', value='a', lineno=3, index=39), Token(type='ASSIGN', value='=', lineno=3, index=41)]

Parser Shift operation: INTEGER '10'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='DATA_TYPE', value='int', lineno=3, index=35), Token(type='IDENTIFIER', value='a', lineno=3, index=39), Token(type='ASSIGN', value='=', lineno=3, index=41), Token(type='INTEGER', value=10, lineno=3, index=43)]

Parser Reduce operation:
Used rule: literal -> INTEGER
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='DATA_TYPE', value='int', lineno=3, index=35), Token(type='IDENTIFIER', value='a', lineno=3, index=39), Token(type='ASSIGN', value='=', lineno=3, index=41), literal]

Parser Reduce operation:
Used rule: expression -> literal
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='DATA_TYPE', value='int', lineno=3, index=35), Token(type='IDENTIFIER', value='a', lineno=3, index=39), Token(type='ASSIGN', value='=', lineno=3, index=41), expression]

Parser Reduce operation:
Used rule: variable_dec_expression -> DATA_TYPE IDENTIFIER ASSIGN expression
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, variable_dec_expression]

Parser Shift operation: SEMICOLON ';'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, variable_dec_expression, Token(type='SEMICOLON', value=';', lineno=3, index=45)]

Parser Reduce operation:
Used rule: variable_declaration -> variable_dec_expression SEMICOLON
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, variable_declaration]

Parser Reduce operation:
Used rule: statement -> variable_declaration
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, statement]

Parser Reduce operation:
Used rule: statements_set -> statements_set statement
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set]

Parser Shift operation: DATA_TYPE 'boolean'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='DATA_TYPE', value='boolean', lineno=4, index=52)]

Parser Shift operation: IDENTIFIER 'd'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='DATA_TYPE', value='boolean', lineno=4, index=52), Token(type='IDENTIFIER', value='d', lineno=4, index=60)]

Parser Shift operation: ASSIGN '='
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='DATA_TYPE', value='boolean', lineno=4, index=52), Token(type='IDENTIFIER', value='d', lineno=4, index=60), Token(type='ASSIGN', value='=', lineno=4, index=62)]

Parser Shift operation: BOOLEAN 'true'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='DATA_TYPE', value='boolean', lineno=4, index=52), Token(type='IDENTIFIER', value='d', lineno=4, index=60), Token(type='ASSIGN', value='=', lineno=4, index=62), Token(type='BOOLEAN', value='true', lineno=4, index=64)]

Parser Reduce operation:
Used rule: literal -> BOOLEAN
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='DATA_TYPE', value='boolean', lineno=4, index=52), Token(type='IDENTIFIER', value='d', lineno=4, index=60), Token(type='ASSIGN', value='=', lineno=4, index=62), literal]

Parser Reduce operation:
Used rule: expression -> literal
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='DATA_TYPE', value='boolean', lineno=4, index=52), Token(type='IDENTIFIER', value='d', lineno=4, index=60), Token(type='ASSIGN', value='=', lineno=4, index=62), expression]

Parser Reduce operation:
Used rule: variable_dec_expression -> DATA_TYPE IDENTIFIER ASSIGN expression
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, variable_dec_expression]

Parser Shift operation: SEMICOLON ';'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, variable_dec_expression, Token(type='SEMICOLON', value=';', lineno=4, index=68)]

Parser Reduce operation:
Used rule: variable_declaration -> variable_dec_expression SEMICOLON
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, variable_declaration]

Parser Reduce operation:
Used rule: statement -> variable_declaration
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, statement]

Parser Reduce operation:
Used rule: statements_set -> statements_set statement
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set]

Parser Shift operation: WHILE 'while'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195)]

Parser Shift operation: OPEN_PAREN '('
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201)]

Parser Shift operation: IDENTIFIER 'a'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), Token(type='IDENTIFIER', value='a', lineno=10, index=203)]

Parser Reduce operation:
Used rule: expression -> IDENTIFIER
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression]

Parser Shift operation: GREATER_THAN '>'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='GREATER_THAN', value='>', lineno=10, index=205)]

Parser Shift operation: INTEGER '8'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='GREATER_THAN', value='>', lineno=10, index=205), Token(type='INTEGER', value=8, lineno=10, index=207)]

Parser Reduce operation:
Used rule: literal -> INTEGER
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='GREATER_THAN', value='>', lineno=10, index=205), literal]

Parser Reduce operation:
Used rule: expression -> literal
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='GREATER_THAN', value='>', lineno=10, index=205), expression]

Parser Reduce operation:
Used rule: expression -> expression GREATER_THAN expression
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression]

Parser Shift operation: CLOSE_PAREN ')'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209)]

Parser Shift operation: OPEN_BRACE '{'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211)]

Parser Reduce operation:
Used rule: statements_set ->
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set]

Parser Shift operation: IF 'if'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223)]

Parser Shift operation: OPEN_PAREN '('
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226)]

Parser Shift operation: INTEGER '5'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), Token(type='INTEGER', value=5, lineno=11, index=228)]

Parser Reduce operation:
Used rule: literal -> INTEGER
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), literal]

Parser Reduce operation:
Used rule: expression -> literal
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression]

Parser Shift operation: EQUAL '=='
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='EQUAL', value='==', lineno=11, index=230)]

Parser Shift operation: INTEGER '5'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='EQUAL', value='==', lineno=11, index=230), Token(type='INTEGER', value=5, lineno=11, index=233)]

Parser Reduce operation:
Used rule: literal -> INTEGER
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='EQUAL', value='==', lineno=11, index=230), literal]

Parser Reduce operation:
Used rule: expression -> literal
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='EQUAL', value='==', lineno=11, index=230), expression]

Parser Reduce operation:
Used rule: expression -> expression EQUAL expression
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression]

Parser Shift operation: CLOSE_PAREN ')'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='CLOSE_PAREN', value=')', lineno=11, index=235)]

Parser Shift operation: OPEN_BRACE '{'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='CLOSE_PAREN', value=')', lineno=11, index=235), Token(type='OPEN_BRACE', value='{', lineno=11, index=237)]

Parser Reduce operation:
Used rule: statements_set ->
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='CLOSE_PAREN', value=')', lineno=11, index=235), Token(type='OPEN_BRACE', value='{', lineno=11, index=237), statements_set]

Parser Shift operation: DATA_TYPE 'char'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='CLOSE_PAREN', value=')', lineno=11, index=235), Token(type='OPEN_BRACE', value='{', lineno=11, index=237), statements_set, Token(type='DATA_TYPE', value='char', lineno=12, index=254)]

Parser Shift operation: IDENTIFIER 'c'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='CLOSE_PAREN', value=')', lineno=11, index=235), Token(type='OPEN_BRACE', value='{', lineno=11, index=237), statements_set, Token(type='DATA_TYPE', value='char', lineno=12, index=254), Token(type='IDENTIFIER', value='c', lineno=12, index=259)]

Parser Shift operation: ASSIGN '='
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='CLOSE_PAREN', value=')', lineno=11, index=235), Token(type='OPEN_BRACE', value='{', lineno=11, index=237), statements_set, Token(type='DATA_TYPE', value='char', lineno=12, index=254), Token(type='IDENTIFIER', value='c', lineno=12, index=259), Token(type='ASSIGN', value='=', lineno=12, index=261)]

Parser Shift operation: CHARACTER ''a''
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='CLOSE_PAREN', value=')', lineno=11, index=235), Token(type='OPEN_BRACE', value='{', lineno=11, index=237), statements_set, Token(type='DATA_TYPE', value='char', lineno=12, index=254), Token(type='IDENTIFIER', value='c', lineno=12, index=259), Token(type='ASSIGN', value='=', lineno=12, index=261), Token(type='CHARACTER', value="'a'", lineno=12, index=263)]

Parser Reduce operation:
Used rule: literal -> CHARACTER
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='CLOSE_PAREN', value=')', lineno=11, index=235), Token(type='OPEN_BRACE', value='{', lineno=11, index=237), statements_set, Token(type='DATA_TYPE', value='char', lineno=12, index=254), Token(type='IDENTIFIER', value='c', lineno=12, index=259), Token(type='ASSIGN', value='=', lineno=12, index=261), literal]

Parser Reduce operation:
Used rule: expression -> literal
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='CLOSE_PAREN', value=')', lineno=11, index=235), Token(type='OPEN_BRACE', value='{', lineno=11, index=237), statements_set, Token(type='DATA_TYPE', value='char', lineno=12, index=254), Token(type='IDENTIFIER', value='c', lineno=12, index=259), Token(type='ASSIGN', value='=', lineno=12, index=261), expression]

Parser Reduce operation:
Used rule: variable_dec_expression -> DATA_TYPE IDENTIFIER ASSIGN expression
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='CLOSE_PAREN', value=')', lineno=11, index=235), Token(type='OPEN_BRACE', value='{', lineno=11, index=237), statements_set, variable_dec_expression]

Parser Shift operation: SEMICOLON ';'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='CLOSE_PAREN', value=')', lineno=11, index=235), Token(type='OPEN_BRACE', value='{', lineno=11, index=237), statements_set, variable_dec_expression, Token(type='SEMICOLON', value=';', lineno=12, index=266)]

Parser Reduce operation:
Used rule: variable_declaration -> variable_dec_expression SEMICOLON
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='CLOSE_PAREN', value=')', lineno=11, index=235), Token(type='OPEN_BRACE', value='{', lineno=11, index=237), statements_set, variable_declaration]

Parser Reduce operation:
Used rule: statement -> variable_declaration
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='CLOSE_PAREN', value=')', lineno=11, index=235), Token(type='OPEN_BRACE', value='{', lineno=11, index=237), statements_set, statement]

Parser Reduce operation:
Used rule: statements_set -> statements_set statement
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='CLOSE_PAREN', value=')', lineno=11, index=235), Token(type='OPEN_BRACE', value='{', lineno=11, index=237), statements_set]

Parser Shift operation: DATA_TYPE 'String'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='CLOSE_PAREN', value=')', lineno=11, index=235), Token(type='OPEN_BRACE', value='{', lineno=11, index=237), statements_set, Token(type='DATA_TYPE', value='String', lineno=13, index=283)]

Parser Shift operation: IDENTIFIER 'b'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='CLOSE_PAREN', value=')', lineno=11, index=235), Token(type='OPEN_BRACE', value='{', lineno=11, index=237), statements_set, Token(type='DATA_TYPE', value='String', lineno=13, index=283), Token(type='IDENTIFIER', value='b', lineno=13, index=290)]

Parser Shift operation: ASSIGN '='
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='CLOSE_PAREN', value=')', lineno=11, index=235), Token(type='OPEN_BRACE', value='{', lineno=11, index=237), statements_set, Token(type='DATA_TYPE', value='String', lineno=13, index=283), Token(type='IDENTIFIER', value='b', lineno=13, index=290), Token(type='ASSIGN', value='=', lineno=13, index=292)]

Parser Shift operation: STRING '"hello"'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='CLOSE_PAREN', value=')', lineno=11, index=235), Token(type='OPEN_BRACE', value='{', lineno=11, index=237), statements_set, Token(type='DATA_TYPE', value='String', lineno=13, index=283), Token(type='IDENTIFIER', value='b', lineno=13, index=290), Token(type='ASSIGN', value='=', lineno=13, index=292), Token(type='STRING', value='"hello"', lineno=13, index=294)]

Parser Reduce operation:
Used rule: literal -> STRING
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='CLOSE_PAREN', value=')', lineno=11, index=235), Token(type='OPEN_BRACE', value='{', lineno=11, index=237), statements_set, Token(type='DATA_TYPE', value='String', lineno=13, index=283), Token(type='IDENTIFIER', value='b', lineno=13, index=290), Token(type='ASSIGN', value='=', lineno=13, index=292), literal]

Parser Reduce operation:
Used rule: expression -> literal
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='CLOSE_PAREN', value=')', lineno=11, index=235), Token(type='OPEN_BRACE', value='{', lineno=11, index=237), statements_set, Token(type='DATA_TYPE', value='String', lineno=13, index=283), Token(type='IDENTIFIER', value='b', lineno=13, index=290), Token(type='ASSIGN', value='=', lineno=13, index=292), expression]

Parser Reduce operation:
Used rule: variable_dec_expression -> DATA_TYPE IDENTIFIER ASSIGN expression
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='CLOSE_PAREN', value=')', lineno=11, index=235), Token(type='OPEN_BRACE', value='{', lineno=11, index=237), statements_set, variable_dec_expression]

Parser Shift operation: SEMICOLON ';'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='CLOSE_PAREN', value=')', lineno=11, index=235), Token(type='OPEN_BRACE', value='{', lineno=11, index=237), statements_set, variable_dec_expression, Token(type='SEMICOLON', value=';', lineno=13, index=301)]

Parser Reduce operation:
Used rule: variable_declaration -> variable_dec_expression SEMICOLON
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='CLOSE_PAREN', value=')', lineno=11, index=235), Token(type='OPEN_BRACE', value='{', lineno=11, index=237), statements_set, variable_declaration]

Parser Reduce operation:
Used rule: statement -> variable_declaration
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='CLOSE_PAREN', value=')', lineno=11, index=235), Token(type='OPEN_BRACE', value='{', lineno=11, index=237), statements_set, statement]

Parser Reduce operation:
Used rule: statements_set -> statements_set statement
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='CLOSE_PAREN', value=')', lineno=11, index=235), Token(type='OPEN_BRACE', value='{', lineno=11, index=237), statements_set]

Parser Reduce operation:
Used rule: statements_block -> statements_set
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='CLOSE_PAREN', value=')', lineno=11, index=235), Token(type='OPEN_BRACE', value='{', lineno=11, index=237), statements_block]

Parser Shift operation: CLOSE_BRACE '}'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='CLOSE_PAREN', value=')', lineno=11, index=235), Token(type='OPEN_BRACE', value='{', lineno=11, index=237), statements_block, Token(type='CLOSE_BRACE', value='}', lineno=14, index=313)]

Parser Reduce operation:
Used rule: else_statement ->
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, Token(type='IF', value='if', lineno=11, index=223), Token(type='OPEN_PAREN', value='(', lineno=11, index=226), expression, Token(type='CLOSE_PAREN', value=')', lineno=11, index=235), Token(type='OPEN_BRACE', value='{', lineno=11, index=237), statements_block, Token(type='CLOSE_BRACE', value='}', lineno=14, index=313), else_statement]

Parser Reduce operation:
Used rule: if_statement -> IF OPEN_PAREN expression CLOSE_PAREN OPEN_BRACE statements_block CLOSE_BRACE else_statement
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, if_statement]

Parser Reduce operation:
Used rule: statement -> if_statement
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set, statement]

Parser Reduce operation:
Used rule: statements_set -> statements_set statement
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_set]

Parser Reduce operation:
Used rule: statements_block -> statements_set
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_block]

Parser Shift operation: CLOSE_BRACE '}'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, Token(type='WHILE', value='while', lineno=10, index=195), Token(type='OPEN_PAREN', value='(', lineno=10, index=201), expression, Token(type='CLOSE_PAREN', value=')', lineno=10, index=209), Token(type='OPEN_BRACE', value='{', lineno=10, index=211), statements_block, Token(type='CLOSE_BRACE', value='}', lineno=15, index=320)]

Parser Reduce operation:
Used rule: while_loop_statement -> WHILE OPEN_PAREN expression CLOSE_PAREN OPEN_BRACE statements_block CLOSE_BRACE
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, while_loop_statement]

Parser Reduce operation:
Used rule: statement -> while_loop_statement
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set, statement]

Parser Reduce operation:
Used rule: statements_set -> statements_set statement
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_set]

Parser Reduce operation:
Used rule: statements_block -> statements_set
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_block]

Parser Shift operation: CLOSE_BRACE '}'
[$end, Token(type='VOID', value='void', lineno=1, index=0), Token(type='MAIN', value='main', lineno=1, index=5), Token(type='OPEN_PAREN', value='(', lineno=1, index=9), Token(type='CLOSE_PAREN', value=')', lineno=1, index=10), Token(type='OPEN_BRACE', value='{', lineno=1, index=12), statements_block, Token(type='CLOSE_BRACE', value='}', lineno=16, index=322)]

Parser Reduce operation:
Used rule: main_function_definition -> VOID MAIN OPEN_PAREN CLOSE_PAREN OPEN_BRACE statements_block CLOSE_BRACE
[$end, main_function_definition]




Parse Tree Content:
('main_function_definition',
 [('var', 'c', ('int', 5)),
  ('var', 'a', ('int', 10)),
  ('var', 'd', ('boolean', 'true')),
  ('while_loop',
   ('while_loop_setup', ('>', 'a', ('int', 8))),
   [('if',
     ('==', ('int', 5), ('int', 5)),
     ('branch',
      [('var', 'c', ('char', "'a'")), ('var', 'b', ('String', '"hello"'))]),
     [])])])


Symbol Table:
+------+---------+---------+------------+-------+
| name |  type   |  value  | lineNumber | index |
+------+---------+---------+------------+-------+
|  c   |  char   |   'a'   |     12     |  259  |
+------+---------+---------+------------+-------+
|  a   |   int   |   10    |     3      |  39   |
+------+---------+---------+------------+-------+
|  d   | boolean |  true   |     4      |  60   |
+------+---------+---------+------------+-------+
|  b   | String  | "hello" |     13     |  290  |
+------+---------+---------+------------+-------+


Compiler job is done!!!
```
