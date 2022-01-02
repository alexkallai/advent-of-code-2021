import sys

numarray = []

forward = 0
depth = 0
aim = 0

for i in sys.stdin:
	numarray.append(i)


for index, member in enumerate(numarray):
	parsed = member.split(" ")
	if parsed[0] == "forward":
		forward += int(parsed[1])
		depth += int(parsed[1]) * aim
	if parsed[0] == "up":
		aim -= int(parsed[1])
	if parsed[0] == "down":
		aim += int(parsed[1])

print("Forward x depth = ", forward*depth)