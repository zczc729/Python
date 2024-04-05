

# input()
a = input('문자열 입력 : ')
print(type(a))




age = int(input('나이 : '))
name = input('이름 : ')

print('{}님의 나이는 {}세 입니다.'.format(name, age))
print('100세 까지 남은 해는 {}년 입니다.'.format(100 - age))


n1 = int(input('첫 번 째 수 입력 : '))
n2 = int(input('두 번 째 수 입력 : '))
print('더하기 : {}\n빼기 : {}\n곱하기 : {}\n나누기 : {:.2f}'.format(n1 + n2, n1 - n2, n1 * n2, n1 / n2))

name = input('이름 : ')
height = float(input('키 : '))
weight = float(input('체중 : '))

print('{} 님의 비만도는 {:.2f}% 입니다.'.format(name, weight / (height - 100) * 0.9 * 100))
