f = open("Day12Dir.txt", "r")
d = f.read().split("\n")

north = 0
east = 0

wn = 1
we = 10

dg = 90
for i in d:
    dg = dg % 360
    dr = i[:1]
    ds = int(i[1:])

    if dr == "N":
        wn = wn + ds
    elif dr == "E":
        we = we + ds
    elif dr == "S":
        wn = wn - ds
    elif dr == "W":
        we = we - ds

    elif ds == 180:
        #(we, wn) -> (-we, -wn)
        we = -we
        wn = -wn

    elif (dr == "L" and ds == 90) or (dr == "R" and ds == 270):
        #(we, wn) -> (wn, -we)
        temp = we
        we = -wn
        wn = temp
        
    elif (dr == "R" and ds == 90) or (dr == "L" and ds == 270):
        #(we, wn) -> (-wn, we)
        temp = we
        we = wn
        wn = -temp
    elif dr == "F":
        north = north + (ds * wn)
        east = east + (ds * we)
    else:
        print("Wat")

    print(i)
    print(north)
    print(east)
    print(wn)
    print(we)
    print()
    print()
print(abs(north) + abs(east))

#(dr == "F" and dg == 0)
#(dr == "F" and dg == 90)
#(dr == "F" and dg == 180)
#(dr == "F" and dg == 270)