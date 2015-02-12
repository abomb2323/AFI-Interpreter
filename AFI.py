"""
****AFI Interpreter****
Author: Adam Crick
Date: 2/12/2015
Version: 0.1.0:1

"""

import sys
import os
import lexAFI
import parseAFI

#Main instructional function.
def main():
    #Version Number, follows APIVer.MajorVer.MinorVer:Bugfix#
    version = "0.1.0:1"

    #Pull the lexer and parser from the other files.
    lexer = lexAFI.generateLexer()
    parser = parseAFI.getParser()

    #If we have no arguments, i.e. Just running the parser, not a file.
    if len(sys.argv) == 1:
        print("Welcome to AFI V",version,"! Enter an expression below:", sep='')
        while 1:
            inputStr = input("|")
            print("|" + str(parser.parse(lexer.lex(inputStr)).eval()))
    #If we're opening a file
    elif len(sys.argv) < 3:
        #Filename comes from the commandline arguments, file extension is .afi
        filename = sys.argv[1]
        fileext = ".afi"

        #If our user decided to remember the file extension
        if fileext in filename:
            file = open(os.getcwd() + "\\" + filename)
            
            for line in file:
                print("|" + str(parser.parse(lexer.lex(line)).eval()))
        #If they put in another file extension
        elif "." in filename:
            print("ERROR: wrong file extension, please use .afi")
        #If they forgot the file extension, still opens.
        else:
            file = open(os.getcwd() + "\\" + filename + ".afi")
            for line in file:
                print("|" + str(parser.parse(lexer.lex(line)).eval()))
    else:
        print("Usage: python AFI.py <filename>")

main()
