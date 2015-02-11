"""
AFI Parser



"""

from rply import ParserGenerator

import mathAFI

class Node(object):
	def __eq__(self, other):
		if not isinstance(other, Node):
			return NotImplemented
		return (type(self) is type(other) and self.__dict__ == other.__dict__)
	def __ne__(self, other):
		return not (self == other)

class Block(Node):
	def __init__(self, statements):
		self.statements = statements

#Statement Node
class Statement(Node):
	def __init__(self, expr):
		self.expr = expr

#Number Node
class Number(Node):
	def __init__(self, value):
		self.value = value

	def eval(self):
		return self.value

class MathExpr(Node):
	def __init__(self, expr):
		self.expr = expr

	def eval(self):
		return mathAFI.calculate(self.expr)

afiParser = ParserGenerator(
#A list of token names accepted by the Parser
	["LBRACKET", "RBRACKET", "LBRACE", "RBRACE", "LPARENS", "RPARENS",
 	 "QUOTE", "IF", "ELSE", "ELIF", "WHILE", "NUMBER",
 	 "WORD", "EQUAL", "ADD", "SUB", "MULT", "DIV", "POW"
	],
	cache_id="afiparser"
)



@afiParser.production('expression : NUMBER')
def expression_number(p):
	# p is a list of the pieces matched by the right hand side of the rule
	return Number(int(p[0].getstr())).eval()

@afiParser.production('expression : LPARENS expression RPARENS')
def expression_parens(p):
	return p[1]	



@afiParser.production('expression : expression ADD expression')
def expression_add(p):
	return '+'

# @afiParser.production('expression : expression SUB expression')
def expression_sub(p):
	return '-'

@afiParser.production('expression : expression MULT expression')
def expression_mult(p):
	return '*'

@afiParser.production('expression : expression DIV expression')
def expression_div(p):
	return '/'

@afiParser.production('expression : expression POW expression')
def expression_pow(p):
	return '^'

@afiParser.production('expression : LBRACE expression RBRACE')
def expression_mathexpr(p):
	print(p)
	return MathExpr(p[1]).eval()


afiparse = afiParser.build()

def getParser():
	return afiparse