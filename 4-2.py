import re

f = open("Day4Pass.txt", "r")
passport = f.read().split("\n\n")
total = -1

required = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
required.sort()

eyecolor = ["amb","blu","brn","gry","grn","hzl","oth"]
for i in passport:
    i = i.replace("\n",' ')
    i = i.split(' ')
    #found = re.split(":",i)
    
    my_list = list()
    
    for x in i:
        my_list.append(x.split(":")[0])
    if "cid" in my_list:
        my_list.remove("cid")
    my_list.sort()
    if my_list != required:
        continue
    valid = 1
    #print(i)
    for x in i:
        y = x.split(":")
        #print(x)
        if y[0] == "byr":
            if not (len(y[1]) == 4):
                valid = 0
                break
            if not (int(y[1]) >= 1920 and int(y[1]) <= 2002):
                valid = 0
                print("Byr Fail")
                break
        if y[0] == "iyr":
            if not (len(y[1]) == 4):
                valid = 0;
                break
            if not (int(y[1]) >= 2010 and int(y[1]) <= 2020):
                valid = 0
                print("Iyr Fail")
                break
        if y[0] == "eyr":
            if not (len(y[1]) == 4):
                valid = 0;
                break
            if not (int(y[1]) >= 2020 and int(y[1]) <= 2030):
                valid = 0
                print("Eyr Fail")
                break
        if y[0] == "hcl":
            if not re.search("#([a-f0-9]){6}",y[1]):
                valid = 0
                print("Hcl Fail")
                break
        if y[0] == "ecl":
            if not (y[1] in eyecolor):
                print("Ecl Fail")
                valid = 0
                break
        if y[0] == "pid":
            if not re.search("[0-9]{9}",y[1]):
                valid = 0
                print("Pid Fail")
                break
        if y[0] == "hgt":
            try:
                typ = y[1][-2:]
                hgt = int(y[1][:-2])
            except:
                valid = 0
                print("Hgt Fail")
                break
            if typ == "cm":
                if not (hgt >= 150 and hgt <= 193):
                    valid = 0
                    print("Hgt Fail")
                    break
            elif typ == "in":
                if not (hgt >= 59 and hgt <= 76):
                    valid = 0
                    print("Hgt Fail")
                    break
            else:
                valid = 0
                break
    
    total = total + valid

print(total)

