with open('day04/data2.txt') as f:

    count = 0

    lines = f.readlines()
    lines = [line.strip() for line in lines]

    for i,line in enumerate(lines):
        for j,c in enumerate(line):
            if c=='X':
                ## forward
                if j <= len(line) - 4 and line[j:j+4] == 'XMAS':
                    count += 1

                ## backward
                if j >= 3 and line[j-3:j+1][::-1] == 'XMAS':
                    count += 1

                ## up
                if i <= len(lines) - 4 and ''.join([lines[i+k][j] for k in range(4)]) == 'XMAS':
                    count += 1
                
                ## down
                if i >= 3 and ''.join([lines[i-k][j] for k in range(4)]) == 'XMAS':
                    count += 1

                ## up-right
                if (i <= len(lines) - 4 and
                    j <= len(line) - 4 and
                    ''.join([lines[i+k][j+k] for k in range(4)]) == 'XMAS'):
                    count += 1

                ## up-left
                if (i <= len(lines) - 4 and
                    j >= 3 and
                    ''.join([lines[i+k][j-k] for k in range(4)]) == 'XMAS'):
                    count += 1

                ## down-right
                if (i >= 3 and
                    j <= len(line) - 4 and
                    ''.join([lines[i-k][j+k] for k in range(4)]) == 'XMAS'):
                    count += 1

                ## down-left
                if (i >= 3 and
                    j >= 3 and
                    ''.join([lines[i-k][j-k] for k in range(4)]) == 'XMAS'):
                    count += 1


    print(count)