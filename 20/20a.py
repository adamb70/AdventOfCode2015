from math import sqrt


def factors(n):
    step = 2 if n % 2 else 1
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))


### Simple Brute Force method. Runs in 35s ###
goal = 34000000
for house in range(1, 1000000):
    result = sum(factors(house)) * 10

    if result >= goal:
        print house
        break
##############################################


### Stupidly complicated sampling method that might not even always work. Runs in 10s ###
result = 0
goal = 34000000
s = 1
e = 1000
i = 0
cont = True
over = True
while cont:
    if over:
        for house in range(s, e):
            result = sum(factors(house))*10
            if result >= goal:
                i = house
                break

    if goal/result >= 1:
        s, e = e*10, e*100
    else:
        over = False
        previous = i
        s, e = s-20000, e-20000
        for house in range(s, e):
            result = sum(factors(house))*10
            if result >= goal:
                i = house
                break
        if i == previous:
            cont = False

print i
#########################################################################################