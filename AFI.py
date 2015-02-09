"""
****AFI Design Version 0.0.2****
AFI V0.0.2 will accept the following:
PMDAS (Parentheses, Multiplication, Division, Addition Subtraction) Expressions



"""

import sys
import mathAFI

#Takes input string, splits the spaces, and figures out what to do with it
def execCmd(inputStr):

    return mathAFI.calculate(inputStr)


#Main instructional function.
def main():
    version = "0.0.2"
    if len(sys.argv) == 1:
    	print("Welcome to AFI V",version,"! Enter an expression below:", sep='')
    	while 1:
        	inputStr = input("|")
        	print("|" + str(execCmd(inputStr)), sep='')
    elif len(sys.argv) < 3:
    	filename = sys.argv[1]
        if ".afi" in filename:
            file = open(filename, r)
        elif "." in filename:
            print("ERROR: wrong file extension, please use .afi")
        else:
            file = open(filename + ".afi", r)
    else:
    	print("Usage: python AFI.py <filename>")
main()
