f = open("Day1Nums.txt", "r")
d = f.read().split("\n")

done = 0
for x in d:
    for y in d:
        for z in d:
            if (int(x) + int(y) + int(z) == 2020):
                print("Answer: " + str(int(x)*int(y)*int(z)))
                done = 1
                break
        if done:
            break
    if done:
        break
