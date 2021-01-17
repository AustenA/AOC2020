from string import ascii_lowercase
f = open("Day8Acc.txt", "r")
d = f.read().split("\n")
acc = 0
place = 0
while True:
    if place >= len(d):
        break
    if d[place] == "dne":
        break
    
    cmd = d[place].split(' ')
    d[place] = "dne"
    if cmd[0] == "acc":
        acc = acc + int(cmd[1])
        
    if cmd[0] == "jmp":
        place = place + int(cmd[1])
    else:
        place = place+1
print(acc)
