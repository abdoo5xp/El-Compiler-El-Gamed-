
# from sys import *
# import FileRead as FR

# symbol_table = {}


# def open_file(filename):
# 	data = open(filename, "r").read()
# 	data += "<EOF>"
# 	return data 

def lex(filecontents):
	tokens = []
	tok = ""
	string = ""
	num = ""
	exp = ""
	state = 0    # state a flage to check of this tok is inside a string or not 
	isexp = 0
	varstarted = 0
	var = ""     
	special_characters = "~!@#$%^&*()+/*-`<>"
	filecontents = list(filecontents)
	#print(filecontents)
	for char in filecontents:
		tok += char
		if tok ==" ":
			if state == 0:
				tok = ""
		elif tok == "\n" or tok == "<EOF>":  # to read multiple lines 
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
		elif tok.upper() == "PRINT":          #or tok == "print":
			tokens.append("PRINT")
			tok=""
		elif tok in "0123456789" and varstarted == 0: #i have added this so we can variable names can have numbers 
			exp += tok  
			tok = ""
		elif tok in "+-*/()%":
			isexp = 1
			exp += tok
			tok = ""
		elif tok == "=" and state == 0:
			if var != "":               
				tokens.append("VAR:" + var)    
				varstarted = 0  
				var = ""
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
		elif tok == "\"":
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


# def parse(toks):
# 	i = 0
# 	#print(toks)
# 	while(i < len(toks)):
# 		if toks[i] == "PRINT":          
# 			if toks[i+1][0:6] =="STRING":      #here i am printing only strings 
# 				#print("FOUND STRING ")
# 				#print(toks[i+1][7:])
# 				getVal(toks[i+1])
# 			elif toks[i+1][0:3] =="VAR":
# 				getVal(toks[i+1])
# 			i+=2		
# 		elif toks[i][0:3] == "NUM":    
# 			#print(toks[i][4:])
# 			getVal(toks[i])
# 			i+=1
# 		elif toks[i][0:3] == "EXP": 
# 			#print(toks[i][4:])
# 			getVal(toks[i])
# 			i+=1
# 		elif toks[i][0:3] == "VAR":  # i have done this to help me with other variable types 
# 			if toks[i+1] == "EQUALS":
# 				if toks[i+2][0:3] in "EXP": 
# 					makeVar(toks[i][5:], "NUM:"+ getVal(toks[i+2])) # here i didn't use str(getval(toks[i+2]))
# 				elif toks[i+2][0:3] in "NUM":
# 					makeVar(toks[i][5:], toks[i+2])
# 				elif toks[i+2][0:6] == "STRING":
# 					makeVar(toks[i][5:],toks[i+2])  
# 					#print(toks[i][5:]+" "+ "\"" + toks[i+2][7:] + "\"") # i have added the "" to the string back, and removed this $ 	
# 			i+=3
# 	print("my symbol table :",symbol_table)
					
# def makeVar(varname,varvalue): 
# 	symbol_table[varname] = varvalue

# def getVal(token):
# 	if token[0:6]=="STRING":
# 		token = token[7:]
# 		#token = token[-1]
# 	elif token[0:3] == "NUM":
# 		token = token[4:]
# 	elif token[0:3] == "EXP":
# 		#print("EXP is here ")
# 		token = evaluate(evalExp(token[4:]))
# 		#token = token[-1]
# 	elif token[0:3] == "VAR":  # VAR:$
# 		token = token[5:]   # this is the variable name that i wanna get its value from its table 
# 		if token in symbol_table:	
# 			token = symbol_table[token]
# 			#print("checking on my token ",token)
# 			print(getVal(token))       # i am awesome <3 <3 
# 		else:
# 			print("undefined variable")

# 	#print(token)
# 	return token


# def evalExp(exp):
# 	#print("i am here ")
# 	num_stack =[]
# 	exp = exp + ","   # we added this at the end cause i want sth that i know to check on to know that i have reached the end of my expression. 
# 	#print("this is the string entering the evalexp",exp)
# 	#print("this is the length of the string entering the evalexp",len(exp))
# 	#i = len(exp) -1
# 	i = 0
# 	num = ""
# 	while i < len(exp): #i >= 0:
# 		#print(exp[i])

# 		if(exp[i] in "+-/*%()"):
# 			#print(exp[i])
# 			#num = num[::-1]
# 			num_stack.append(num)
# 			#print("num appended :",num,"and op :",exp[i])
# 			num_stack.append(exp[i])
# 			num=""
# 		# elif(exp[i] in "()"):
# 		# 	num_stack.append(num)
# 		# 	print("parenthes : ",exp[i])
# 		# 	num_stack.append(exp[i])
# 		elif (exp[i] ==","):
# 			#print("num not in reverse order ",num)
# 			#num = num[::-1]   			#to print whole List in reverse order, use [::-1].
# 			#print("num in reverse order ",num)
# 			num_stack.append(num)
# 			num = "" 
# 		else:
# 			num += exp[i] 
# 		#i-=1
# 		i+=1
# 	#print(num_stack)
# 	return num_stack
 
# def evaluate(num_stack):
# 	# prec = []
# 	# prec = num_stack
# 	#while '*' in prec or '/' in prec or '%' in prec:
# 	# 34an eval exp bterga3ly "" elements ba3d el parentheses.
# 	print(num_stack)
# 	 #((5+9)*8)
# 	while '' in num_stack:
# 		for i,val in enumerate(num_stack):
# 			if val == "":
# 				del num_stack[i]
	
# 	#print(num_stack)

# 	contains_parenthes = 0
# 	parenthes_EXP = []
	
# 	for i,val in enumerate(num_stack):
# 	 	if val is "(":
# 	 		num_stack[i] = " "
# 	 		num_of_parentheses = 1
# 	 		#contains_parenthes = 1
# 	 		#start_index_new_exp = 0
# 	 		result_index = i+1
# 	 		#n = i+1
# 	 		exp_list = []
# 	 		exp_list = num_stack[i+1:]
# 	 		#print("exp_list : ",exp_list)
# 	 		for n,ch in enumerate(exp_list):
# 	 			if ch is "(":
# 	 				num_of_parentheses += 1
# 	 			elif ch is ")":
# 	 				if num_of_parentheses == 1:
# 	 					num_stack[n+i+1] = " "
# 	 					#print("recursion is here :")
# 	 					num_stack[result_index] = evaluate(parenthes_EXP)
# 	 					#print("the result of parenthes evaluation :",num_stack[result_index])
# 	 					break
# 	 				else:
# 	 					num_of_parentheses -= 1
# 	 			#result_index = i+1  
# 	 			parenthes_EXP.append(exp_list[n])
# 	 			num_stack[n+i+1] = " "
# 	 			#exp_list[n] = " "
# 	 			#print("appended element :",parenthes_EXP)
# 	 		#num_stack[result_index] = evaluate(parenthes_EXP)
	
# 	#print("after parentheses are removed :",num_stack)
	
# 	while ' ' in num_stack:
# 		for i,val in enumerate(num_stack):
# 			if val == " ":
# 				del num_stack[i]

# 	prec = []
# 	prec = num_stack
# 	#print(prec)
	
# 	for i,val in enumerate(num_stack):
# 		if val in "*/%":          # this val is a string not an index can't do val-1
# 			prec[i+1] = dada(float(num_stack[i-1]),val,float(num_stack[i+1]))
# 			#prec.pop(val:val+2)
# 			prec[i] = " "
# 			prec[i-1] = " "
# 			#prec[] = prec[:] - prec[val:val+2]

# 	#print(prec)
# 	while ' ' in prec:
# 		for i,val in enumerate(prec):
# 			if val == " ":
# 				del prec[i]
		
# 	#print(prec)
# 	# now i have a list with + or - only
# 	# while ("+" in prec) or ("-" in prec):
# 	# restart = True
# 	# while restart:
# 	for i,v in enumerate(prec):
# 	#	print("the index = ",i,"\n the value = ",v)	
# 		if v in "-+":
# 			#print("before:",prec[i])
# 			#print("the index : ",i)
# 			prec[i+1] = dada(float(prec[i-1]),v,float(prec[i+1]))
# 			#print("after:",prec[i])
# 	#		print(prec)
# 	# R = prec[-1]
# 	# del prec 
# 	# del num_stack

# 	print("result:",prec[-1])
# 	return prec[-1]


# def dada(num1,op,num2):
# 	if op == "*":
# 		return str(num1*num2)
# 	elif op == "/":
# 		return str(num1/num2)
# 	elif op == "%":
# 		#print("the mod op :",num1,"%",num2,"the result:",num1%num2)
# 		return str(num1%num2)
# 	elif op == "+":
# 		return str(num1+num2)
# 	elif op == "-":
# 		return str(num1-num2)

# def run():
# 	#rf = RF()
# 	parse(lex(FR.open_file(argv[1])))
# 	#evaluate()

# run()