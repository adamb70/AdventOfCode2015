from itertools import combinations
from operator import mul

weights = []
with open('24.txt', 'r') as file:
    for line in file:
        weights.append(int(line.strip()))


def process(weights):
    group_size = sum(weights) / 4
    for i in range(len(weights)):
        QE = [reduce(mul, c) for c in combinations(weights, i)
              if sum(c) == group_size]
        if QE:
            return min(QE)


print process(weights)