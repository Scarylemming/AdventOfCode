import re 

f = open("12.txt", "r")
data = [line for line in f.read().split("\n")]


data = data[0:len(data)-1]

def tourner(string,direction) : 
	if string[0] == "L" : 
		direction += int(string[1:])
	else : 
		direction -= int(string[1:])
	direction %= 360 
	return direction
def avancer(string, direction, place) : 
	if direction == 0 : 
		place[0] += int(string[1:])
	if direction == 90 : 
		place[1] += int(string[1:])
	if direction == 180 : 
		place[0] -= int(string[1:])
	if direction == 270 : 
		place[1] -= int(string[1:])
	return place
def gogogo(string, place) : 
	if string[0] == "E" :
		place[0] += int(string[1:])
	if string[0] == "N" : 
		place[1] += int(string[1:])
	if string[0] == "W" :
		place[0] -= int(string[1:])
	if string[0] == "S" :
		place[1] -= int(string[1:])
	return place

 
place = [0,0]
direction = 0 
for i in data : 
	if i[0] in ["R", "L"] : 
		direction = tourner(i,direction)
	else : 
		if i[0] == "F" : 
			place = avancer(i,direction, place)
		elif i[0] in ["E", "N", "W", "S"] : 
			place = gogogo(i,place)
print(place)
print(abs(place[0]) + abs(place[1]))

