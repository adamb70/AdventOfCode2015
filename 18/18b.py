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


def setCorners(dic):
    corners = (0, 0), (0, size-1), (size-1, 0), (size-1, size-1)
    for n in corners:
        dic[n] = 1


def neighboursOn(x, y):
    count = 0
    for a in range(x-1, x+2):
        for b in range(y-1, y+2):
            if (a, b) != (x, y):
                count += coords[(a, b)]
    return count


setCorners(coords)

steps = 100
for step in range(steps):
    nextStep = defaultdict(int)
    setCorners(nextStep)

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

    setCorners(nextStep)
    coords = nextStep


print sum(coords.values())