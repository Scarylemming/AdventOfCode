import re 

f = open("3.txt", "r")

data = [line for line in f.read().split("\n")]
data = data[0:len(data) -1]

x = 0
arbres = 0 

for i in data : 
	if x >= len(i) : 
		x -= len(i)
	if i[x] == "#" : 
		#print(i,x)
		arbres += 1 
		#print("#") 
	#else : 
		#print("O")
	x += 3

print(arbres)