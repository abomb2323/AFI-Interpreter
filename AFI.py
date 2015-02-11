"""
****AFI Design Version 0.0.2****
AFI V0.0.2 will accept the following:
PMDAS (Parentheses, Multiplication, Division, Addition Subtraction) Expressions



"""

import sys
import os
import mathAFI
import lexAFI
import parseAFI

#Main instructional function.
def main():
    version = "0.0.2"

    lexer = lexAFI.generateLexer()
    parser = parseAFI.getParser()

    if len(sys.argv) == 1:
        print("Welcome to AFI V",version,"! Enter an expression below:", sep='')
        while 1:
            inputStr = input("|")
            print("|" + str(parser.parse(lexer.lex(inputStr))))

    elif len(sys.argv) < 3:
        filename = sys.argv[1]
        fileext = ".afi"
        if fileext in filename:
            file = open(os.getcwd() + "\\" + filename)
            
            for line in file:
                for token in lexer.lex(line):
                    print(parser.parse(token).eval())

        elif "." in filename:
            print("ERROR: wrong file extension, please use .afi")
        else:
            file = open(os.getcwd() + "\\" + filename + ".afi")
            for line in file:
                for token in lexer.lex(line):
                    print(token)
    else:
        print("Usage: python AFI.py <filename>")
main()
