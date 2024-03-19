import re

f = open("10.txt", "r")

data = [line for line in f.read().split("\n")]
data = data[0:-1]
for i in range(0,len(data)) : 
	data[i] = int(data[i])
data += [0]
data.sort()

joint1 = 0 
joint2 = 0 
joint3 = 1 
for i in range(0,len(data)-1) : 
	if data[i+1] - data[i] == 1 : 
		joint1 += 1
	elif data[i+1] - data[i] == 2 : 
		joint2 += 1 
	elif data[i+1] - data[i] == 3 : 
		joint3 += 1 

print(data)
print(joint1,joint3)
print(joint1 * joint3)
