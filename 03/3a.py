with open('3.txt', 'r') as file:
    data = file.read()


# METHOD 1
loc = [0, 0]
visited = []

for n in data:
    if n == '^':
        loc[1] += 1
    elif n == '>':
        loc[0] += 1
    elif n == '<':
        loc[0] -= 1
    elif n == 'v':
        loc[1] -= 1
    else:
        print 'error with ' + n
        break

    if str(loc) not in visited:
        visited.append(str(loc))

print len(visited)


# METHOD 2.  0.3 seconds slower, but better method?
"""
currentloc = (0, 0)
visited = [currentloc,]

for n in data:
    x, y = currentloc
    if n == '^':
        y += 1
    elif n == '>':
        x += 1
    elif n == '<':
        x -= 1
    elif n == 'v':
        y -= 1
    else:
        print 'error with ' + n
        break

    currentloc = (x, y)
    if currentloc not in visited:
        visited.append(currentloc)

print len(visited)
"""