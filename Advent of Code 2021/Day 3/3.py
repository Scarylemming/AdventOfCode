f = open("3.txt", "r")


data = [line for line in f.read().split("\n")][:-1]

#data =["00100", "11110", "10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]

a = ""
b = ""


for j in range(len(data[0])) : 
    count = 0 
    ones = 0 
    for i in range(len(data)) : 
        if data[i][j] == "1" : 
            ones += 1
        count += 1
    if 2 * ones > count : 
        a += "1"
        b += "0"
    else : 
        a += "0"
        b += "1"
        
print(a,b)
        
print(int(a, 2), int(b,2))

print(int(a, 2) * int(b, 2))
        