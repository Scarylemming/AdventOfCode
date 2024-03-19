import re 

f = open("16.txt", "r")

data = [line for line in f.read().split("\n")]
data1 = []
for i in data : 
	if i != "" : 
		data1 += [i]

data = data1
restrictions = []
nearby_tickets = []
liste_noms = []
for i in range(0,len(data)) : 
	if data[i] == "your ticket:" : 
		place_ticket = i
	if data[i] == "nearby tickets:" : 
		place_nearby_tickets = i

for i in range(0,place_ticket) : 
	ajouter = 0
	if ("arrival" in data[i]) | ("departure" in data[i]) :
		ajouter = 1
	ligne = data[i].split(" ")[1+ajouter] + " "
	ligne += data[i].split(" ")[3+ajouter]
	if ajouter == 0 : 
		nom = data[i].split(" ")[0]
	else : 
		nom = data[i].split(" ")[0] + " "
		nom += data[i].split(" ")[1]
	liste_noms += [nom[0:-1]]
	restrictions += [ligne]
	i += 1 

for i in range(place_nearby_tickets+1,len(data)) : 
	nearby_tickets += [data[i].split(",")]

for i in range(0,len(restrictions)) :
	restrictions[i] = restrictions[i].split(" ") 

possibles = []
for i in restrictions : 
	for j in i : 
		j = j.split("-")
		for k in range(int(j[0]), int(j[1])+1) : 
			if k not in possibles : 
				possibles += [k]
possibles.sort()

tickets_valables = []
for i in nearby_tickets : 
	test = 0 
	for j in i : 
		if int(j) not in possibles : 
			test = 1
			break 
	if test == 0 : 
		tickets_valables += [i]

print(restrictions)
print(len(restrictions))

classes_possibles = []
for i in range(0,len(restrictions)) : 
	classes_possibles += [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]]

for i in tickets_valables : 
	for j in range(0,len(i)) : 
		for k in range(0,len(restrictions)) : 
			r = [restrictions[k][0].split("-"), restrictions[k][1].split("-")]
			if not ((int(r[0][0]) <= int(i[j]) <= int(r[0][1])) | (int(r[1][0]) <= int(i[j]) <= int(r[1][1]))) : 
				classes_possibles[j][k] = "#"
				#print(r,i[j],i,j,k)
				#print(classes_possibles)

for i in range(0,len(classes_possibles)) : 
	ligne = []
	for j in classes_possibles[i] : 
		if j != "#" : 
			ligne += [j]
	classes_possibles[i] = ligne

fini = []
while fini != [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19] : 
	fini.sort()
	#print(fini)
	for i in range(0,len(classes_possibles)) : 
		if len(classes_possibles[i]) == 1 :
			if classes_possibles[i][0] not in fini : 
				fini += classes_possibles[i]
		else : 
			for j in range(0,len(classes_possibles[i])) : 
				if classes_possibles[i][j] in fini : 
					#print(classes_possibles[i], "premier")
					classes_possibles[i] = classes_possibles[i][0:j] + classes_possibles[i][j+1:]
					#print(classes_possibles[i])
					#fini = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
					break 

print(classes_possibles)

produit = 1

ticket = data[place_ticket+1].split(",")

for i in range(0,len(classes_possibles)) : 
	if "departure" in liste_noms[classes_possibles[i][0]] : 
		produit *= int(ticket[i])

print(produit)
 