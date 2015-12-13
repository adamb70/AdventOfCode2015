import json

with open('12.txt', 'r') as file:
    data = json.loads(file.read())


def loop(item):
    if type(item) == int:
        return item
    elif type(item) == list:
        value = 0
        for n in item:
            value += loop(n)
        return value
    elif type(item) == dict:
        if 'red' in item.values() or 'red' in item:
            return 0
        value = 0
        for key in item:
            value += loop(key)
            value += loop(item[key])
        return value
    else:
        return 0



total = 0
total += loop(data)

print total