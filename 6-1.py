f = open("Day6Yes.txt", "r")
d = f.read().split("\n\n")
total = 0

for x in d:
    x = x.replace('\n', '')
    x = list(dict.fromkeys(x))
    total = total + len(x)
    
print(total)
