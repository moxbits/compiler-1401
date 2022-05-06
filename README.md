# Mini JAVA Compiler 

## Description
Mini JAVA Compiler is the compiler of a simple mini programming language similar to JAVA programming language. In this project we are going to implement a Lexer and a Parser for this Mini JAVA Compiler. 

Currently, only lexer is implemented and it will generate two different output files for each input file: one for symbol table and one for all of identified tokens. 

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
    /*
Lorem ipsum dolor sit amet.
Quis officiis et fugiat quam ea sunt nesciunt.
33 voluptates neque ut dolores aperiam non aspernatur exercitationem cum quos culpa.
Est debitis quos eum quam illum ut doloribus autem et neque eaque sit galisum corporis sed possimus quaerat.
Et voluptas sint et accusantium suscipit qui error dolores eos velit corrupti. 
*/
    int sut = 2;
    int x;
    if(sut == 1) {
        x = 10;
        /*
Lorem ipsum dolor sit amet.
Quis officiis et fugiat quam ea sunt nesciunt.
33 voluptates neque ut dolores aperiam non aspernatur exercitationem cum quos culpa.
Est debitis quos eum quam illum ut doloribus autem et neque eaque sit galisum corporis sed possimus quaerat.
Et voluptas sint et accusantium suscipit qui error dolores eos velit corrupti. 
*/
    } else if (sut == 2) {
        x = 20;
    } else if (sut >= 3 && sut <= 5) {
        x = 30;
    } else {
        x = 60;
    }
    x = (x / (sut + 2)) - 5;
    x = x % sut;
}
```
### command line output
```
All Identified Tokens:
+----+-------------------+-------+
| id |       type        | value |
+----+-------------------+-------+
| 1  |       VOID        | void  |
+----+-------------------+-------+
| 2  |    IDENTIFIER     | main  |
+----+-------------------+-------+
| 3  |    OPEN_PAREN     |   (   |
+----+-------------------+-------+
| 4  |    CLOSE_PAREN    |   )   |
+----+-------------------+-------+
| 5  | OPEN_CURLY_BRACE  |   {   |
+----+-------------------+-------+
| 6  |        INT        |  int  |
+----+-------------------+-------+
| 7  |    IDENTIFIER     |  sut  |
+----+-------------------+-------+
| 8  |    ASSIGNMENT     |   =   |
+----+-------------------+-------+
| 9  |   INT_CONSTANT    |   2   |
+----+-------------------+-------+
| 10 |     SEMICOLON     |   ;   |
+----+-------------------+-------+
| 11 |        INT        |  int  |
+----+-------------------+-------+
| 12 |    IDENTIFIER     |   x   |
+----+-------------------+-------+
| 13 |     SEMICOLON     |   ;   |
+----+-------------------+-------+
| 14 |        IF         |  if   |
+----+-------------------+-------+
| 15 |    OPEN_PAREN     |   (   |
+----+-------------------+-------+
| 16 |    IDENTIFIER     |  sut  |
+----+-------------------+-------+
| 17 |       EQUAL       |  ==   |
+----+-------------------+-------+
| 18 |   INT_CONSTANT    |   1   |
+----+-------------------+-------+
| 19 |    CLOSE_PAREN    |   )   |
+----+-------------------+-------+
| 20 | OPEN_CURLY_BRACE  |   {   |
+----+-------------------+-------+
| 21 |    IDENTIFIER     |   x   |
+----+-------------------+-------+
| 22 |    ASSIGNMENT     |   =   |
+----+-------------------+-------+
| 23 |   INT_CONSTANT    |  10   |
+----+-------------------+-------+
| 24 |     SEMICOLON     |   ;   |
+----+-------------------+-------+
| 25 | CLOSE_CURLY_BRACE |   }   |
+----+-------------------+-------+
| 26 |       ELSE        | else  |
+----+-------------------+-------+
| 27 |        IF         |  if   |
+----+-------------------+-------+
| 28 |    OPEN_PAREN     |   (   |
+----+-------------------+-------+
| 29 |    IDENTIFIER     |  sut  |
+----+-------------------+-------+
| 30 |       EQUAL       |  ==   |
+----+-------------------+-------+
| 31 |   INT_CONSTANT    |   2   |
+----+-------------------+-------+
| 32 |    CLOSE_PAREN    |   )   |
+----+-------------------+-------+
| 33 | OPEN_CURLY_BRACE  |   {   |
+----+-------------------+-------+
| 34 |    IDENTIFIER     |   x   |
+----+-------------------+-------+
| 35 |    ASSIGNMENT     |   =   |
+----+-------------------+-------+
| 36 |   INT_CONSTANT    |  20   |
+----+-------------------+-------+
| 37 |     SEMICOLON     |   ;   |
+----+-------------------+-------+
| 38 | CLOSE_CURLY_BRACE |   }   |
+----+-------------------+-------+
| 39 |       ELSE        | else  |
+----+-------------------+-------+
| 40 |        IF         |  if   |
+----+-------------------+-------+
| 41 |    OPEN_PAREN     |   (   |
+----+-------------------+-------+
| 42 |    IDENTIFIER     |  sut  |
+----+-------------------+-------+
| 43 |    CLOSE_CARET    |   >   |
+----+-------------------+-------+
| 44 |    ASSIGNMENT     |   =   |
+----+-------------------+-------+
| 45 |   INT_CONSTANT    |   3   |
+----+-------------------+-------+
| 46 |    IDENTIFIER     |  sut  |
+----+-------------------+-------+
| 47 |    OPEN_CARET     |   <   |
+----+-------------------+-------+
| 48 |    ASSIGNMENT     |   =   |
+----+-------------------+-------+
| 49 |   INT_CONSTANT    |   5   |
+----+-------------------+-------+
| 50 |    CLOSE_PAREN    |   )   |
+----+-------------------+-------+
| 51 | OPEN_CURLY_BRACE  |   {   |
+----+-------------------+-------+
| 52 |    IDENTIFIER     |   x   |
+----+-------------------+-------+
| 53 |    ASSIGNMENT     |   =   |
+----+-------------------+-------+
| 54 |   INT_CONSTANT    |  30   |
+----+-------------------+-------+
| 55 |     SEMICOLON     |   ;   |
+----+-------------------+-------+
| 56 | CLOSE_CURLY_BRACE |   }   |
+----+-------------------+-------+
| 57 |       ELSE        | else  |
+----+-------------------+-------+
| 58 | OPEN_CURLY_BRACE  |   {   |
+----+-------------------+-------+
| 59 |    IDENTIFIER     |   x   |
+----+-------------------+-------+
| 60 |    ASSIGNMENT     |   =   |
+----+-------------------+-------+
| 61 |   INT_CONSTANT    |  60   |
+----+-------------------+-------+
| 62 |     SEMICOLON     |   ;   |
+----+-------------------+-------+
| 63 | CLOSE_CURLY_BRACE |   }   |
+----+-------------------+-------+
| 64 |    IDENTIFIER     |   x   |
+----+-------------------+-------+
| 65 |    ASSIGNMENT     |   =   |
+----+-------------------+-------+
| 66 |    OPEN_PAREN     |   (   |
+----+-------------------+-------+
| 67 |    IDENTIFIER     |   x   |
+----+-------------------+-------+
| 68 |      DIVIDE       |   /   |
+----+-------------------+-------+
| 69 |    OPEN_PAREN     |   (   |
+----+-------------------+-------+
| 70 |    IDENTIFIER     |  sut  |
+----+-------------------+-------+
| 71 |       PLUS        |   +   |
+----+-------------------+-------+
| 72 |   INT_CONSTANT    |   2   |
+----+-------------------+-------+
| 73 |    CLOSE_PAREN    |   )   |
+----+-------------------+-------+
| 74 |    CLOSE_PAREN    |   )   |
+----+-------------------+-------+
| 75 |       MINUS       |   -   |
+----+-------------------+-------+
| 76 |   INT_CONSTANT    |   5   |
+----+-------------------+-------+
| 77 |     SEMICOLON     |   ;   |
+----+-------------------+-------+
| 78 |    IDENTIFIER     |   x   |
+----+-------------------+-------+
| 79 |    ASSIGNMENT     |   =   |
+----+-------------------+-------+
| 80 |    IDENTIFIER     |   x   |
+----+-------------------+-------+
| 81 |    IDENTIFIER     |  sut  |
+----+-------------------+-------+
| 82 |     SEMICOLON     |   ;   |
+----+-------------------+-------+
| 83 | CLOSE_CURLY_BRACE |   }   |
+----+-------------------+-------+


Symbol Table:
+----+------+-----------+-----------+
| id | name |   type    |   value   |
+----+------+-----------+-----------+
| 2  | main | undefined | undefined |
+----+------+-----------+-----------+
| 81 | sut  |    INT    |     2     |
+----+------+-----------+-----------+
| 80 |  x   |    INT    |    60     |
+----+------+-----------+-----------+


Compiler job is done!!!
```
### output files
#### Symbol table output file:
the name of the file will be input_output_symbol_table.txt
```
+----+------+-----------+-----------+
| id | name |   type    |   value   |
+----+------+-----------+-----------+
| 2  | main | undefined | undefined |
+----+------+-----------+-----------+
| 81 | sut  |    INT    |     2     |
+----+------+-----------+-----------+
| 80 |  x   |    INT    |    60     |
+----+------+-----------+-----------+
```
#### All identified tokens output file:
the name of the file will be input_output_all_tokens.txt
```
+----+-------------------+-------+
| id |       type        | value |
+----+-------------------+-------+
| 1  |       VOID        | void  |
+----+-------------------+-------+
| 2  |    IDENTIFIER     | main  |
+----+-------------------+-------+
| 3  |    OPEN_PAREN     |   (   |
+----+-------------------+-------+
| 4  |    CLOSE_PAREN    |   )   |
+----+-------------------+-------+
| 5  | OPEN_CURLY_BRACE  |   {   |
+----+-------------------+-------+
| 6  |        INT        |  int  |
+----+-------------------+-------+
| 7  |    IDENTIFIER     |  sut  |
+----+-------------------+-------+
| 8  |    ASSIGNMENT     |   =   |
+----+-------------------+-------+
| 9  |   INT_CONSTANT    |   2   |
+----+-------------------+-------+
| 10 |     SEMICOLON     |   ;   |
+----+-------------------+-------+
| 11 |        INT        |  int  |
+----+-------------------+-------+
| 12 |    IDENTIFIER     |   x   |
+----+-------------------+-------+
| 13 |     SEMICOLON     |   ;   |
+----+-------------------+-------+
| 14 |        IF         |  if   |
+----+-------------------+-------+
| 15 |    OPEN_PAREN     |   (   |
+----+-------------------+-------+
| 16 |    IDENTIFIER     |  sut  |
+----+-------------------+-------+
| 17 |       EQUAL       |  ==   |
+----+-------------------+-------+
| 18 |   INT_CONSTANT    |   1   |
+----+-------------------+-------+
| 19 |    CLOSE_PAREN    |   )   |
+----+-------------------+-------+
| 20 | OPEN_CURLY_BRACE  |   {   |
+----+-------------------+-------+
| 21 |    IDENTIFIER     |   x   |
+----+-------------------+-------+
| 22 |    ASSIGNMENT     |   =   |
+----+-------------------+-------+
| 23 |   INT_CONSTANT    |  10   |
+----+-------------------+-------+
| 24 |     SEMICOLON     |   ;   |
+----+-------------------+-------+
| 25 | CLOSE_CURLY_BRACE |   }   |
+----+-------------------+-------+
| 26 |       ELSE        | else  |
+----+-------------------+-------+
| 27 |        IF         |  if   |
+----+-------------------+-------+
| 28 |    OPEN_PAREN     |   (   |
+----+-------------------+-------+
| 29 |    IDENTIFIER     |  sut  |
+----+-------------------+-------+
| 30 |       EQUAL       |  ==   |
+----+-------------------+-------+
| 31 |   INT_CONSTANT    |   2   |
+----+-------------------+-------+
| 32 |    CLOSE_PAREN    |   )   |
+----+-------------------+-------+
| 33 | OPEN_CURLY_BRACE  |   {   |
+----+-------------------+-------+
| 34 |    IDENTIFIER     |   x   |
+----+-------------------+-------+
| 35 |    ASSIGNMENT     |   =   |
+----+-------------------+-------+
| 36 |   INT_CONSTANT    |  20   |
+----+-------------------+-------+
| 37 |     SEMICOLON     |   ;   |
+----+-------------------+-------+
| 38 | CLOSE_CURLY_BRACE |   }   |
+----+-------------------+-------+
| 39 |       ELSE        | else  |
+----+-------------------+-------+
| 40 |        IF         |  if   |
+----+-------------------+-------+
| 41 |    OPEN_PAREN     |   (   |
+----+-------------------+-------+
| 42 |    IDENTIFIER     |  sut  |
+----+-------------------+-------+
| 43 |    CLOSE_CARET    |   >   |
+----+-------------------+-------+
| 44 |    ASSIGNMENT     |   =   |
+----+-------------------+-------+
| 45 |   INT_CONSTANT    |   3   |
+----+-------------------+-------+
| 46 |    IDENTIFIER     |  sut  |
+----+-------------------+-------+
| 47 |    OPEN_CARET     |   <   |
+----+-------------------+-------+
| 48 |    ASSIGNMENT     |   =   |
+----+-------------------+-------+
| 49 |   INT_CONSTANT    |   5   |
+----+-------------------+-------+
| 50 |    CLOSE_PAREN    |   )   |
+----+-------------------+-------+
| 51 | OPEN_CURLY_BRACE  |   {   |
+----+-------------------+-------+
| 52 |    IDENTIFIER     |   x   |
+----+-------------------+-------+
| 53 |    ASSIGNMENT     |   =   |
+----+-------------------+-------+
| 54 |   INT_CONSTANT    |  30   |
+----+-------------------+-------+
| 55 |     SEMICOLON     |   ;   |
+----+-------------------+-------+
| 56 | CLOSE_CURLY_BRACE |   }   |
+----+-------------------+-------+
| 57 |       ELSE        | else  |
+----+-------------------+-------+
| 58 | OPEN_CURLY_BRACE  |   {   |
+----+-------------------+-------+
| 59 |    IDENTIFIER     |   x   |
+----+-------------------+-------+
| 60 |    ASSIGNMENT     |   =   |
+----+-------------------+-------+
| 61 |   INT_CONSTANT    |  60   |
+----+-------------------+-------+
| 62 |     SEMICOLON     |   ;   |
+----+-------------------+-------+
| 63 | CLOSE_CURLY_BRACE |   }   |
+----+-------------------+-------+
| 64 |    IDENTIFIER     |   x   |
+----+-------------------+-------+
| 65 |    ASSIGNMENT     |   =   |
+----+-------------------+-------+
| 66 |    OPEN_PAREN     |   (   |
+----+-------------------+-------+
| 67 |    IDENTIFIER     |   x   |
+----+-------------------+-------+
| 68 |      DIVIDE       |   /   |
+----+-------------------+-------+
| 69 |    OPEN_PAREN     |   (   |
+----+-------------------+-------+
| 70 |    IDENTIFIER     |  sut  |
+----+-------------------+-------+
| 71 |       PLUS        |   +   |
+----+-------------------+-------+
| 72 |   INT_CONSTANT    |   2   |
+----+-------------------+-------+
| 73 |    CLOSE_PAREN    |   )   |
+----+-------------------+-------+
| 74 |    CLOSE_PAREN    |   )   |
+----+-------------------+-------+
| 75 |       MINUS       |   -   |
+----+-------------------+-------+
| 76 |   INT_CONSTANT    |   5   |
+----+-------------------+-------+
| 77 |     SEMICOLON     |   ;   |
+----+-------------------+-------+
| 78 |    IDENTIFIER     |   x   |
+----+-------------------+-------+
| 79 |    ASSIGNMENT     |   =   |
+----+-------------------+-------+
| 80 |    IDENTIFIER     |   x   |
+----+-------------------+-------+
| 81 |    IDENTIFIER     |  sut  |
+----+-------------------+-------+
| 82 |     SEMICOLON     |   ;   |
+----+-------------------+-------+
| 83 | CLOSE_CURLY_BRACE |   }   |
+----+-------------------+-------+
```