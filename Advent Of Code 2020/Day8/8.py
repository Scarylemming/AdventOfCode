import re 

f = open("8.txt", "r")

data = [line.split(" ") for line in f.read().split("\n")]
if data[-1] == [""] : 
	print("trouvé")
	data = data[0:len(data)-1]

place = 0 
accumulateur = 0 
liste_places_visitées = []
while place not in liste_places_visitées : 
	liste_places_visitées += [place]
	if data[place][0] == "acc" : 
		accumulateur += int(data[place][1])
		place += 1
	elif data[place][0] == "jmp" : 
		place += int(data[place][1]) 
	elif data[place][0] == "nop" : 
		place += 1 

print(accumulateur)

