import re

data = []
with open('5.txt', 'r') as file:
    for line in file:
        data.append(line)

result = []
for word in data:
    if len(re.findall('[aeiou]', word)) > 2:
        if re.search(r'(\w)(\1)', word):
            if not re.search(r'ab|cd|pq|xy', word):
                result.append(word)

print len(result)