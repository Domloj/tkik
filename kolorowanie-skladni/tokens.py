whiteSpaces = [' ', '\n', '\t', '\r']

Operators = {
	"+": "plus",
	"-": "minus",
	"*": "multiply",
	"/": "divide",
	"=": "assign",
	"%": "modulo",
	"<": "less",
	">": "more",
	",": "comma",
	".": "dot",
	";": "semicolon",
	":": "colon",
	"_": "floor",
	"!": "negation",
	'\'' : "single_quotation",
	"\"" : "double_quotation",
	"&" : "half_conjuction",
	"|" : "half_alternative",
}

Brackets = {
	'(': "Param_L",
	')': "Param_P",
	'{': "Curly_L",
	'}': "Curly_P",
	'[': "Square_L",
	']': "Square_P",
}

LogicExp = {
	"&&" : "conjuction",
	"||" : "alternative",
	":=" : "colon_assign",
	"==" : "comparison",
	"!=" : "neg_comparison",
	"<=" : "less_equal",
	">=" : "more_equal",
	"++" : "increase",
	"--" : "decrease",
	"//" : "comment_line",
	"/*" : "comment_block_start",
	"*/" : "comment_block_end",
}

KeyWords = {
	"if" : "if",
	"else" : "else",
	"for" : "for",
	"return" : "return",
	"func" : "func",
	"var" : "var",
	"string" : "type",
	"int" : "type",
	"print" : "print",
	"plus" : "operator",
	"minus" : "operator",
	"multiply" : "operator",
	"divide" : "operator",
	"assign" : "operator",
	"colon_assign" : "operator",
	"modulo" : "operator",
	"less" : "comparison",
	"more" : "comparison",
	"comma" : "seperators",
	"dot" : "seperators",
	"semicolon" : "seperators",
	"floor" : "seperators",
    "colon" : "operator",
	"negation" : "operator",
	"increase" : "operator",
	"decrease" : "operator",
	"conjuction" : "logic",
	"alternative" : "logic",
	"comparison" : "comparison",
	"neg_comparison" : "comparison",
	"less_equal" : "comparison",
	"more_equal" : "comparison",
	"Param_L" : "brackets",
	"Param_P" : "brackets",
	"Curly_L" : "brackets",
	"Curly_P" : "brackets",
	"Square_L" : "brackets",
	"Square_P" : "brackets",
	"single_quotation" : "text",
	"double_quotation" : "text",
	"text" : "text",
	"comment_line" : "comment",
	"comment_block_start" : "comment",
	"comment_block_end" : "comment",
	"number" : "number",
}

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

letters = [
	"a", "b", "c", "d", "e", "f",
	"g", "h", "i", "j", "k", "l",
	"m", "n", "o", "p", "q", "r",
	"s", "t", "u", "v", "w", "x",
	"y", "z",

	"A", "B", "C", "D", "E", "F",
	"G", "H", "I", "J", "K", "L",
	"M", "N", "O", "P", "Q", "R",
	"S", "T", "U", "V", "W", "X",
	"Y", "Z"]

Inital = """<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Code</title>
    <style>
        body {
            background-color: #1e1e1e;
            color: white;
            font-family: Consolas, monospace;
            font-size: large;
        }
        .if { color:rgb(255, 0, 144); }   /* Malinowy */
        .else { color: #00a2ff; }   /* Niebieski */
        .for { color:rgb(159, 0, 251); }   /* Fioletowy */
        .return { color:rgb(0, 47, 255); }   /* Granatowy */
        .func { color:rgb(255, 0, 217); }   /* Różowy */
        .var { color: #ff7700; }   /* Pomarańczowy */
        .type { color:rgb(255, 242, 0); }      /* Żółty */
        .number { color:rgb(115, 255, 0); }    /* Seledynowy */
        .operator { color:rgb(145, 108, 71); }  /* Brązowy */
        .comment { color:rgb(0, 188, 25); }   /* Zielony */
        .brackets { color:rgb(255, 0, 0); }  /* Czerowny */
        .seperators { color: #faffe8; }  /* Biały */
        .logic { color:rgb(0, 238, 255); }  /* Turkusowy */
        .comparison { color:rgb(255, 225, 0); } /* Seledynowy */
        .print { color:rgb(0, 174, 255); } /* Niebieski */
		.text { color:rgb(6, 194, 34); } /* Zielony */
    </style>
</head>
<body>
<pre>
"""

End = """
</pre>
</body>
</html>
"""