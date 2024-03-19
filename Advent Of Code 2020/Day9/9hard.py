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

def chercher_liste_continue(data,x) : 
	for i in range(0,len(data)) : 
		somme = data[i]
		j = 1
		while somme < x : 
			somme += data[i+j]
			j += 1
		if somme == x : 
			liste = data[i:i+j]
			liste.sort()
			return [liste[0], liste[-1]]
			print(somme,sum(data[i:i+j]),x)
			print(data[i:i+j], data[i], data[i+j-1])
			return [data[i], data[i+j-1]]
	return [0,0] 


for i in range(0,len(data)-25) :
	if not verifier(data[i+25],data[i:i+25]) : 
		print(data[i+25])
		probleme = data[i+25]
		#print(data[i:i+26])
		break 

print(len(data))
print(sum(chercher_liste_continue(data,probleme)))
