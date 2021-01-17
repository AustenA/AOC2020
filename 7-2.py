f = open("Day7Bags.txt", "r")
d = f.read().split("\n")
total = 0
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
            if inside == "other bag":
                cant.append(bags[0])
                break
            print(inside)

            if bags[0] == "shiny gold bag" and not (inside in can):
                can.append(inside)
                total = total + int(z[:1])
                #print("Gold")
            if bags[0] in can:
                can.append(inside)
                total = total + int(z[:1])
                
    if temp == can:
        running = False    
    test = input()
print()
if "shiny gold bag" in can:
    can.remove("shiny gold bag")
print(can)
print(total)