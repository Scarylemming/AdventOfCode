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
	while string[-3:] != "bag" : 
		#print(string[-3:])
		string = string[0:len(string)-1]
	return string
def enlever_nombres(string) : 
	res = ""
	for i in range(0,len(string)) : 
		if i in [0,1,2] : 
			if string[i] not in "qwertzuiopasdfghjklyxcvbnm" : 
				a = 0
			else : 
				res += string[i]
		else : 
			res += string[i]
	return res 

instructions1 = []
for i in instructions : 
	#print(i, "ici est le i ")
	ligne = enlever_s_et_point(enlever_nombres(i[0]))
	ligne1 = []
	for j in i[1] : 
		#print(j, "j")
		ligne1 += [enlever_s_et_point(enlever_nombres(j))]
	instructions1 += [[ligne, ligne1]]
	ligne = []

liste_bags = []
for i in instructions1 : 
	if i[0] not in liste_bags : 
		liste_bags += [i[0]]

liste_contenant = ["shiny gold bag"]
ancienne_liste_contenant = []
while ancienne_liste_contenant != liste_contenant : 
	ancienne_liste_contenant = liste_contenant 
	for i in liste_contenant : 
		#print(i, "liste_contenant")
		for j in instructions1 :
			#print(j)
			if i in j[1] : 
				#print(i,j[1], j[0], "TROUVE")
				if j[0] not in liste_contenant : 
					liste_contenant += [j[0]]

print(len(liste_contenant)-1)

