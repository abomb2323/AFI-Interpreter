from distutils.core import setup
import py2exe, sys

sys.argv.append('py2exe')

setup(
    name = "AFI Interpreter",
    description = "Another Fucking Interpreter",
    author = "Adam Crick",
    author_email = "adam.crick@hotmail.com",
    version = "0.0.1",
    console = ["AFI.py"],
)
