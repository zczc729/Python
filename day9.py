"""
if True:
    print('a')
if False:
    print('b')


x = 15
# x= 5
if x > 10:
	print('x는 10보다 크다.')

x = 15
if x in (10,11,12):
	print('x는 10, 11, 12 중 하나에 포함된다.')

x = 15
if type(x) is int:
	print('x는 int형 자료 이다.')

x = 15
if x > 10 and x != 15:
	print('x는 10보다 크면서 15는 아니다.')

if True:
    print('True')
else :
    print('False')

if False:
    print('a')
else :
    print('b')

number = int(input('정수 값 입력 : '))

if number % 3 == 0:
	print('3의 배수이다.')
else :
	print('3의 배수가 아니다')

number1 = int(input('정수 값 입력 : '))

if number1 % 2 == 0 :
    print('{}는 짝수 입니다.'.format(number1))
else :
    print('{}는 홀수 입니다.'.format(number1))

number2 = int(input('첫 번 째 수 입력 : '))
number3 = int(input('두 번 째 수 입력 : '))

if number2 > number3 :
    print('{} - {} = {}'.format(number2, number3, number2 - number3))
else :
    print('{} - {} = {}'.format(number3, number2, number3 - number2))


num1 = int(input('정수 입력 : '))
num2 = int(input('정수 입력 : '))

if (num1 % 2 == 0 and num2 % 2 == 0) or (num1 % 2 == 1 and num2 % 2 == 1) :
    print('{} + {} = {}'.format(num1, num2, num1 + num2))
else :
    print('{} x {} = {}'.format(num1,num2, num1 * num2))

from random import randint

n1 = randint(10, 100)
n2 = randint(10, 100)
n3 = int(input('{} + {} = '.format(n1,n2)))

if n3 == n1 + n2:
    print('정답 입니다.')
else :
    print('오답 입니다.')

score = int(input('점수 입력  : '))

if 90 <= score <= 100:
	print('수 입니다.')
elif 80 <= score < 90:
	print('우 입니다.')
elif 70 <= score < 90:
	print('미 입니다.')
elif 60 <= score < 70:
	print('양 입니다.')
else:
	print('가 입니다.')

"""
"""
if True:
    print('a')
    if True:
    print('b')

"""
"""
    
if True:
    print('a')
    if True:
        print('b')

name = input('이름 : ')
height = float(input('키 : '))
weight = float(input('몸무게 : '))
std_weight = (height - 100) * 0.9
bimando = weight / std_weight * 100

if bimando < 100:
    print('{} 님의 비만도는 {:.2f}%로 저체중 입니다.'.format(name, bimando))
elif 100 <= bimando < 110:
    print('{} 님의 비만도는 {:.2f}%로 정상 입니다.'.format(name, bimando))
elif 110 <= bimando < 120:
    print('{} 님의 비만도는 {:.2f}%로 과체중 입니다.'.format(name, bimando))
elif 120 <= bimando < 130:
    print('{} 님의 비만도는 {:.2f}%로 비만 입니다.'.format(name, bimando))
else :
    print('{} 님의 비만도는 {:.2f}%로 고도 비만 입니다.'.format(name, bimando))

year = int(input('연도 입력 : '))
nyeon = ''

if year % 4 == 0:
    nyeon = '윤년'
    if year % 100 == 0:
        nyeon = '평년'
        if year % 400 == 0:
            nyeon = '윤년'
else :
    nyeon = '평년'

print('{}년은 {} 입니다.'.format(year, nyeon))

"""

"""
year = int(input('연도 입력 : '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('{}년은 윤년'.format(year))
        else:
            print('{}년은 평년'.format(year))
    else:
        print('{}년은 윤년'.format(year))
else:
    print('{}년은 평년'.format(year))

"""




