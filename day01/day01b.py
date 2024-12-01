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

loc1 = np.sort(loc1)
loc2 = np.sort(loc2)

unique_elements, counts = np.unique(loc2, return_counts=True)
count_dict = dict(zip(unique_elements, counts))

# Use dict.get to handle elements not present in count_dict
sum_total = sum(element * count_dict.get(element, 0) for element in loc1)

print(sum_total)