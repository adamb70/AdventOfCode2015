OFF = 0
ON = 1
TOGGLE = 2

processed = []
with open('6.txt', 'r') as file:
    for line in file.readlines():
        line = line.strip()
        line = line.replace(' through ', '), (')+')'
        line = line.replace('turn on ', str(ON)+', (')
        line = line.replace('turn off ', str(OFF)+', (')
        line = line.replace('toggle ', str(TOGGLE)+', (')
        processed.append(eval(line))

grid = {}
for n in range(0, 1000):
    for i in range(0, 1000):
        grid[(n, i)] = 0

for value, start, end in processed:
    width = end[0] - start[0]
    height = end[1] - start[1]

    for w in range(0, width+1):
        for h in range(0, height+1):
            if value == TOGGLE:
                grid[(start[0]+w, start[1]+h)] = abs(grid[(start[0]+w, start[1]+h)]-1)
            else:
                grid[(start[0]+w, start[1]+h)] = value

print sum(grid.values())


# Visualisation
from PIL import Image
img = Image.new('RGB', (1000,1000))
for key in grid.keys():
    if grid[key] == 1:
        img.putpixel((key[0],key[1]), (255, 255, 255))

img.save('img.png', 'PNG')