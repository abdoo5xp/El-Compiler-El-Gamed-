import exc as ex 
// ahaaa

symbol_table = {}

def parse(toks):
	i = 0
	#print(toks)
	while(i < len(toks)):
		if toks[i] == "PRINT":          
			if toks[i+1][0:6] =="STRING":      #here i am printing only strings 
				#print("FOUND STRING ")
				string = getVal(toks[i+1])
				
				# if "%d" in string:
				# 	clean_string = ""        #Initialize result string
				# 	for character in string:
				# 		if character.isalnum():        #a function that allows only characters and digits
				# 			clean_string += character   # Add alphanumeric characters
				# 	print(clean_string)
				# 	string += getVal(toks[i+2])
				# 	i+=1

				print(string)
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
		elif toks[i] == "INPUT":  # input STRING:"sth" VAR:$var_name
			if toks[i+1][0:6] == "STRING" and toks[i+2][0:3] == "VAR": # i was gonna make another if inside for string and other types but python saves input as a string so screw it.                
				getInput(getVal(toks[i+1]),toks[i+2][5:])	
			i+=3
		# elif toks[i] == "IF":  # input STRING:"sth" VAR:$var_name
		# 	if toks[i+1][0:3] is "VAR":
		# 		if toks[i+2][0:6] == "STRING":
		# 			getInput(getVal(toks[i+1]),toks[i+2][5:])	
		# 	i+=3 
	print("my symbol table :",symbol_table)
	

def getInput(string_to_be_printed, varname):
	i ="STRING:"+ input(string_to_be_printed +" ") # i tried python and it saves it as a STRING 
	makeVar(varname,i)


def makeVar(varname,varvalue):
	symbol_table[varname] = varvalue


def getVar(varname):
	if varname in symbol_table:	
			return symbol_table[varname]
	else:
		print("undefined variable")
		exit()

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
		name = token[5:]   # this is the variable name that i wanna get its value from its table 
		token = getVar(name)
		token = getVal(token)       # i am awesome <3 <3 
	#print(token)
	return token
