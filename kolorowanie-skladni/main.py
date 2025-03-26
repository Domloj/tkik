import argparse
from tokens import whiteSpaces, numbers, letters, Inital, End, Operators, Brackets, LogicExp, KeyWords

def scanner(expression: str, position: int) -> tuple[str, str, int]:
    token = ''
    char = expression[position]
    position += 1

    if char in Operators:
        if position < len(expression):
            token = char + expression[position]
            if token in LogicExp:
                position += 1
                return token, LogicExp[token], position
            else:
                return char, Operators[char], position
        return char, Operators[char], position
    
    if char in Brackets:
        return char, Brackets[char], position

    if char in numbers:
        token += char
        while position < len(expression) and expression[position] in numbers:
            token += expression[position]
            position += 1
        return token, "number", position
    
    if char in letters:
        token += char
        while position < len(expression) and (expression[position] in numbers or expression[position] in letters):
            token += expression[position]
            position += 1
        return token, token, position

    raise Exception()

def process_expression(expression: str, position: int, row: int, columns: int, output, comment_line: bool, comment_block: bool, text: bool) -> tuple[int, bool, bool, bool]:
    try:
        while position < len(expression):
            token, value, position = scanner(expression, position)
            #print(f'Token: {token}, value: {value}, row: {row}, column: {position + columns - len(token)}')
            print(f'{token} : {value}')

            if value == "comment_block_start":
                comment_block = True

            if value == "comment_line":
                comment_line = True
            
            if value == "comment_block_end":
                comment_block = False
            
            if comment_line or comment_block:
                value = "comment_line"
            
            if value == "double_quotation" and not text:
                text = True
            elif value == "double_quotation" and text:
                text = False

            if text:
                value = "text"

            if value in KeyWords:
                output.write("<span class=\"" + KeyWords[value] + "\">" + token + "</span>")
            else: 
                output.write(token)
        return position, comment_line, comment_block, text
    except Exception as e:
        print(f'Nieoczekiwany znak: {expression[position]} w row: {row}, column: {position + columns}')

def main():
    parser = argparse.ArgumentParser(description="Podaj plik wejściowy do skanera")
    parser.add_argument("-file", required=True ,help="Path to file with input data")
    args = parser.parse_args()
    file_name = args.file
    
    output_file = open("output.html", "w")
    output_file.write(Inital)

    try:
        with open(file_name, "r") as file:
            position = 0
            row = 1
            columns = 1
            expression = ""
            comment_line = False
            comment_block = False
            text = False

            while (char := file.read(1)):
                if char in whiteSpaces:
                    position, comment_line, comment_block, text = process_expression(expression, position, row, columns, output_file, comment_line, comment_block, text)
                    output_file.write(char)
                    columns += len(expression) + 1
                    expression = ""
                    position = 0
                    if char == '\n': 
                        row += 1
                        columns = 1
                        comment_line = False
                else:
                    expression = expression + char

            if expression:
                _, _, _, _ = process_expression(expression, position, row, columns, output_file, comment_line, comment_block, text)

    except Exception as e:
        output_file.close()
        raise ValueError(e)

    output_file.write(End)
    output_file.close()

if __name__ == "__main__":
    main()