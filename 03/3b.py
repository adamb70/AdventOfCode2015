with open('3.txt', 'r') as file:
    data = file.read()


santa = data[::2]
robo = data[1::2]

santaloc = (0, 0)
roboloc = (0, 0)

visited = [(0, 0), ]


def move(who):
    if who == santa:
        pos = santaloc
    else:
        pos = roboloc

    for n in who:
        x, y = pos
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

        pos = (x, y)
        if pos not in visited:
            visited.append(pos)

move(santa)
move(robo)

print len(visited)
