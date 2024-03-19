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

def verifier_fields(passeport) : 
	compte = 0
	for i in passeport : 
		i = i.split(":")
		#print(i)
		for j in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] : 
			if i[0] == j : 
				#print("C'est égal")
				compte += 1 
				break 
	if compte == 7 : 
		return True 


def check(passeport) : 
	if not verifier_fields(passeport) : 
		return False 

	for i in passeport : 
		i = i.split(":")
		if not check_norm(i[0], i[1]) : 
			return False 
	return True


def check_norm(field, code) : 
	if field == "byr" : 
		if 1920 <= int(code) <= 2002 : 
			return True 
		else : 
			return False
	elif field == "iyr" : 
		if 2010 <= int(code) <= 2020 : 
			return True 
		else : 
			return False
	elif field == "eyr" : 
		if 2020 <= int(code) <= 2030 :
			return True 
		else : 
			return False
	elif field == "hgt" : 
		if code[len(code)-2:len(code)] == "cm" : 
			if 150 <= int(code[0:len(code)-2]) <=193 : 
				return True
			else : 
				return False
		elif code[len(code)-2:len(code)] == "in" : 
			if 59 <= int(code[0:len(code)-2]) <= 76 : 
				return True 
			else : 
				return False
		else : 
			print("Problème, on a pas réussi à différencier les cm des in")
			print(code)
			return False 
	elif field == "hcl" : 
		if code[0] == "#" : 
			for i in code[1:] : 
				if i not in "abcdef1234567890" : 
					return False
				return True
		else : 
			return False
	elif field == "ecl" : 
		if code in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] : 
			return True 
		else : 
			return False 
	elif field == "pid" : 
		if len(code) == 9 : 
			for i in code : 
				if i not in "1234567890" : 
					return False 
			return True 
		else : 
			return False 
	elif field == "cid" : 
		return True 
	else : 
		print("On a un code que l'on ne reconnait pas")
		return False
			

resultat = 0 

for i in data : 
	if check(i) : 
		resultat += 1

print(resultat)

