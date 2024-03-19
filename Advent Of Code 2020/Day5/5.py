import re 

f = open("5.txt", "r") 

data = [line for line in f.read().split("\n")]

def debinariser(seat) : 
	res = ""
	for i in seat : 
		if i in ["F", "L"] : 
			res += "0"
		else : 
			res += "1"

	return res 

data = data[0:len(data)-1]
maximum = 0 
for i in data : 
	maximum = max(maximum, int(debinariser(i),2))

print(maximum)