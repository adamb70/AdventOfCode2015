from collections import defaultdict

aunts = {}
with open('16.txt', 'r') as file:
    for line in file:
        line = line.replace(':', '').replace(',', '').strip().split()
        aunts[int(line[1])] = zip(line[2::2], line[3::2])


def default():
    return 9999


for aunt in aunts:
    values = defaultdict(default, aunts[aunt])

    if 'children' in values and int(values['children']) != 3:
        continue
    if 'cats' in values and int(values['cats']) <= 8:
        continue
    if 'samoyeds' in values and int(values['samoyeds']) != 2:
        continue
    if 'pomeranians' in values and int(values['pomeranians']) >= 3:
        continue
    if 'akitas' in values and int(values['akitas']) != 0:
        continue
    if 'vizslas' in values and int(values['vizslas']) != 0:
        continue
    if 'goldfish' in values and int(values['goldfish']) >= 5:
        continue
    if 'trees' in values and int(values['trees']) <= 3:
        continue
    if 'cars' in values and int(values['cars']) != 2:
        continue
    if 'perfumes' in values and int(values['perfumes']) != 1:
        continue

    print aunt