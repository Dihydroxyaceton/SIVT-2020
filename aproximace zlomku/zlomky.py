import math

inputnumber = float(input("enter your number: "))

tolerance = 0.002


# čitatel = numerator
# jmenovatel = nominator

print("Please stand by...")

ok_results = []
numerator = 1
nominator = 1


def check_tolerance():
	#print (inputnumber-outcome)
	if (inputnumber-outcome) < tolerance:
		if (inputnumber-outcome) > -tolerance:
			#print ("ok")
			ok_results.append(str(numerator)+"/"+str(nominator))


for i in range(500):
	for i in range(500):
		outcome = numerator / nominator
		check_tolerance()
		#print(numerator)
		numerator += 1
	numerator = 1
	nominator += 1

#print(inputnumber)
print(ok_results)
