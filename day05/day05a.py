# before = {}
after = {}

with open('day05/data2.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    line = lines.pop(0)
    while len(line) > 0:
        b,a = [int(x) for x in line.split("|")]
        
        # if b not in before:
        #     before[b] = [a]
        # else:
        #     before[b].append(a)

        if a not in after:
            after[a] = [b]
        else:
            after[a].append(b)
        
        line = lines.pop(0)
    
    #lines.pop(0)

    total = 0;
    for line in lines:
        pages = [int(x) for x in line.split(",")]
        valid = True
        for i in range(len(pages)-1):
            if pages[i] in after:
                if any([x in after[pages[i]] for x in pages[i+1:]]):
                    valid = False
                    break
        if valid:
            total += pages[len(pages)//2]
    
    print(total)

        
                    
