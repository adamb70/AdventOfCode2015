import re

data = []
with open('5.txt', 'r') as file:
    for line in file:
        data.append(line)

result = []
for word in data:
    if re.search(r'(\w)(\w).*(\1)(\2)', word):
        if re.search(r'(\w)(\w)(\1)', word):
            result.append(word)


print len(result)