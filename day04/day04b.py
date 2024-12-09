with open('day04/data2.txt') as f:

    count = 0

    lines = f.readlines()
    lines = [line.strip() for line in lines]

    for i,line in enumerate(lines):
        for j,c in enumerate(line):
            incr = [(i-1,j-1),(i-1,j+1), (i+1,j+1), (i+1,j-1)]
            if c=='A':
                ## forward
                if (1 <= j <= len(line) - 2 and
                    1 <= i <= len(lines) - 2):
                    for k in range(4):
                        p = [incr[(k+i)%4] for i in range(4)]
                        if ''.join([lines[p[i][0]][p[i][1]] for i in range(4)]) == 'MMSS':
                            count += 1



    print(count)