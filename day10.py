for cnt in range(10):
	print('반복 출력')

for cnt in range(10):
	print('{} 번째 반복.'.format(cnt))

for x in range(10):
    print(x)

for x in range(5, 10):
    print(x)

for x in range(1, 10, 2):
    print(x)

for x in range(10, 0, -1):
    print(x, end='')

for char in 'abcde':
	print(char)

for tup in (1, 2, 3, 4, 5):
	print(tup)

for x in range(1,10):
    for y in range(1, 10):

        print('{} x {} = {}'.format(x, y, x * y))


for num1 in range(1, 21):
    print(num1, end=' ')

for num2 in range(1, 21):
    if num2 % 2 == 0:
        print(num2, end=' ')

for num2 in range(2, 21, 2):
        print(num2, end=' ')


for x in range(100, 50, -1):
    if x % 2 == 1:
        print(x, end=' ')

for x in range(1, 51):
    if x % 5 == 0:
        print(x)
    else :
        print(x, end=' ')

num1 = 0
for x in range (1, 101):
    num1 += x

print(num1)

st = 'Python basic program language'

num2 = 0
for x in st:
    if x != ' ':
        num2 += 1

print(num2)

from random import randint

for x in range(10):
    for y in range(8):
        n1 = chr(randint(97,122))
        print(n1, end='')
    print()


from random import randint

for x in range(10):
    for y in range(16):
        z = randint(0, 2)
        if z == 0:
            print(chr(randint(97,122)), end='')
        elif z == 1:
            print(chr(randint(65,90)), end='')
        elif z == 2:
            print(randint(0,9), end='')
    print()
        
        
        
















        
        
