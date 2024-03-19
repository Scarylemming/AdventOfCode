import re 

f = open("24.txt", "r")

data = [line for line in f.read().split("\n")]

data = data[0:-1]

def deplacement(string, coord) : 
	if string == "e" : 
		return [coord[0]+1, coord[1]]
	if string == "w" : 
		return [coord[0]-1, coord[1]]
	if string == "ne" : 
		return [coord[0]+0.5, coord[1]+1]
	if string == "nw" : 
		return [coord[0]-0.5, coord[1]+1]
	if string == "se" : 
		return [coord[0]+0.5, coord[1]-1]
	if string == "sw" : 
		return [coord[0]-0.5, coord[1]-1]


toutes_places = []
for i in data : 
	place = 0
	start = [0,0]
	while place < len(i) : 
		if i[place] in "ns" : 
			start = deplacement(i[place:place+2], start)
			place += 2
		else : 
			start = deplacement(i[place], start)
			place += 1
	if start not in toutes_places : 
		toutes_places += [start]
	else : 
		for j in range(0,len(toutes_places)) : 
			if toutes_places[j] == start : 
				#print(toutes_places[j])
				#print("MEME")
				toutes_places = toutes_places[0:j] + toutes_places[j+1:]
				break

print(len(toutes_places))

print(toutes_places)

somme = 0

for i in toutes_places : 
	for j in toutes_places : 
		if i == j : 
			somme += 1 
print(somme)