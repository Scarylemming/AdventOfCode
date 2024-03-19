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
somme = 0 

for i in nearby_tickets : 
	for j in i : 
		if int(j) not in possibles : 
			somme += int(j)
print(somme)

