import re 

f = open("6.txt", "r") 

data = [line for line in f.read().split("\n")]
if data[-1] == "" : 
	data = data[0:len(data)-1]


