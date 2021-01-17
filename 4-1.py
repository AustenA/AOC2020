import re

f = open("Day4Pass.txt", "r")
passport = f.read().split("\n\n")
total = 0

required = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
required.sort()
for i in passport:
    found = re.findall("[a-z]{3}(?=:)",i)
    found.sort()
    if "cid" in found:
        found.remove("cid")
    
    if found == required:
        total = total + 1;
print(total)
