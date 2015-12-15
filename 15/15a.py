from itertools import permutations, combinations_with_replacement

ingredients = {}
with open('15.txt', 'r') as file:
    for line in file:
        line = line.strip().replace(',','').split()
        ingredients[line[0].rstrip(':')] = (int(line[2]), int(line[4]), int(line[6]), int(line[8]), int(line[10]))


combinations = []
for each in combinations_with_replacement(range(1, 98), 4):
    if sum(each) == 100:
        combinations.append(each)


def getTotal(components, numbers):
    capacity = 0
    durability = 0
    flavour = 0
    texture = 0
    for n in range(0, 4):
        capacity += ingredients[components[n]][0] * numbers[n]
        durability += ingredients[components[n]][1] * numbers[n]
        flavour += ingredients[components[n]][2] * numbers[n]
        texture += ingredients[components[n]][3] * numbers[n]

    if capacity < 1 or durability < 1 or flavour < 1 or texture < 1:
        return 0
    else:
        return capacity * durability * flavour * texture


results = {}
for each in permutations(ingredients, 4):
    for n in combinations:
        results[(each, n)] = getTotal(each, n)


print max(results.values())

print results.keys()[results.values().index(max(results.values()))]