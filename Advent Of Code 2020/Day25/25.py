key1 = 15628416
key2 = 11161639

n = 20201227

test1 = 5764801
test2 = 17807724

nombre = 1 
compte = 0

while nombre != key1 : 
	nombre *= 7 
	nombre %= n 
	compte += 1

print(compte)


nombre2 = 1 
compte2 = 0

while nombre2 != key2 : 
	nombre2 *= 7 
	nombre2 %= n 
	compte2 += 1

print(compte2)

a = 1

for i in range(0,compte) : 
	a *= key2
	a %= n 

print(a)
