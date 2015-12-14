time = 2503

reindeer = {}
with open('14.txt', 'r') as file:
    for line in file:
        line = line.split()
        reindeer[line[0]] = (line[3], line[6], line[-2])


results = {}
for n in reindeer:
    speed = int(reindeer[n][0])
    travel = int(reindeer[n][1])
    rest = int(reindeer[n][2])

    i = 0
    distance = 0
    while i <= time:
        if i <= time - travel:
            distance += speed * travel
            i += travel + rest
        else:
            distance += (time - i) * speed
            break

    results[n] = distance

print max(results.values())