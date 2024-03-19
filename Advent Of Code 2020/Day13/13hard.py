import re 

f = open("13.txt", "r")

data = [line for line in f.read().split("\n")]
data = data[0:-1]



liste = []
for i in data[1].split(",") : 
	if i != "x" : 
		liste += [int(i)]
	else : 
		liste += [i]

nombre_residus = []

for i in range(0,len(liste)) : 
	if liste[i] != "x" : 
		nombre_residus += [[liste[i], i]]
produit = 1 
for i in nombre_residus : 
	produit *= i[0]



def is_prime(n) : 
	for i in range(2,int(n**0.5)-1) : 
		if n%i == 0 : 
			return False 
	return True 

resultat = 0
for i in nombre_residus : 
	n_i = int(produit/i[0]) 
	for j in range(1,i[0]) : 
		if (n_i*j)%i[0] == 1 : 
			resultat += n_i*j*i[1]
print("Le résultat est", -(resultat%produit-produit))

