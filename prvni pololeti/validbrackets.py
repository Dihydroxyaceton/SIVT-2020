"""
bracket chain validity verifying
"""

def checkBrackets(text):
	openbrackets=0
	closebrackets=0
	if (text[0])==")":
		return print("not valid!") # bracket chain can't begin with a closing bracket
	if (text[-1])=="(":
		return print("not valid!") # bracket chain can't end with an opening bracket 
	for character in text:
		if character == "(":
			openbrackets+=1
			#print("ob+1") # developer option
		if character == ")":
			closebrackets+=1
			#print("cb+1") # developer option	
	if openbrackets==closebrackets: # opening bracket count has to match closing bracket count
		return print("OK")
	else:
		return print("not valid!")
	
checkBrackets(input())

