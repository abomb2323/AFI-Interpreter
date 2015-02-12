"""
AFI Parser



"""

from rply import ParserGenerator

from rply.token import BaseBox

class Number(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

class BinaryOp(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Add(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()

class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()

class Mult(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()

class Div(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()

class Pow(BinaryOp):
	def eval(self):
		return self.left.eval() ** self.right.eval()

afiParser = ParserGenerator(
    # A list of all token names, accepted by the parser.
    ['LPARENS', 'RPARENS', 'NUMBER', 'ADD', 'SUB', 'MULT', 'DIV', 'POW'
    ],
    # A list of precedence rules with ascending precedence, to
    # disambiguate ambiguous production rules.
    precedence=[
    	
        ('left', ['ADD', 'SUB']),
        ('left', ['MULT', 'DIV']),
        ('left', ['POW'])
    ]
)

@afiParser.production('expression : NUMBER')
def expression_number(p):
    # p is a list of the pieces matched by the right hand side of the
    # rule
    return Number(int(p[0].getstr()))

@afiParser.production('expression : LPARENS expression RPARENS')
def expression_parens(p):
    return p[1]

@afiParser.production('expression : expression ADD expression')
@afiParser.production('expression : expression SUB expression')
@afiParser.production('expression : expression MULT expression')
@afiParser.production('expression : expression DIV expression')
@afiParser.production('expression : expression POW expression')
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

@afiParser.error
def error_handler(token):
	raise ValueError("Ran into a %s where it wasn't expected" % token.gettokentype())

parser = afiParser.build()

def getParser():
	return parser