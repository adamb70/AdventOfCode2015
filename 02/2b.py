data = []
with open('2.txt', 'r') as file:
    for line in file:
        data.append(map(int, tuple(line.strip().split('x'))))


total = 0
for n in data:
    l, w, h = n

    order = sorted(n)
    total += 2*order[0] + 2*order[1]

    total += l*w*h

print total