import re

encoded = 0
with open('8a.txt', 'r') as file:
    data = file.read()
    for line in data.splitlines():
        encoded += len(re.escape(line)) + 2

    characters = len(data.replace('\n',''))

print encoded-characters