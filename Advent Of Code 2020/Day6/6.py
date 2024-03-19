import re 

f = open("6.txt", "r") 

data = [line for line in f.read().split("\n")]
if data[-1] == "" : 
	data = data[0:len(data)-1]

groups = []
groupe = ""
for i in data : 
	if i == "" : 
		groups += [groupe]
		groupe = ""
	else : 
		groupe += i 
groups += [groupe]
def count_letters(n) :
	res = 0 
	for i in "abcdefghijklmnopqrstuvwxyz" : 
		if i in n : 
			res += 1 
	return res 
testgroupe = ["abc", "abc", "abac", "aaaa", "b"]
test_somme = 0
for i in testgroupe : 
	test_somme += count_letters(i) 

#print(test_somme)

somme = 0 
for i in groups : 
	somme += count_letters(i) 
	#print(count_letters(i),i)
print(somme)

#print(count_letters("abc"))
