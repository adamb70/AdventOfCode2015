from math import sqrt
from collections import defaultdict


def factors(n):
    step = 2 if n % 2 else 1
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))


elves = defaultdict(int)
goal = 34000000
for house in range(1, 1000000):
    result = 0
    for elf in factors(house):
        if not elves[elf] >= 50:
            elves[elf] += 1
            result += elf * 11

    if result >= goal:
        print house
        break