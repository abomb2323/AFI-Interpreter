"""
AFI Parser



"""

from rply import ParserGenerator

from rply.token import BaseBox

#AST Class for Comparing things
class Equivalence(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left == self.right

#Number AST class
#Number can have a value, derp
class Number(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

#Binary Operator AST class
#BinaryOp can have a left and a right, i.e. the things you're evaluating.
class BinaryOp(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right

#Addition class, self explanatory 
class Add(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()

#Subtraction class
class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()

#Multiplication Class
class Mult(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()

#Division Class
class Div(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()

#Power class
class Pow(BinaryOp):
	def eval(self):
		return self.left.eval() ** self.right.eval()

#Generating the parser's information, including what keywords will be used.
afiParser = ParserGenerator(
    # A list of all token names, accepted by the parser.
    ['LPARENS', 'RPARENS', 'NUMBER', 'ADD', 'SUB', 'MULT', 'DIV', 'POW', 'SEMICOLON', 'EQUAL'
    ],
    # A list of precedence rules with ascending precedence, to
    # disambiguate ambiguous production rules.
    precedence=[
    	
        ('left', ['ADD', 'SUB']),
        ('left', ['MULT', 'DIV']),
        ('left', ['POW'])
    ]
)

#A line is an expression followed by a semicolon
@afiParser.production('line : expression SEMICOLON')
def line(p):
    return p[0]

#An equivalence expression is an expression, followed by two equals signs, followed by another expression
@afiParser.production('expression : expression EQUAL EQUAL expression')
def equivalence_expression(p):
    return Equivalence(p[0], p[3])

#An expression can be a number
@afiParser.production('expression : NUMBER')
def expression_number(p):
    # p is a list of the pieces matched by the right hand side of the
    # rule
    return Number(int(p[0].getstr()))

#An expression can also be an expression inside parentheses
@afiParser.production('expression : LPARENS expression RPARENS')
def expression_parens(p):
    return p[1]

#An expression can also be in PEMDAS form
@afiParser.production('expression : expression ADD expression')
@afiParser.production('expression : expression SUB expression')
@afiParser.production('expression : expression MULT expression')
@afiParser.production('expression : expression DIV expression')
@afiParser.production('expression : expression POW expression')
#What to do when a binary operator is used
def expression_binop(p):
    left = p[0]
    right = p[2]
    if p[1].gettokentype() == 'ADD':
        return Add(left, right)
    elif p[1].gettokentype() == 'SUB':
        return Sub(left, right)
    elif p[1].gettokentype() == 'MULT':
        return Mult(left, right)
    elif p[1].gettokentype() == 'DIV':
        return Div(left, right)
    elif p[1].gettokentype() == 'POW':
    	return Pow(left, right)
    else:
        raise AssertionError('Oops, this should not be possible!')


#Error handler, if it runs into a token that isn't expected.
@afiParser.error
def error_handler(token):
	raise ValueError("Ran into a %s where it wasn't expected" % token.gettokentype())

#Build yo parsers
parser = afiParser.build()

#Function to allow access to the parser from other files.
def getParser():
	return parser