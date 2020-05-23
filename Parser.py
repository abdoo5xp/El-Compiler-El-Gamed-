import exc as ex 

symbol_table = {}

def parse(toks):
	i = 0
	condition = []
	iscondition = 0
	stmts = []
	isstmt = 0
	cond_state = 0
	#print(toks)
	while(i < len(toks)):
		if toks[i] == ":":
			iscondition = 0
			cond_state = parseMC(condition)      
			print ("your condition ", condition)   #here implement the parse condition 
			print ("\n cond_state = ",cond_state)
			condition = ""
			i+=1
		elif toks[i] == "IF":
			iscondition = 1
			i+=1
		elif iscondition :
			condition.append(toks[i])
			i+=1
		elif toks[i] == "}":
			isstmt = 0
			if cond_state:
				parse(stmts)
			i+=1
		elif toks[i] == "{":
			isstmt = 1
			i+=1
		elif isstmt :
			stmts.append(toks[i])
			i+=1
		elif toks[i] == "PRINT":          
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
			toks.append(",")
			if toks[i+1][0:6] == "STRING" :
				if  toks[i+2][0:3] == "VAR": # i was gonna make another if inside for string and other types but python saves input as a string so screw it.                
					getInput(getVal(toks[i+1]),toks[i+2][5:])
					#print("checking on the poped item : ",toks.pop())
					#print(toks)
					toks.pop()
					i+=3
				else: 		#elif toks[i+2] == ",":  # bs dh ma3nah en deh a5er token fe el list 
					getInput(getVal(toks[i+1]),"")
					toks.pop()
					i+=2
		elif toks[i][0:3] == "NUM":    
			#print(toks[i][4:])
			getVal(toks[i])
			i+=1
		elif toks[i][0:3] == "EXP": 
			#print(toks[i][4:])
			getVal(toks[i])
			i+=1
		# elif toks[i] == "IF":  # input STRING:"sth" VAR:$var_name
		# 	if toks[i+1][0:3] is "VAR":
		# 		if toks[i+2][0:6] == "STRING":
		# 			getInput(getVal(toks[i+1]),toks[i+2][5:])	
		# 	i+=3 
	
	print(" \n my symbol table :",symbol_table)
	

def getInput(string_to_be_printed, varname):
	if varname == "":
		print(input(string_to_be_printed+" "))
	else : 
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


def parseCond(condlist):
	# for i,val in enumerate(condlist):
	# 	if val in "<>&|=":
	# 		if condlist[i+1] in "<>&|=":
	# 			condlist[i] += condlist[i+1]
	# 			del condlist[i+1]       

	return ex.evalCond(getVal(condlist[0]),condlist[1],getVal(condlist[2]))


def parseMC(condlist):
	
	res = []
	# mixing the operator tokens in <= ,&& and so on 
	for i,val in enumerate(condlist):
		if val in "<>&|=":
			if condlist[i+1] in "<>&|=":
				condlist[i] += condlist[i+1]
				del condlist[i+1]

	res.append(parseCond(condlist[0:3]))    # calculate the first condition ,cause you may have only one condition
	result = res[0]

	for i,val in enumerate(condlist):       # instead of getting operations first, once you find an operation get the result of its operands.
		if val in ["&&","||"]:
			res.append(val)
			res.append(parseCond(condlist[i+1:i+4]))

	for i,val in enumerate(res):            # now you have sth like this(true && true || false),so calculate its result
		if val == "&&":
			result = res[i-1] & res[i+1]
			res[i+1] = result
		elif val == "||": 
			result = res[i-1] | res[i+1]
			res[i+1] = result

	return result


# 1 > 2 && 5 < 10 || 3 < 20  
 # false && true || true 
 # 	false || true 
 # 		true 