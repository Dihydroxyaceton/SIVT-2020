import math

inputnumber = float(input("enter your number: "))

tolerance = 0.0001
maxnumber = 1000

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
			ok_results.append(str(numerator)+"/"+str(nominator))

for i in range(maxnumber):
	for i in range(maxnumber):
		outcome = numerator / nominator
		check_tolerance()
		numerator += 1
	numerator = 1
	nominator += 1

print(ok_results)
