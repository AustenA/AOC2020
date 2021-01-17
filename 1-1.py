f = open("Day1Nums.txt", "r")
d = f.read().split("\n")

done = 0
for x in d:
    for y in d:
        if (int(x) + int(y) == 2020):
            print("Answer: " + str(int(x)*int(y)))
            done = 1
            break
    if done:
        break
