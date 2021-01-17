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

number = int(d[place])
place = 0
done = 0
while True:
    if place >= len(d):
        break
    place2 = int(place)
    lowest = int(d[place2])
    counting = 0
    highest = 0
    lowest = 1000000000
    while True:
        if place2 >= len(d):
            break
        counting = counting + int(d[place2])
        if int(d[place2]) < lowest:
            lowest = int(d[place2])
        if int(int(d[place2]) > highest):
            highest = int(d[place2])
        if counting > number:
            break
        if counting == number:
            done = 1
            break
        place2 = place2 + 1
    place = place + 1
    if done:
        break
print()
print(lowest + highest)
