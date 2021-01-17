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

            xd = 1
            yd = 1
            while True:
                if x - (xd - 1):
                    if d[x-xd][y] == "#":
                        taken = taken + 1
                        break
                    elif d[x-xd][y] == "L":
                        break
                    else:
                        xd = xd + 1
                        continue
                else:
                    break
            xd = 1
            yd = 1
            while True:
                if x - (xd - 1):
                    if y + yd < length:
                        if d[x - xd][y + yd] == "#":
                            taken = taken + 1
                            break
                        elif d[x - xd][y + yd] == "L":
                            break
                        else:
                            xd = xd + 1
                            yd = yd + 1
                            continue
                    else:
                        break
                else:
                    break

            xd = 1
            yd = 1
            while True:
                if y - (yd - 1):
                    if d[x][y-yd] == "#":
                        taken = taken + 1
                        break
                    elif d[x][y-yd] == "L":
                        break
                    else:
                        yd = yd + 1
                        continue
                else: 
                    break
            xd = 1
            yd = 1
            while True:
                if y - (yd - 1):
                    if x + xd < len(d):
                        if d[x+xd][y - yd] == "#":
                            taken = taken + 1
                            break
                        if d[x+xd][y - yd] == "L":
                            break
                        else:
                            xd = xd + 1
                            yd = yd + 1
                            continue
                    else:
                        break
                else:
                    break
            xd = 1
            yd = 1
            while True:
                if (x - (xd - 1)) * (y - (yd - 1)):
                    if d[x-xd][y-yd] == "#":
                        taken = taken + 1
                        break
                    elif d[x-xd][y-yd] == "L":
                        break
                    else:
                        xd = xd + 1
                        yd = yd + 1
                else:
                    break
            xd = 1
            yd = 1
            while True:
                if x + xd < len(d):
                    if d[x+xd][y] == "#":
                        taken = taken + 1
                        break
                    elif d[x+xd][y] == "L":
                        break
                    else:
                        xd = xd + 1
                else:
                    break
            xd = 1
            yd = 1
            while True:
                if x + xd < len(d):
                    if y + yd < length:
                        if d[x + xd][y+yd] == "#":
                            taken = taken + 1
                            break
                        elif d[x + xd][y+yd] == "L":
                            break
                        else:
                            xd = xd + 1
                            yd = yd + 1
                    else:
                        break
                else: 
                    break
                            
            xd = 1
            yd = 1
            while True:
                if y + yd < length:
                    if d[x][y+yd] == "#":
                        taken = taken + 1
                        break
                    elif d[x][y+yd] == "L":
                        break
                    else:
                        yd = yd + 1
                else:
                    break

            if taken == 0:
                temp = list(tempL[x])
                temp[y] = "#"
                tempL[x] = ''.join(temp)
            elif taken >= 5:
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