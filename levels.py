level_1 = []
f = open('level.txt', 'r')
for line in f:
    level_1.append(line[0:len(line) - 1])
