import re
from tabulate import tabulate
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

optAssg = r'(\+=|\-=|\*=|\/=|\%=|\~=)'
optArtm = r'(\=|\+|\-|\*|\/|\%|\~|\^)'
optUni = r'(\+\+|\-\-|\+|\-)'
optLog = r'(\!|\|\||&&)'
optRel = r'(==|!=|><|>=|<=)'

# Define the tokens using regular expressions
tokens = [
    ('NUMBER', r'\d+(\.\d*)?'),  # Matches numbers, including decimal numbers
    ('KEYWORD', r'(false|none|true|and|as|assert|break|class|'
                r'continue|def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal|'
                r'not|or|pass|raise|return|try|while|with|yield|print)'),  # Matches keywords
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),  # Matches identifiers
    ('OPERATOR_ASSIGNMENT', optAssg),  # Matches operator assignment
    ('OPERATOR_ARITHMETIC', optArtm),  # Matches operators arithmetic
    ('UNARY_OPERATOR', optUni),  # Matches unary operators
    ('OPERATOR_LOGIC', optLog),  # Matches operator logic
    ('OPERATOR_RELATION', optRel),  # Matches operator relation
    ('AT_SIGN', r'@'),  # Matches the at sign
    ('APOSTROPHE', r"'"),  # Represent a single character and denotes character literals.
    ('QUOTATION_SIGN', r'"'),  # Denote string literals in programming
    ('COMMA', r','),  # Separator between elements in lists, parameters in function or method declarations, and arguments in function calls.
    ('COLON', r':'),  # Used to denote inheritance; used as part of switch/case or goto statements; used as part of ternary expressions; and used for specifying parameter names and generic type constraints.
    ('SEMICOLON', r';'),  # Used to terminate a line of code
    ('LBRACE', r'{'),  # Used to define blocks of code
    ('RBRACE', r'}'),  # Used to define blocks of code
    ('LPAREN', r'\('),  # Used to enclose expressions, conditions, parameters, arguments, functions, and methods
    ('RPAREN', r'\)'),  # Used to enclose expressions, conditions, parameters, arguments, functions, and methods
    ('LBRACKET', r'\['),  # Used for array declarations and indexing.
    ('RBRACKET', r'\]'),  # Used for array declarations and indexing.
    ('COMMENT', r'//.*|/\*(.|\n)*?\*/'),  # Used at the beginning of writing single-line comments.
    ('DATA_BINDING_START', r'<%'),  # Matches the start of data binding
    ('DATA_BINDING_END', r'%>'),  # Matches the end of data binding
    ('WHITE_SPACE', r'[ ]+'),  # Matches whitespace (to be skipped)
    ('VALUE_SIGN', r':'),  # Matches the value sign
    ('NEWLINE', r'\n'),  # Matches newline character
    ('ERROR', r'.'), # Matches error character as error
]

pattern = '|'.join('(?P<%s>%s)' % pair for pair in tokens)

lexer = re.compile(pattern)

def determine_token_type(lexeme):
    if lexeme[0].isalpha():
        return 'variable'
    elif lexeme.isdigit():
        return 'int literal'
    else:
        return 'unknown'

def tokenize(input_string):
    pos = 0
    while pos < len(input_string):
        match = lexer.match(input_string, pos)
        if match:
            token_type = match.lastgroup
            token_value = match.group()
            if token_type != 'WHITE_SPACE' and token_type != 'NEWLINE':
                lexeme_type = determine_token_type(token_value)
                yield token_type, token_value, lexeme_type
            pos = match.end()
        else:
            print(f"Lexer Error: Unexpected character '{input_string[pos]}' at position {pos}")
            break

def generate_strings(input_string):
    # Display incremental strings
    print("Generated String:")
    print(input_string)

def generate_lexical_table_pdf(tokens_list):
    print("Generated Tokens:")
    print("{:<15}{}".format("Lexeme", "Token"))
    print("-" * 30)

    for token_type, token_value, lexeme_type in tokens_list:
        print("{:<15}{}".format(token_value, lexeme_type))

    print("-" * 30)

def scan_characters(input_string):
    current_lexeme = ""
    data = []  # List to store data for tabulate
    tokens_list = []  # List to store recognized tokens

    for position, char in enumerate(input_string):
        current_lexeme += char
        token_type = None

        # Use the lexer to find matches
        match = lexer.match(input_string, position)
        if match:
            token_type = match.lastgroup

        if token_type:
            lexeme_type = determine_token_type(current_lexeme)
            tokens_list.append((current_lexeme, token_type, lexeme_type))
            status = f'Recognized: {token_type} ({lexeme_type})'
        else:
            status = 'Not Recognized'

        data.append([position + 1, repr(current_lexeme), status])

    # Print the table
    print(tabulate(data, headers=["Position", "Character", "Status"], tablefmt="fancy_grid"))


def input_and_display():
    print("Enter data (press Enter to finish):")
    user_input = ""
    while True:
        line = input()
        if not line:
            break
        user_input += line + "\n"

        # Display incremental strings
        generate_strings(user_input)

        # Store tokens in a list for generating the lexical table PDF
        tokens_list = list(tokenize(user_input))

        # Scan and recognize each character
        scan_characters(user_input.strip())  # Strip newline characters


if _name_ == "_main_":
    input_and_display()