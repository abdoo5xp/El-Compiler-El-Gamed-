from sys import *
import FileRead as FR 
import lexer as lx  
import Parser as ps 

def run():
	ps.parse(lx.lex(FR.open_file(argv[1])))
	#evaluate()

run()
