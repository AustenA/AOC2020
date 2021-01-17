f = open("Day3Trees.txt", "r")
d = f.read().split("\n")
supertotal = 0
height = len(d)
width = len(d[0])

total = 0
down = 0
over = 0
downSpeed = 1
rightSpeed = 1

while True:
    over = rightSpeed + over
    down = downSpeed + down
    if down >= height:
        break
    over = over%width
    print(d[down][over])
    if (d[down][over] == '#'):
        total = total + 1
supertotal = total

total = 0
down = 0
over = 0
downSpeed = 1
rightSpeed = 3

while True:
    over = rightSpeed + over
    down = downSpeed + down
    if down >= height:
        break
    over = over%width
    print(d[down][over])
    if (d[down][over] == '#'):
        total = total + 1
supertotal = total * supertotal


total = 0
down = 0
over = 0
downSpeed = 1
rightSpeed = 5

while True:
    over = rightSpeed + over
    down = downSpeed + down
    if down >= height:
        break
    over = over%width
    print(d[down][over])
    if (d[down][over] == '#'):
        total = total + 1
supertotal = total * supertotal


total = 0
down = 0
over = 0
downSpeed = 1
rightSpeed = 7

while True:
    over = rightSpeed + over
    down = downSpeed + down
    if down >= height:
        break
    over = over%width
    print(d[down][over])
    if (d[down][over] == '#'):
        total = total + 1
supertotal = total * supertotal

total = 0
down = 0
over = 0
downSpeed = 2
rightSpeed = 1

while True:
    over = rightSpeed + over
    down = downSpeed + down
    if down >= height:
        break
    over = over%width
    print(d[down][over])
    if (d[down][over] == '#'):
        total = total + 1
supertotal = total * supertotal

print(supertotal)

