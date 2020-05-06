import exc as ex 

symbol_table = {}

def parse(toks):
	i = 0
	#print(toks)
	while(i < len(toks)):
		if toks[i] == "PRINT":          
			if toks[i+1][0:6] =="STRING":      #here i am printing only strings 
				#print("FOUND STRING ")
				#print(toks[i+1][7:])
				print(getVal(toks[i+1]))
			elif toks[i+1][0:3] =="VAR":
				print(getVal(toks[i+1]))
			i+=2		
		elif toks[i][0:3] == "NUM":    
			#print(toks[i][4:])
			getVal(toks[i])
			i+=1
		elif toks[i][0:3] == "EXP": 
			#print(toks[i][4:])
			getVal(toks[i])
			i+=1
		elif toks[i][0:3] == "VAR":  # this is the token --> 'VAR:$var_name''EQUALS''TYPE:var_value'
			if toks[i+1] == "EQUALS":       
				if toks[i+2][0:3] in "EXP": 
					makeVar(toks[i][5:], "NUM:"+ getVal(toks[i+2])) # here i didn't use str(getval(toks[i+2])) cause the return of my getval is a string 
				elif toks[i+2][0:3] in "NUM":
					makeVar(toks[i][5:], toks[i+2])
				elif toks[i+2][0:6] == "STRING":
					makeVar(toks[i][5:],toks[i+2])  					#print(toks[i][5:]+" "+ "\"" + toks[i+2][7:] + "\"") # i have added the "" to the string back, and removed this $ 	
				elif toks[i+2][0:3] in "VAR": 
					makeVar(toks[i][5:],getVal(toks[i+2]))
			i+=3
	print("my symbol table :",symbol_table)
			

def makeVar(varname,varvalue): 
	symbol_table[varname] = varvalue


def getVal(token):
	if token[0:6]=="STRING":
		token = token[7:]
		#token = token[-1]
	elif token[0:3] == "NUM":
		token = token[4:]
	elif token[0:3] == "EXP":
		#print("EXP is here ")
		token = ex.evaluate(ex.evalExp(token[4:]))
		#token = token[-1]
	elif token[0:3] == "VAR":  #'VAR:$var_name''EQUALS''TYPE:var_value'
		token = token[5:]   # this is the variable name that i wanna get its value from its table 
		if token in symbol_table:	
			token = symbol_table[token]
			#print("checking on my token ",token)
			token = getVal(token)       # i am awesome <3 <3 
		else:
			print("undefined variable")

	#print(token)
	return token
