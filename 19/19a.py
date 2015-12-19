import re
from collections import defaultdict

replacements = defaultdict(list)
with open('19.txt', 'r') as file:
    lines = file.readlines()
    for line in lines[:-2]:
        line = line.strip().split(' => ')
        replacements[line[0]].append(line[1])
    inp = lines[-1].strip()


pattern = re.compile('|'.join(replacements))
matches = re.findall(pattern, inp)


results = set()
i = 0
for n in re.finditer(pattern, inp):
    for v in replacements[matches[i]]:
        results.add(inp[0:n.start()] + v + inp[n.end():])
    i += 1

print len(results)

