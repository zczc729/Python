tup = (1, 2, 3)

print(tup)
print(tup[0])
print(tup[1])
print(tup[-1])
print(tup[-3])

tup = (1, 2, 3)

print(tup)
print(tup[0:2])
print(tup[1:3])
print(tup[:2])
print(tup[-3:-1])
print(tup[-2])




tup = ('a', 'b', 'c', 'd')

for idx in range(4):
	print(tup[idx])

for idx in range(len(tup)):
	print(tup[idx])

for val in tup:
	print(val)



tup = 1, 2, 3, 4

print(type(tup))
print(tup)
print(tup[1])

num1, num2, num3, num4 = tup

print(num1)
print(num2)
print(num3)
print(num4)

tup = (('a', 'b'), ('c', 'd'), ('e', 'f'))

print(tup[0]) # ('a', 'b')
print(tup[1]) # ('c', 'd')
print(tup[2][0]) # 'e'

for val in tup:
	print(val[0], val[1])

for val1, val2 in tup:
	print(val1, val2)



tup = (1, 2, 3, 1, 2)

print(tup.count(2))
print(tup.index(2))
print(tup.index(2, 2))

tup = ('a', 'b', 'c', 'a', 'a')
print(tup.count('a'))

menu = (
    ('칼국수', 6000),
    ('비빔밥', 5500),
    ('돼지 국밥', 7000),
    ('돈까스', 7000),
    ('김밥', 2000),
    ('라면', 2500)
)

print(menu[4][1], menu[5][1])

print('7000원 메뉴')
for k, v in menu:
    if v == 7000:
        print('{} : {}원'.format(k, v))

print('6000원 이하 메뉴')
for k, v in menu: 
    if v <= 6000:
        print('{} : {}원'.format(k, v))

for idx in range(len(menu)):
    if menu[idx][1] <= 6000:
        print(menu[idx][0], menu[idx][1])

user_in = input('메뉴 입력 : ')
cnt = 0

for k, v in menu:
    if k == user_in:
        cnt = cnt + 1
        print('{} : {}원'.format(k, v))
if cnt == 0:
    print('해당 메뉴가 존재하지 않습니다.')


menu = (
    ('칼국수', 6000),
    ('비빔밥', 5500),
    ('돼지 국밥', 7000),
    ('돈까스', 7000),
    ('김밥', 2000),
    ('라면', 2500)
)


print('메뉴 입력을 원치 않으면 \'exit\'을 입력 해주세요.')
tot = 0

while True:
    usermenu = input('메뉴 입력 : ')
    for k, v in menu:
        if k == usermenu:
            tot = tot + v
    if usermenu == 'exit':
        print('총 가격 : {:,}원'.format(tot))
        break



tup = (('a', 'b'), ('c', 'd'), ('e', 'f'))

for val in tup:
	print(val[0], val[1])

for val1, val2 in tup:
	print(val1, val2)









  
