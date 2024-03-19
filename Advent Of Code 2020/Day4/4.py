import re 

f = open("4.txt", "r")

lignes = [line for line in f.read().split("\n")]

data = []

un_passeport = []
for i in lignes : 
	if i == "" : 
		data += [un_passeport] 
		un_passeport = []
	else : 
		un_passeport += i.split(" ")

resultat = 0 
for i in data :
	print(i)
	compte = 0 
	for j in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] : 
		trouve = 0
		for k in i : 
			#print(k[0:3], j)
			if k[0:3] == j :
				trouve = 1 
				compte += 1
				break
	if compte == 7 : 
		resultat += 1 

print(resultat)

