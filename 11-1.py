f = open("Day11Seat.txt", "r")
d = f.read().split("\n")

length = len(d[0])
tempL = list(d)
total = 0
while True:
    for x in range(len(d)):
        for y in range(length):
            if d[x][y] == ".":
                temp = list(tempL[x])
                temp[y] = d[x][y]
                tempL[x] = ''.join(temp)
                continue
            taken = 0
            if x:
                if d[x-1][y] == "#":
                    taken = taken + 1
                if y + 1 < length:
                    if d[x - 1][y + 1] == "#":
                        taken = taken + 1
            if y:
                if d[x][y-1] == "#":
                    taken = taken + 1
                if x + 1 < len(d):
                    if d[x+1][y - 1] == "#":
                        taken = taken + 1
            if x * y:
                if d[x-1][y-1] == "#":
                    taken = taken + 1
            if x + 1 < len(d):
                if d[x+1][y] == "#":
                    taken = taken + 1
                if y + 1 < length:
                    if d[x + 1][y+1] == "#":
                        taken = taken + 1
            if y + 1 < length:
                if d[x][y+1] == "#":
                    taken = taken + 1
    
            if taken == 0:
                temp = list(tempL[x])
                temp[y] = "#"
                tempL[x] = ''.join(temp)
            elif taken >= 4:
                temp = list(tempL[x])
                temp[y] = "L"
                tempL[x] = ''.join(temp)
            else:
                temp = list(tempL[x])
                temp[y] = d[x][y]
                tempL[x] = ''.join(temp)

    if d == tempL:
        break
    d = list(tempL)

print('\n'.join(tempL))
print()

d = list(tempL)
for x in range(len(d)):
        for y in range(length):
            if d[x][y] == "#":
                total = total + 1
print(f"Total: {total}")