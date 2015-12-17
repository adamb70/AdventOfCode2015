from itertools import combinations

containers = []
with open('17.txt', 'r') as file:
    for line in file:
        containers.append(int(line))


results = []
for n in range(0, len(containers)):
    for each in combinations(containers, n):
        if sum(each) == 150:
            results.append(len(each))

count = 0
for v in results:
    if v == min(results):
        count += 1

print count