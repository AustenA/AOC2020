f = open("Day9Pre.txt", "r")
d = f.read().split("\n")
place = 0
array = list()
pre = 25

for i in range(pre):
    array.append(d[place])
    place = place + 1
while True:
    if place >= len(d):
        break
    fail = 1

    for x in range(len(array)):
        for y in range(len(array)):
            if x == y:
                continue
            #print("Total: " + str(int(array[x]) + int(array[y])))
            if int(array[x]) + int(array[y]) == int(d[place]):
                fail = 0
    if fail:
        break
    array.append(d[place])
    array.pop(0)
    place = place + 1

print(d[place])
