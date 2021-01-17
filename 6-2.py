from string import ascii_lowercase
f = open("Day6Yes.txt", "r")
d = f.read().split("\n\n")
total = 0

for x in d:
    people = x.count('\n') + 1
    for i in ascii_lowercase:
        if people == x.count(i):
            total = total + 1
print(total)
