line = 0
while True:
    f = open("Day8Acc.txt", "r")
    d = f.read().split("\n")
    acc = 0
    if line >= len(d):
        error = "OutOfLinesCodeSucks"
        break
    if d[line].split(" ")[0] == "nop":
        d[line] = d[line].replace("nop","jmp")
    elif d[line].split(" ")[0] == "jmp":
        d[line] = d[line].replace("jmp","nop")
    place = 0
    while True:
        if place >= len(d):
            error = "EOF"
            break
        if d[place] == "dne":
            error = "LOOP"
            break
        
        cmd = d[place].split(' ')
        d[place] = "dne"
        if cmd[0] == "acc":
            acc = acc + int(cmd[1])
        
        if cmd[0] == "jmp":
            place = place + int(cmd[1])
        else:
            place = place+1
    line = line + 1
    if error == "EOF":
        break
print(acc)
print(error)
