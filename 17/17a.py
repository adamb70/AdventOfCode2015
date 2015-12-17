from itertools import combinations

containers = []
with open('17.txt', 'r') as file:
    for line in file:
        containers.append(int(line))


results = 0
for n in range(0, len(containers)):
    for each in combinations(containers, n):
        if sum(each) == 150:
            results += 1

print results