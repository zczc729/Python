# append 에제
lst = [1, 2, 3]

lst.append('a')
lst.append([4, 'b'])

print(lst)

# extend 예제
lst = [1, 2, 3]
lst.extend(['a', 'b', 'c'])

print(lst)

# insert 예제
lst = [1, 2, 3]
lst.insert(1, 'b')

print(lst)

# pop 예제
lst = [1, 2, 3]

print(lst.pop())
print(lst.pop(0))

print(lst)

lst = [1, 2, 3]
a = lst.pop()
b = lst.pop(0)

print(a, b)

# remove 예제

lst = [1, 2, 3]

print(lst.remove(2)) # None
print(lst)


# clear 예제

lst = [1, 2, 3]

lst.clear()

print(lst)

# count 예제

lst = [1, 2, 3, 1]

print(lst.count(1))

# index 예제

lst = [1, 2, 3, 1]

print(lst.index(2))
print(lst.index(1, 1))

# reverse 예제

lst = [1, 3, 2]

lst.reverse()
print(lst)

# sort 예제

lst = [1, 3, 2]

lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)


# 과제 1
menu = [
	['칼국수', 6000], 
	['비빔밥', 5500], 
	['돼지 국밥', 7000], 
	['돈까스', 7000], 
	['김밥', 2000], 
	['라면', 2500]
]

# 1.

'''
for k in range(len(menu)):
    if menu[k][0] == '비빔밥' or menu[k][0] == '돈까스':
        print(menu[k][1],'원')
'''

for k, v in menu:
    if k in ('비빔밥', '돈까스'):
        print('{} 가격 : {}'.format(k, v))
        
# print('{}원 {}원'.format(menu[1][1], menu[3][1]))

# 2.

'''
user_menu = input('메뉴 입력 :  ')
user_price = int(input('가격 입력 :  '))

menu.append([user_menu,user_price])

print(menu)
'''
'''
user_menu = input('메뉴 입력 :  ')
user_price = int(input('가격 입력 :  '))
s = 0


for k in range(len(menu)):
    if menu[k][0] == user_menu:
        s = 1
        menu[k][1] = user_price
if s == 0:
    menu.append([user_menu,user_price])

print(menu)
'''

from random import randint

auto = randint(0, len(menu) - 1)

print('메뉴 : {}\n가격 : {}'.format(menu[auto][0], menu[auto][1]))


# 강사 
from random import random

auto = int(random() * len(menu))

print('메뉴 : {}\n가격 : {}'.format(menu[auto][0], menu[auto][1]))



        




