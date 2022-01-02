import sys

# power consumption = gamma rate * epsilon rate

numarray = []

epsilon = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] #12 wide is the input column
epsilonbin = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] #12 wide is the input column
epsilonbinstr = ""
gammabinstr = ""

for i in sys.stdin:
	numarray.append(i)


for index, member in enumerate(numarray):
	for i, m in enumerate(member):
		if m == "1":
			epsilon[i] += 1

for index0, member0 in enumerate(epsilon):
	if member0 > len(numarray)/2:
		epsilonbin[index0] = 1
		epsilonbinstr += "1"
		gammabinstr += "0"
	else:
		epsilonbinstr += "0"
		gammabinstr += "1"

print("epsilon rate = ", epsilonbinstr)
print("gamma rate = ", gammabinstr)


epsilonrate = int(epsilonbinstr, 2)
gammarate = int(gammabinstr, 2)
print("power consumption is: ", epsilonrate*gammarate)