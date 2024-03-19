import re 

f = open("13.txt", "r")

data = [line for line in f.read().split("\n")]
data = data[0:-1]

departure = int(data[0])

liste = []
for i in data[1].split(",") : 
	if i != "x" : 
		liste += [int(i)]

print(liste)
minimum = 1000
for i in liste : 
	if (i - departure%i) < minimum : 
		minimum = (i - departure%i)
		print(minimum * i)