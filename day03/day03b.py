import re

pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)"
total = 0

with open("day03/data.txt","r") as f:
    do = True
    for line in f:
        for match in re.finditer(pattern, line):
            if match.group(0) == "do()":
                do = True
            elif match.group(0) == "don't()":
                do = False
            elif do:
                total += int(match.group(1)) * int(match.group(2))

print(total)