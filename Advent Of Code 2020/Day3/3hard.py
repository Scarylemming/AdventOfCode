import re 

f = open("3.txt", "r")

data = [line for line in f.read().split("\n")]
data = data[0:len(data) -1]

def arbres_pente(x,y,data) : 
	place = 0 
	arbres = 0
	for i in range(0,len(data),y) :
		if place >= len(data[i]) : 
			place -= len(data[i])
		if data[i][place] == "#" :
			arbres += 1 
		place += x 
	return arbres  

produit = 1 
for pentes in [[1,1], [3,1], [5,1], [7,1], [1,2]] : 
	produit *= arbres_pente(pentes[0],pentes[1],data)
print(produit)