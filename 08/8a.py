count = 0
with open('8a.txt', 'r') as file:
    data = file.read()
    for line in data.splitlines():
        count += len(eval(line))

    characters = len(data.replace('\n',''))

print characters-count