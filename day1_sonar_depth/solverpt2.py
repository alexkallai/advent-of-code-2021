import sys

numarray = []

for i in sys.stdin:
	numarray.append(int(i))

kisebb = 0
nagyobb = 0

for index, member in enumerate(numarray):
	if index < len(numarray)-3:
		if (numarray[index] + numarray[index + 1] + numarray[index + 2] ) < (numarray[index + 1] + numarray[index + 2] + numarray[index + 3] ):
			nagyobb += 1

print("Azon esetek száma, amikor a 3-as csúszóablakos mérés nagyobb, mint az előző:", nagyobb)