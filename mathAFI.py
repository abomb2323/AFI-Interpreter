"""

AFI Basic Math Operations Library (BMOL) Ver. 0.0.2

Current supported operations:
*Addition
*Subtraction
*Multiplication
*Division

"""
import re
 
LEFT_PAREN = '('
RIGHT_PAREN = ')'
OP_PLUS = '+'
OP_MINUS = '-'
OP_MULT = '*'
OP_DIV = '/'
OP_POW = '^'
OP_ATTR = {
    OP_PLUS: {'prcd': 1, 'fn': lambda a, b: add(a, b)},
    OP_MINUS: {'prcd': 1, 'fn': lambda a, b: sub(a, b)},
    OP_MULT: {'prcd': 2, 'fn': lambda a, b: mult(a, b)},
    OP_DIV: {'prcd': 2,'fn': lambda a, b: div(a, b)},
    OP_POW: {'prcd': 3, 'fn' : lambda a, b: a**b },
}
sep_re = re.compile(r'\s*(%s|%s|%s|%s|%s|%s|%s)\s*' % (
                    re.escape(LEFT_PAREN),
                    re.escape(RIGHT_PAREN),
                    re.escape(OP_PLUS),
                    re.escape(OP_MINUS),
                    re.escape(OP_MULT),
                    re.escape(OP_DIV),
                    re.escape(OP_POW)))
 
def tokenize(expr):
    return [t.strip() for t in sep_re.split(expr.strip()) if t]
 
 
def in2postfix(tokens):
    opstack = []
    postfix = []
    for t in tokens:
        if t in OP_ATTR:
            while len(opstack)>0 and opstack[-1] in OP_ATTR\
                  and OP_ATTR[t]['prcd'] <= OP_ATTR[opstack[-1]]['prcd']:
                postfix.append(opstack.pop())
            opstack.append(t)
        elif t == LEFT_PAREN:
            opstack.append(t)
        elif t == RIGHT_PAREN:
            while opstack[-1] != LEFT_PAREN:
                postfix.append(opstack.pop())
            opstack.pop()
        else:
            postfix.append(t)
    postfix.extend(reversed(opstack))
    return postfix
 
 
def calc_postfix(tokens):
    result, stack = 0, []
    for tok in tokens:
        if tok in OP_ATTR:
            op1, op2, result = stack.pop(), stack.pop(), 0
            try:
                stack.append(OP_ATTR[tok]['fn'](op2, op1))
            except ZeroDivisionError:
                raise ValueError('%s %s %s ?!' % (op2, tok, op1))
        else:
            stack.append(float(tok))
    if len(stack) != 1:
        raise ValueError("INVALID EXPRESSION: operators and operands don't match")
    return stack.pop()
 
 
def calculate(expr):
    tokens = tokenize(expr)
    postfix = in2postfix(tokens)
    return calc_postfix(postfix)



#Adds two integer together.
def add(a, b):
    ans = float(a) + float(b)
    if ans.is_integer():
        return int(ans)
    return ans

#Subtracts two numbers
def sub(a, b):
    ans = float(a) - float(b)
    if ans.is_integer():
        return int(ans)
    return ans

#Multiplies two numbers together.
def mult(a, b):
    ans = float(a) * float(b)
    if ans.is_integer():
        return int(ans)
    return ans

#Divides two numbers
def div(a, b):
    if float(b) == 0:
        return "ERROR: DIV BY ZERO"
    else:
        ans = float(a)/float(b)
        if ans.is_integer():
            return int(ans)
        return ans

