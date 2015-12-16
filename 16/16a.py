from collections import defaultdict

aunts = {}
with open('16.txt', 'r') as file:
    for line in file:
        line = line.replace(':', '').replace(',', '').strip().split()
        aunts[int(line[1])] = zip(line[2::2], line[3::2])


for aunt in aunts:
    values = defaultdict(str, aunts[aunt])

    if 'children' in values and values['children'] != '3':
        continue
    if 'cats' in values and values['cats'] != '8':
        continue
    if 'samoyeds' in values and values['samoyeds'] != '2':
        continue
    if 'pomeranians' in values and values['pomeranians'] != '3':
        continue
    if 'akitas' in values and values['akitas'] != '0':
        continue
    if 'vizslas' in values and values['vizslas'] != '0':
        continue
    if 'goldfish' in values and values['goldfish'] != '5':
        continue
    if 'trees' in values and values['trees'] != '3':
        continue
    if 'cars' in values and values['cars'] != '2':
        continue
    if 'perfumes' in values and values['perfumes'] != '1':
        continue

    print aunt