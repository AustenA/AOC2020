f = open("Day2Pass.txt", "r")
d = f.read().split("\n")
total = 0
for x in d:
    a = x.split()
    char = a[1].strip(":")
    numbers = a[0].split("-")
    numbers[0] = int(numbers[0]) - 1
    numbers[1] = int(numbers[1]) - 1
    if (a[2][numbers[0]] != char) and (a[2][numbers[1]] != char):
        continue
    if (a[2][numbers[0]] != char) != (a[2][numbers[1]] != char):
        total = total + 1

print(total)
