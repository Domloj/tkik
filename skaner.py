def scanner(char):
    result = ''

    TOKENS_CODES = {'NUMBER': 1,
                   'IDENTIFIER': 2,
                   'PLUS': 3,
                   'MINUS': 4,
                   'MULTIPLY': 5,
                   'DIVIDE': 6,
                   'LPAREN': 7,
                   'RPAREN': 8}

    def is_whitespace(char):
        if char == ' ' or char == '\t' or char == '\n':
            return True

    def is_number(char):
        if '0' <= char <= '9':
            return 'NUMBER'
        return None

    def is_char(char):
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            return 'IDENTIFIER'
        return None

    def is_other(char):
        TOKEN_OTHER = {
            '+': 'PLUS',
            '-': 'MINUS',
            '*': 'MULTIPLY',
            '/': 'DIVIDE',
            '(': 'LPAREN',
            ')': 'RPAREN'
        }
        return TOKEN_OTHER.get(char)

    if is_whitespace(char):
        return None

    result = is_number(char)
    if result:
        return result, char

    result = is_char(char)
    if result:
        return result, char

    result = is_other(char)
    if result:
        return result, char

    raise ValueError(f"ERROR: unknown character '{expression[position]}' in column {position}")

expression = '2+3*(76+8/3)ala+ 3\t*(9?-3)'
position = 0
while position < len(expression):
    char = expression[position]
    result = scanner(char)
    if result:
        k, w = result
        cur_k, cur_w = '',''
        while (k == cur_k or cur_k == ''):
            w+=cur_w
            position += 1
            if position >= len(expression):
                break
            result = scanner(expression[position])
            if result:
                cur_k, cur_w = result
        print(f'({k},{w})')
