from itertools import permutations

with open('9a.txt', 'r') as file:
    distances = {}
    places = set()
    for line in file.readlines():
        lst = line.replace(' to ', ' = ').strip().split(' = ')
        distances[(lst[0], lst[1])] = int(lst[2])
        distances[(lst[1], lst[0])] = int(lst[2])

        places.add(lst[0])
        places.add(lst[1])


results = []
for each in permutations(places):
    sum = 0
    for x,y in zip(each, each[1:]):
        sum += distances[(x, y)]
    results.append(sum)


print min(results)