with open('1.txt', 'r') as file:
    data = file.read()

i = 0

for n in data:
    if n == '(':
        i += 1
    elif n == ')':
        i -= 1
    else:
        print 'error with ' + n

print i