import copy

f = open("10.txt", "r")


data = [line for line in f.read().split("\n")][:-1]

somme = 0

for i in data : 
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
                if c == ")" : 
                    somme += 3
                elif c == "]" : 
                    somme += 57
                elif c == "}" : 
                    somme += 1197
                elif c == ">" : 
                    somme += 25137
                break
        else : 
            new += c

print(somme)