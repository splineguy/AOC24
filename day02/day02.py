import numpy as np

count = 0
count_ar = 0

def is_safe(x):
    return (all((x[i] < x[i+1] and x[i+1]-x[i]<4) for i in range(len(x)-1)) or 
            all((x[i] > x[i+1] and x[i]-x[i+1]<4) for i in range(len(x)-1)))

with open("day02/data.txt","r") as f:
    for line in f:
        x = [int(i) for i in line.split()]
        
        
        if is_safe(x):
            count +=1
            count_ar +=1
            continue
        is_safe_after_removal = any(is_safe(x[:i]+x[i+1:]) for i in range(len(x)))
        if is_safe_after_removal:
            count_ar+=1
            continue
        
        

print(count)
print(count_ar)


                
                
