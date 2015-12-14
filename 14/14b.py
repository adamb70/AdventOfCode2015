time = 2503

reindeer = {}
with open('14.txt', 'r') as file:
    for line in file:
        line = line.split()
        reindeer[line[0]] = (line[3], line[6], line[-2])


moveTimes = {}
# Add all seconds of movement to a list for each deer
for n in reindeer:
    times = []
    travel = int(reindeer[n][1])
    rest = int(reindeer[n][2])

    x = 0
    while x <= time:
        if x <= time - travel:
            for i in range(x, x+travel):
                times.append(i)
                x += 1
            x += rest
        else:
            for i in range(x, time+1):
                times.append(i)
                x += 1
            break

    moveTimes[n] = times


distances = dict.fromkeys(reindeer, 0)
points = dict.fromkeys(reindeer, 0)
for i in range(0, time+1):
    for n in reindeer:
        speed = int(reindeer[n][0])

        if i in moveTimes[n]:
            distances[n] += speed

    winner = max(distances.values())
    for deer in [k for k, v in distances.items() if v == winner]:
        # For each deer in the lead (may have a draw)
        points[deer] += 1

print max(points.values())
