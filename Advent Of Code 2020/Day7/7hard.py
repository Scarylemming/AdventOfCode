import re 

f = open("7.txt", "r") 

data = [line.split("contain") for line in f.read().split("\n")]
if data[-1] == [""] : 
	#print(data[-1])
	data = data[0:len(data)-1]

instructions = []
for i in data : 
	instructions += [[i[0], i[1].split(",")]]

def enlever_s_et_point(string) :
	#print(string, "string")
	while string[-3:] != "bag" : 
		#print(string[-3:])
		string = string[0:len(string)-1]
	return string
def enlever_nombres(string) : 
	if string == " no other bags." : 
		return [0,string]
	res = ""
	nombre = ""
	for i in range(0,len(string)) : 
		if i in [0,1,2] : 
			if string[i] in "1234567890" : 
				nombre += string[i]
			elif string[i] != " " : 
				res += string[i]
		else : 
			res += string[i]
	if nombre == "" : 
		return res
	else : 
		return [int(nombre), res]

instructions1 = []
for i in instructions : 
	#print(i, "ici est le i ")
	#print(i)
	ligne = enlever_s_et_point(enlever_nombres(i[0]))
	ligne1 = []
	for j in i[1] : 
		#print(j, "j")
		ligne2 = enlever_nombres(j)
		ligne2[1] = enlever_s_et_point(ligne2[1])
		ligne1 += [ligne2]
	instructions1 += [[ligne, ligne1]]
	ligne = []


def nombre_contenant(bag, instructions) :
	somme = 1
	for i in instructions : 
		if i[0] == bag : 
			#print(i)
			somme = 1
			for j in i[1] :
				if j[0] != 0 : 
					somme += j[0]*nombre_contenant(j[1], instructions)
	return somme

print(nombre_contenant("shiny gold bag", instructions1)-1)