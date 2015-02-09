"""
****AFI Design Version 0.0.2****
AFI V0.0.2 will accept the following:
PMDAS (Parentheses, Multiplication, Division, Addition Subtraction) Expressions



"""

import sys
import os
import mathAFI
import lexAFI

#Main instructional function.
def main():
    version = "0.0.2"

    lexer = lexAFI.generateLexer()

    if len(sys.argv) == 1:
        print("Welcome to AFI V",version,"! Enter an expression below:", sep='')
        while 1:
            inputStr = input("|")

            for token in lexer.lex(inputStr):
                print(token)
                
    elif len(sys.argv) < 3:
        filename = sys.argv[1]
        fileext = ".afi"
        if fileext in filename:
            file = open(os.getcwd() + "\\" + filename)
            print(file.read())
        elif "." in filename:
            print("ERROR: wrong file extension, please use .afi")
        else:
            file = open(os.getcwd() + "\\" + filename + ".afi", r)
    else:
        print("Usage: python AFI.py <filename>")
main()
