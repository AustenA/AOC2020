f = open("Day7Bags.txt", "r")
d = f.read().split("\n")

can = list()
cant = list()
temp = list()
running = True
while running:
    temp = list(can)
    for y in d:
        bags = y.replace(" contain ", "-").split('-')
        #print(bags)
        for z in bags[1].split(','):
            inside = z[2:].lstrip(" ").rstrip(".")
            if inside in cant:
                continue
            if inside == "other bags":
                cant.append(bags[0])
                break

            if "shiny gold bag" in inside and not (bags[0] in can):
                can.append(bags[0])
                #print("Gold")
            if inside in can and not (bags[0] in can):
                can.append(bags[0])
    if temp == can:
        running = False    

print()
if "shiny gold bag" in can:
    can.remove("shiny gold bag")
print(can)
print(len(can))