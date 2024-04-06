
x = 0
while True:
	if x % 2 == 0:
		break
	print(x)
	x = x + 1

x = 0
while True:
	if x % 2 == 0:
		continue
	print(x)
	x = x + 1
x = 0
while x < 20:
    x += 1
    print(x, end=' ')

print()


y = 0
tot = 0
while y < 100:
    y += 1
    tot += y
print(tot)

from random import randint

n1 = int(input('숫자 입력 : '))
n2 = randint(1, 10)
n3 = 0
tot = 0

while n2 < n1:
    n2 += 1
    tot += n2
    n3 += 1

print('반복 횟수는 {}번 입니다.'.format(n3))    
print('{}까지의 누적 합은 {} 입니다.'.format(n1, tot))

from random import randint

num = int(input('정수 입력 : '))
rand = randint(1, 10)
tot = 0
cnt = 0
while True:
    tot += rand
    cnt += 1
    if num <= tot:
        tot = tot - rand
        print('누적합 : {}\n반복 횟수 : {}'.format(tot, cnt))
        break

num1 = int(input('정수 입력 : '))
결과 = ''
while True:
    나머지 = num1 % 2
    num1 = num1 // 2
    결과 = str(나머지) + 결과
    if num1 == 0:
        print(결과)
        break


x = 0
y = 0
while True:
	while True:
		if x == 5:
                    y = y + 1
                    break
            x = x + 1

x = 0
while True:
	while True:
		if x == 5:
                    y = y + 1
                    continue
            x = x + 1




