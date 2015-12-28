from collections import defaultdict

output = (3010, 3019)
paper = defaultdict(int)


def remainder(value):
    return value * 252533 % 33554393


paper[(1, 1)] = 20151125
prev = 20151125

h, l = 2, 1
turn = 2

while paper[output] == 0:
    for n in range(turn):
        paper[(h, l)] = remainder(prev)

        prev = paper[(h, l)]

        if h != 1:
            h -= 1
            l += 1

    turn += 1
    h, l = turn, 1


print paper[output]