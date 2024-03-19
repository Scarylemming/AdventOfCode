import re 

f = open("6.txt", "r") 

data = [line for line in f.read().split("\n")]
if data[-1] == "" : 
	data = data[0:len(data)-1]

groups = []
groupe = []
for i in data : 
	if i == "" : 
		groups += [groupe]
		groupe = []
	else : 
		groupe += [i]
groups += [groupe]
def count_letters(groupe) :
	#print(groupe)
	res = 0 
	for i in "abcdefghijklmnopqrstuvwxyz" : 
		for j in groupe : 
			test = 0 
			if i not in j :
				test = 1 
				break
		if test == 0 :
			res += 1 

	return res 
testgroupe = [["abc"], ["a", "b", "c"], ["ab", "ac"], ["a", "a", "a", "a"], ["b"]]
test_somme = 0
for i in testgroupe : 
	test_somme += count_letters(i) 
	print(count_letters(i))

print(test_somme)

somme = 0 
for i in groups : 
	somme += count_letters(i) 
	#print(count_letters(i),i)
print(somme)

#print(count_letters("abc"))
