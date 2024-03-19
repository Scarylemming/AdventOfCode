import re 
from copy import copy 
from copy import deepcopy
f = open("Test.txt", "r")

data = [line for line in f.read().split("\n")]

def chercher_place(x,y,dx,dy,max_x, max_y,data) : 
	while (x not in [0,max_x]) & (y not in [0,max_y]) : 
		if data[x][y] == "#" : 
			return [x,y]
		x += dx 
		y += dy 
	return None

def cases_adjacentes(x,y,max_x, max_y,data) : 
	res = []
	directions = [[-1,-1], [0,-1], [1,-1], [1,0], [1,1], [0,1], [-1,1],[-1,0]]
	for dir in directions : 
		a = chercher_place(x,y,dir[0], dir[1], max_x, max_y,data)
		if not ((a == None) | (a == [x,y])) :
			res += [a]
	return res 

for i in range(0,len(data)) : 
	#print(data[i])
	ligne = []
	for j in data[i] : 
		ligne += [j]
	#print(ligne)
	data[i] = ligne

max_x = len(data)-1 
max_y = len(data[0])-1 
#print(cases_adjacentes(0,0,max_x, max_y))

def iteration(data) : 
	nouveau = deepcopy(data)
	for i in range(0,len(data)) : 
		for j in range(0,len(data[0])) : 
			possible = cases_adjacentes(i,j,max_x, max_y,data)
			occupes = 0 
			for k in possible : 
				#print(k, k[0])
				if data[k[0]][k[1]] == "#" : 
					occupes += 1
			if occupes == 0 : 
				#print(nouveau[i][j])
				if nouveau[i][j] == "L" : 
					nouveau[i][j] = "#"
			elif occupes > 4 : 
				if nouveau[i][j] == "#" : 
					nouveau[i][j] = "L"
	return nouveau
def egal(x,y) : 
	if len(x) == 1 : 
		if x == y : 
			return True 
		else : 
			return False
	for i in range(0,len(x)) : 
		if not egal(x[i], y[i]) : 
			print(x[i], y[i])
			print(x,y)

			return False 
	return True 
def comptage(data) : 
	res = 0 
	for i in data : 
		for j in i : 
			if j == "#" : 
				res += 1
	return res


a = data 
b = deepcopy(a) 
#print(b[0])
#print(a[0])
a = iteration(a)
#print(b[0])
#print(a[0])
while a != b : 
	b = deepcopy(a)
	#print(b[0], compte)
	#print(a[0], compte, "a")
	c = iteration(b)
	a = c
	#print(b[0], compte)
	#print(a[0], compte, "a")


print(comptage(a))

