f = open("2.txt", "r")


data = [line for line in f.read().split("\n")][:-1]

place = [0,0]

for i in data : 
    if "forward" in i : 
        place[0] += int(i[-1])
    elif "up" in i : 
        place[1] -= int(i[-1])
    elif "down" in i : 
        place[1] += int(i[-1])

print(place)

print(place[0] * place[1])
