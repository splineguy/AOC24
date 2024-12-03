import re

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
total = 0

with open("day03/data.txt","r") as f:
    for line in f:
        matches = re.findall(pattern, line)
        for match in matches:
            total += int(match[0]) * int(match[1])

print(total)