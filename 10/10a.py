def process(num):
    count = 1
    curnum = ''
    result = ''
    for n in num+' ':
        if curnum == n:
            count += 1
        elif curnum == '':
            curnum = n
        else:
            result += str(count) + curnum
            count = 1
            curnum = n

    return result


input = '1321131112'

for i in range(0, 40):
    input = process(input)


print len(input)