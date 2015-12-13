data = []
with open('2.txt', 'r') as file:
    for line in file:
        data.append(map(int, tuple(line.strip().split('x'))))


total = 0
for n in data:
    l, w, h = n

    a = 2*l*w
    b = 2*w*h
    c = 2*h*l

    area = a+b+c
    extra = min(a/2, b/2, c/2)

    total += area+extra

print total