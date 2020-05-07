
def lex(filecontents):
	tokens = []
	tok = ""
	string = ""
	num = ""
	exp = ""
	condition = ""
	iscomment = 0
	state = 0    # state a flage to check of this tok is inside a string or not 
	isexp = 0
	iscondition = 0
	varstarted = 0
	var = ""     
	special_characters = "~!@#$%^&*()+/*-`<>"
	filecontents = list(filecontents)
	#print(filecontents)
	for char in filecontents:
		tok += char
		if tok in " \t":
			if state == 0:
				tok = ""
		elif tok == "\n" or tok == "<EOF>" :  # to read multiple lines 
			if exp != "" and isexp == 1:
				#print(exp + "Exp")
				tokens.append("EXP:" + exp)
				exp =""		
			elif exp != "" and isexp == 0:
				#print(exp +"num")
				tokens.append("NUM:" + exp)
				exp = ""
			elif var != "":
				tokens.append("VAR:" + var)
				varstarted = 0  
				var = ""
			tok=""
			iscomment = 0
		elif tok is "#":
			iscomment = 1
		elif iscomment:
			tok=""
		elif tok.upper() == "PRINT":       #To take upper and lower case "print"
			tokens.append("PRINT")
			tok=""
		elif tok.upper() == "INPUT":       #To take upper and lower case "input"
			tokens.append("INPUT")
			tok=""
		elif tok.upper() == "IF":       #To take upper and lower case "input"
			tokens.append("IF")
			#iscondition = 1          lets continue in another time 
			tok=""
		elif tok.upper() == "THEN":       #To take upper and lower case "input"
			if exp != "" and isexp == 0:
				#print(exp +"num")
				tokens.append("NUM:" + exp)
				exp = ""
			tokens.append("THEN")
			tok=""
		elif tok.upper() == "ENDIF":       #To take upper and lower case "input"
			tokens.append("ENDIF")
			tok=""
		# elif iscondition:
		# 	condition += tok
		# 	tok=""
		elif tok in "0123456789" and varstarted == 0: #i have added this so we can variable names can have numbers 
			exp += tok  
			tok = ""
		elif tok in "+-*/()%":
			isexp = 1
			exp += tok
			tok = ""
		elif tok == "=" and state == 0:
			if exp != "" and isexp == 0:
				#print(exp +"num")
				tokens.append("NUM:" + exp)
				exp = ""
			if var != "":               
				tokens.append("VAR:" + var)    
				varstarted = 0  
				var = ""
			if tokens[-1] is "EQUALS":
				tokens[-1] = "EQEQ"
			else:
				tokens.append("EQUALS")
			tok = ""
		elif tok == "$" and state == 0:
			varstarted = 1
			var += tok
			tok = ""
		elif varstarted == 1:
			if tok in special_characters:
				varstarted = 0
				continue 
			# if tok in "<":        # if the file ends with a variable the <EOF> gets appended to the var name and the program doesn't get into the condition of tok == <EOF>
			# 	varstarted = 0	  # so i wrote this condition
			# 	continue 
			#print(tok)
			var += tok        # saving the variable name
			#print(var)
			#print("the tok ",tok)
			tok = "" 
		elif tok in " \"":
			if state == 0:    # this is state for telling the compiler this is the first of the string start saving characters 
				state = 1
				tok = ""       # i have added this to not add the " with the string
			elif state == 1:  # this one is for the end of the string to tell te compiler the string has ended. 
				tokens.append("STRING:" + string)
				state = 0
				string = ""
				tok = ""
		elif state == 1: 
			string += tok  # saving the string  
			tok = ""
			
	#print (exp)
	print(tokens)
	return tokens
	#return ''
