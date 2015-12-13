from itertools import permutations

values = {}
people = set()
with open('13a.txt', 'r') as file:
    for line in file:
        line = line.rstrip('\n.').split(' ')

        if line[2] == 'lose':
            number = -int(line[3])
        else:
            number = int(line[3])

        values[(line[0], line[-1])] = number
        people.add(line[0])
        people.add(line[-1])


for person in people:
    values[(person, 'me')] = 0
    values[('me', person)] = 0
people.add('me')


results = {}
for each in permutations(people):
    total = 0
    for n in zip(each, each[1:]):
        total += values[n]
    for n in zip(each[::-1], each[-2::-1]):
        total += values[n]

    # For first and last people's values (because table is circle)
    total += values[(each[0], each[-1])]
    total += values[(each[-1], each[0])]

    results[each] = total

print max(results.values())