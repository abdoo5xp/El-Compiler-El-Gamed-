from sys import *
import FileRead as FR 
import lexer as lx  
import Parser as ps

def run():
	
	if len(argv) > 1:
		ps.parse(lx.lex(FR.open_file(argv[1])))
	#evaluate()
	else:
		while True:
			data = input("A&A >")
			ps.parse(lx.lex(data))


run()