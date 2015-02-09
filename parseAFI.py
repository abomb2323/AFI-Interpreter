"""
AFI Parser



"""

from rply import ParserGenerator

import astAFI

def generateParser():

	afiParser = ParserGenerator(
	#A list of token names accepted by the Parser
		["LBRACKET", "RBRACKET", "LBRACE", "RBRACE", "LPARENS", "RPARENS",
	 	 "QUOTE", "IF", "ELSE", "ELIF", "WHILE", "NUMBER",
	 	 "WORD", "EQUAL", "ADD", "SUB", "MULT", "DIV", "POW"
		]
	)

	
