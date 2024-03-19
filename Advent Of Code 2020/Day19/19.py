import re 

f = open("19.txt", "r")

data = [line for line in f.read().split("\n")]
data = data[0:-1]

instructions = []
mots = []

for i in data : 
	if i != "" : 
		if i[0] in "1234567890" : 
			instructions += [i]
		else : 
			mots += [i]

for i in instructions : 
	if "a" in i : 
		print(i, "lettre a") 
	if "b" in i : 
		print(i, "lettre b")

dict_instructions = {}

for i in instructions : 
	dict_instructions[int(i.split(":")[0])] = i.split(":")[1]

for i in dict_instructions : 
	print(dict_instructions[i])