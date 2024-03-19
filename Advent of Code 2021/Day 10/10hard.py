import copy

f = open("10.txt", "r")


data = [line for line in f.read().split("\n")][:-1]

scores = []

new_data = []

def count(string) : 
    somme = 0
    n = len(string)
    for i in range(n) : 
        somme *= 5
        if string[n - i - 1] == "(" : 
            somme += 1
        elif string[n - i - 1] == "[" : 
            somme += 2
        elif string[n - i -1] == "{" : 
            somme += 3 
        else : 
            somme += 4
    return somme

for i in data : 
    corrupted = False
    new = ""
    for c in i : 
        #print(new)
        if c in [")", "]", "}", ">"] : 
            if (new[-1] == "(") and (c == ")") : 
                new = new[:-1]
            elif (new[-1] == "[") and (c == "]") : 
                new = new[:-1]
            elif (new[-1] == "{") and (c == "}") : 
                new = new[:-1]
            elif (new[-1] == "<") and (c == ">") : 
                new = new[:-1]
            else :
                corrupted = True
                break
        else : 
            new += c
    if corrupted == False : 
        #print(count(new))
        scores.append(count(new))

scores.sort()

print(scores[int((len(scores) - 1) / 2)])
