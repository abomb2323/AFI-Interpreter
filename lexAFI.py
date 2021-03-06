"""

AFI Lexer Using RPly


"""

from rply import LexerGenerator

#Generate dem lexers
#Tokens are used with RegEx to figure shit out.
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
	afiLex.add("WORD", r"\w+[^\^;]")
	afiLex.add("EQUAL", r'\=')
	afiLex.add("ADD", r'\+')
	afiLex.add("SUB", r'\-')
	afiLex.add("MULT", r'\*')
	afiLex.add("DIV", r'\/')
	afiLex.add("POW", r'\^')
	afiLex.add("SEMICOLON", r'\;')
	return afiLex.build()