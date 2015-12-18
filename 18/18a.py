from collections import defaultdict

initial = []
with open('18.txt', 'r') as file:
    for n in file.readlines():
        initial.append(n.replace('\n',''))


coords = defaultdict(int)
size = 100
for x in range(size):
    for y in range(size):
        coords[(x, y)] = 0 if initial[x][y] == '.' else 1


def neighboursOn(x, y):
    count = 0
    for a in range(x-1, x+2):
        for b in range(y-1, y+2):
            if (a, b) != (x, y):
                count += coords[(a, b)]
    return count


steps = 100
for step in range(steps):
    nextStep = defaultdict(int)

    for x in range(size):
        for y in range(size):
            if coords[(x, y)] == 1:
                if neighboursOn(x, y) == 2 or neighboursOn(x, y) == 3:
                    nextStep[(x, y)] = 1
                else:
                    nextStep[(x, y)] = 0
            else:
                if neighboursOn(x, y) == 3:
                    nextStep[(x, y)] = 1
                else:
                    nextStep[(x, y)] = 0

    coords = nextStep


print sum(coords.values())