instructions = []
with open('23.txt', 'r') as file:
    for line in file:
        line = line.replace(',', '')
        instructions.append(tuple(line.split()))

a = 0
b = 0

i = 0

while True:
    if i > len(instructions)-1:
        break

    n = instructions[i]

    if n[0] == 'hlf':
        if n[1] == 'a':
            a /= 2
        else:
            b /= 2
    elif n[0] == 'tpl':
        if n[1] == 'a':
            a *= 3
        else:
            b *= 3
    elif n[0] == 'inc':
        if n[1] == 'a':
            a += 1
        else:
            b += 1
    elif n[0] == 'jmp':
        i += int(n[1])
        continue
    elif n[0] == 'jie':
        if n[1] == 'a':
            if a % 2 == 0:
                i += int(n[2])
                continue
        else:
            if b % 2 == 0:
                i += int(n[2])
                continue
    elif n[0] == 'jio':
        if n[1] == 'a':
            if a == 1:
                i += int(n[2])
                continue
        else:
            if b == 1:
                i += int(n[2])
                continue

    i += 1

print b