import re 

f = open("12.txt", "r")
data = [line for line in f.read().split("\n")]


data = data[0:len(data)-1]

def tourner(string,direction,place, waypoint) : 
	if string[0] == "L" : 
		if string[1:] == "90" : 
			waypoint = [-waypoint[1], waypoint[0]]
		elif string[1:] == "180" : 
			waypoint = [-waypoint[0], -waypoint[1]]
		elif string[1:] == "270" : 
			waypoint = [waypoint[1], -waypoint[0]] 
	else :
		if string[1:] == "270" : 
			waypoint = [-waypoint[1], waypoint[0]]
		elif string[1:] == "180" : 
			waypoint = [-waypoint[0], -waypoint[1]]
		elif string[1:] == "90" : 
			waypoint = [waypoint[1], -waypoint[0]] 
	return waypoint
def avancer(string, direction, place, waypoint) : 
	place[0] += waypoint[0] * int(string[1:])
	place[1] += waypoint[1] * int(string[1:])
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
waypoint = [10,1]
direction = 0 
for i in data : 
	#print(place, waypoint)
	if i[0] in ["R", "L"] : 
		waypoint = tourner(i,direction, place, waypoint)
	else : 
		if i[0] == "F" : 
			#print(place, waypoint, i)
			place = avancer(i,direction, place, waypoint)
		elif i[0] in ["E", "N", "W", "S"] : 
			waypoint = gogogo(i,waypoint)
print("La réponse est", abs(place[0]) + abs(place[1]))

