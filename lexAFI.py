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
	afiLex.add("NUMBER", r'\d+')
	afiLex.add("WORD", r"[a-zA-z_][a-zA-Z0-9]*")
	afiLex.add("EQUAL", r'\=')
	afiLex.add("ADD", r'\+')
	afiLex.add("SUB", r'\-')
	afiLex.add("MULT", r'\*')
	afiLex.add("DIV", r'\/')
	afiLex.add("POW", r'\^')
	return afiLex.build()