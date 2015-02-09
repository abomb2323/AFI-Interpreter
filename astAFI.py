"""

AST Functions for AFI


"""

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