f = open("Day2Pass.txt", "r")
d = f.read().split("\n")
total = 0
for x in d:
    a = x.split()
    numbers = a[0].split("-")
    totalOcc = a[2].count(a[1].strip(":"))
    if totalOcc >= int(numbers[0]) and totalOcc <= int(numbers[1]):
        total = total + 1


print(total)
