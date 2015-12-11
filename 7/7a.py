inputs = {}
with open('7a.txt', 'r') as file:
    for line in file.readlines():
        line = line.strip()
        line = line.split(' -> ')
        inputs[line[-1]] = line[0].split(' ')


def getValue(wire):
    if wire.isdigit():
        return int(wire)

    command = inputs[wire]

    try:
        if type(command) == int:
            return command
    except AttributeError:
        pass

    if 'NOT' in command:
        x = command[1]
        value = ~ getValue(x)
        inputs[wire] = value
        return value
    elif 'RSHIFT' in command:
        x = command[0]
        y = command[2]
        value = getValue(x) >> getValue(y)
        inputs[wire] = value
        return value
    elif 'LSHIFT' in command:
        x = command[0]
        y = command[2]
        value = getValue(x) << getValue(y)
        inputs[wire] = value
        return value
    elif 'OR' in command:
        x = command[0]
        y = command[2]
        value = getValue(x) | getValue(y)
        inputs[wire] = value
        return value
    elif 'AND' in command:
        x = command[0]
        y = command[2]
        value = getValue(x) & getValue(y)
        inputs[wire] = value
        return value
    else:
        if command[0].isdigit():
            return int(command[0])
        else:
            return getValue(command[0])


print getValue('a')