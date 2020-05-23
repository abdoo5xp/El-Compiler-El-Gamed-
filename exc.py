def evalExp(exp):
	#print("i am here ")
	num_stack =[]
	exp = exp + ","   # we added this at the end cause i want sth that i know to check on to know that i have reached the end of my expression. 
	#print("this is the string entering the evalexp",exp)
	#print("this is the length of the string entering the evalexp",len(exp))
	#i = len(exp) -1
	i = 0
	num = ""
	while i < len(exp): #i >= 0:
		#print(exp[i])

		if(exp[i] in "+-/*%()"):
			#print(exp[i])
			#num = num[::-1]
			num_stack.append(num)
			#print("num appended :",num,"and op :",exp[i])
			num_stack.append(exp[i])
			num=""
		# elif(exp[i] in "()"):
		# 	num_stack.append(num)
		# 	print("parenthes : ",exp[i])
		# 	num_stack.append(exp[i])
		elif (exp[i] ==","):
			#print("num not in reverse order ",num)
			#num = num[::-1]   			#to print whole List in reverse order, use [::-1].
			#print("num in reverse order ",num)
			num_stack.append(num)
			num = "" 
		else:
			num += exp[i] 
		#i-=1
		i+=1
	#print(num_stack)
	return num_stack
 
def evaluate(num_stack):
	# prec = []
	# prec = num_stack
	#while '*' in prec or '/' in prec or '%' in prec:
	# 34an eval exp bterga3ly "" elements ba3d el parentheses.
	#print(num_stack)
	 #((5+9)*8)
	while '' in num_stack:
		for i,val in enumerate(num_stack):
			if val == "":
				del num_stack[i]
	
	#print(num_stack)

	contains_parenthes = 0
	parenthes_EXP = []
	
	for i,val in enumerate(num_stack):
	 	if val is "(":
	 		num_stack[i] = " "
	 		num_of_parentheses = 1
	 		#contains_parenthes = 1
	 		#start_index_new_exp = 0
	 		result_index = i+1
	 		#n = i+1
	 		exp_list = []
	 		exp_list = num_stack[i+1:]
	 		#print("exp_list : ",exp_list)
	 		for n,ch in enumerate(exp_list):
	 			if ch is "(":
	 				num_of_parentheses += 1
	 			elif ch is ")":
	 				if num_of_parentheses == 1:
	 					num_stack[n+i+1] = " "
	 					#print("recursion is here :")
	 					num_stack[result_index] = evaluate(parenthes_EXP)
	 					#print("the result of parenthes evaluation :",num_stack[result_index])
	 					break
	 				else:
	 					num_of_parentheses -= 1
	 			#result_index = i+1  
	 			parenthes_EXP.append(exp_list[n])
	 			num_stack[n+i+1] = " "
	 			#exp_list[n] = " "
	 			#print("appended element :",parenthes_EXP)
	 		#num_stack[result_index] = evaluate(parenthes_EXP)
	
	#print("after parentheses are removed :",num_stack)
	
	while ' ' in num_stack:
		for i,val in enumerate(num_stack):
			if val == " ":
				del num_stack[i]

	prec = []
	prec = num_stack
	#print(prec)
	
	for i,val in enumerate(num_stack):
		if val in "*/%":          # this val is a string not an index can't do val-1
			prec[i+1] = dada(float(num_stack[i-1]),val,float(num_stack[i+1]))
			#prec.pop(val:val+2)
			prec[i] = " "
			prec[i-1] = " "
			#prec[] = prec[:] - prec[val:val+2]

	#print(prec)
	while ' ' in prec:
		for i,val in enumerate(prec):
			if val == " ":
				del prec[i]
		
	#print(prec)
	# now i have a list with + or - only
	# while ("+" in prec) or ("-" in prec):
	# restart = True
	# while restart:
	for i,v in enumerate(prec):
	#	print("the index = ",i,"\n the value = ",v)	
		if v in "-+":
			#print("before:",prec[i])
			#print("the index : ",i)
			prec[i+1] = dada(float(prec[i-1]),v,float(prec[i+1]))
			#print("after:",prec[i])
	#		print(prec)
	# R = prec[-1]
	# del prec 
	# del num_stack

	#print("result:",prec[-1])
	return prec[-1]


def dada(num1,op,num2):
	if op == "*":
		return str(num1*num2)
	elif op == "/":
		return str(num1/num2)
	elif op == "%":
		#print("the mod op :",num1,"%",num2,"the result:",num1%num2)
		return str(num1%num2)
	elif op == "+":
		return str(num1+num2)
	elif op == "-":
		return str(num1-num2)

def evalCond(oper1,op,oper2):   # test this func by printing its output 
	oper1 = float(oper1)
	oper2 = float(oper2)
	if op == "<":
		return (oper1 < oper2)
	elif op == ">":
		return (oper1 > oper2)
	elif op == "==":
		return (oper1 == oper2)
	elif op == "<=":
		return (oper1 <= oper2)
	elif op == ">=":
		return (oper1 >= oper2)
	elif op == "|":                        # bitwise or 
		return (oper1 | oper2)
	elif op == "&":						   # bitwise and 
		return (oper1 & oper2)


