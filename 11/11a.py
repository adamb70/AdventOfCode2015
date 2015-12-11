import re

inp = 'vzbxkghb'

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaback = alphabet[::-1]

run = [''.join(x) for x in zip(alphabet, alphabet[1:], alphabet[2:])]
test = re.compile('|'.join(run))

passed = 0
word = list(inp)

while passed != 3:
    passed = 0
    for i in reversed(range(0, len(word))):
        orig = word[i]
        word[i] = alphaback[alphaback.index(word[i])-1]

        if orig == 'z' and word[i] == 'a':
            pass
        else:
            break


    strword = ''.join(e for e in word)

    if re.search(r'i|o|l', strword):
        continue
    else:
        passed += 1

    if not re.search(test, strword):
        continue
    else:
        passed += 1

    pairs = re.findall(r'([a-z])(\1)', strword)
    if len(pairs) < 2 or len(pairs) % 2 != 0 or len(pairs) != len(set(pairs)):
        continue
    else:
        passed += 1


print ''.join(x for x in word)


