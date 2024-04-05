from random import random

print(random())
print(random() * 10)
print(int(random() * 10))
print(int(random() * 10) + 1)

from random import randint
from random import randrange
print(randint(5, 10))
print(randrange(5, 10))
print(randrange(5, 10, 2))

print(chr(65))
print(chr(randint(65, 90))) # 'A', 'Z'
print(chr(randint(97, 122))) # 'a', 'z'

print(int(random() * 100) + 1)
print(int(random() * 1000) + 1)
print(int(random() * 900) + 100)

a = chr(int(random() * 26) + 65)
b = chr(int(random() * 26) + 65)
c = chr(int(random() * 26) + 65)
print(a + b + c)

rand = int(random() * 99) + 1
print('{} : {}'. format(rand, not bool(rand % 2)))
print('{} : {}'.format(rand, rand % 2 == 0))
# print(bool(int(random() * 100) % 2 == 0))
