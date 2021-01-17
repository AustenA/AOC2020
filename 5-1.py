import array as arr

f = open("Day5Board.txt", "r")
d = f.read().split("\n")
highest = 0
tmp = 0
def spl(s):
    return [c for c in s]

for seat in d:
    seat = spl(seat)
    start = [0,127]
    startRow = [0,7]
    place = start[1] - (start[0] - 1)
    placeRow = startRow[1] - (startRow[0] - 1)

    for i in seat:
        if i == 'F':
            place = place / 2
            start[1] = start[0] + place - 1
        if i == 'B':
            place = place / 2
            start[0] = start[1] - (place - 1)
        if i == 'L':
            placeRow = placeRow / 2
            startRow[1] = startRow[0] + placeRow - 1
        if i == 'R':
            placeRow = placeRow / 2
            startRow[0] = startRow[1] - (placeRow - 1)
    tmp = start[0] * 8 + startRow[0]
    if tmp > highest:
        highest = tmp

print(highest)

