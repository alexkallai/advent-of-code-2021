import sys

#life support rating =  oxygen_gen_rating_str x co2_scrubber_rating_str

numarray = []

# read in the input in a list
for i in sys.stdin:
	numarray.append(i)
numarray_width = len(numarray[0])

oxygen_gen_rating = []
co2_scrubber_rating = []

print("Calculating oxygen_gen_rating...")
for position, member in enumerate(numarray):
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

print("Calculating co2_scrubber_rating...")



#oxygen_gen_rating_int = int( , 2)
#co2_scrubber_rating_int = int( , 2)
#print("power consumption is: " )