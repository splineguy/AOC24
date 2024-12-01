import numpy as np

with open('data1.txt', 'r') as f:
    lines = f.readlines()

loc1 = []
loc2 = []
for line in lines:
    num1, num2 = map(int, line.split())
    loc1.append(num1)
    loc2.append(num2)

loc1 = np.array(loc1)
loc2 = np.array(loc2)

loc1_sorted = np.sort(loc1)
loc2_sorted = np.sort(loc2)

result = np.sum(np.abs(loc2_sorted - loc1_sorted))
print(result)


