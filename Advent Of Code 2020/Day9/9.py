import re 

f = open("9.txt", "r") 

ancien_data = [line for line in f.read().split("\n")]
if ancien_data[-1] == "" : 
	ancien_data = ancien_data[0:len(ancien_data)-1]

data = []
for i in ancien_data : 
	data += [int(i)]

def verifier(x,liste) : 
	for i in liste : 
		for j in liste : 
			if i != j : 
				if (i+j) == x : 
					return True
	return False 


for i in range(0,len(data)-25) :
	if not verifier(data[i+25],data[i:i+25]) : 
		print(data[i+25])
		print(data[i:i+26])
		break 

