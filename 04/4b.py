from hashlib import md5

inkey = 'ckczppom'

for i in range(0, 100000000):
    key = inkey + str(i)
    hexd = md5(key).hexdigest()
    if hexd.startswith('000000'):
        print i
        break