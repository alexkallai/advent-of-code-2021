import sys

numarray = []

for i in sys.stdin:
	numarray.append(int(i))

kisebb = 0
nagyobb = 0

for index, member in enumerate(numarray):
	if index !=0:
		if numarray[index] > numarray[index-1]:
			nagyobb += 1

print("Azon esetek száma, amikor az adott mérés nagyobb, mint az előző:", nagyobb)