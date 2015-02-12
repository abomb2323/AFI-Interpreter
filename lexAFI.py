"""

AFI Lexer Using RPly


"""

from rply import LexerGenerator

def generateLexer():
	afiLex = LexerGenerator()
	afiLex.ignore(r'\s+')
	afiLex.add("LBRACKET",r'\[')
	afiLex.add("RBRACKET",r'\]')
	afiLex.add("LPARENS",r'\(')
	afiLex.add("RPARENS",r'\)')
	afiLex.add("LBRACE", r'\{')
	afiLex.add("RBRACE", r'\}')
	afiLex.add("QUOTE", r'\"')
	afiLex.add("IF", r"if")
	afiLex.add("ELSE", r"else")
	afiLex.add("ELIF", r"elif")
	afiLex.add("WHILE", r"while")
	afiLex.add("NUMBER", r'\d+')
	#Fuck Regex, need to fix the delimiters to not include the '^' symbol..
	#afiLex.add("WORD", r"[a-zA-z_][a-zA-Z0-9][^\^]*")
	afiLex.add("EQUAL", r'\=')
	afiLex.add("ADD", r'\+')
	afiLex.add("SUB", r'\-')
	afiLex.add("MULT", r'\*')
	afiLex.add("DIV", r'\/')
	afiLex.add("POW", r'\^')
	return afiLex.build()