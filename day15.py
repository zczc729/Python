# 예제

dic = {'a':1, 'b':2, 'c':3}

print(dic['a'])
dic['c'] = 5 * dic['b']
print(dic['c'])

print(dic)

dic = {1:'a', 2:'b'}
dic = {1.1:'a', 2.1:'b'}
dic = {(1,):'a', (2,):'b'}
# dic = {[1]:'a'} # 에러 / 리스트 자료형은 key로 사용 불가
dic = {1:'a', 2:3, 3:(1,), 4:[1]} # value에는 어떠한 값도 사용 가능

dic = {'a':1, 'b':2, 'c':3}

for k in dic:
	print(k, dic[k])


dl = {'음료':['탄산', '과일', '우유', '물'], '식사':['김밥', '라면', '돈까스', '비빔밥']}

for key in dl:
	print(dl[key])

for key in dl:
	print(dl[key][0])

ld = [{'name':'Park', 'age':25, 'blood':'B'},
      {'name':'Kim', 'age':27, 'blood':'A'}
]

for dic in ld:
	print(dic['name'], dic['age'], dic['blood'])

dd = {'Park':{'age':25, 'blood':'B'},
      'Kim':{'age':37, 'blood':'A'}
}

for name in dd:
	print(name, dd[name]['age'], dd[name]['blood'])


# update 예제

dic = {'a':1, 'b':2, 'c':3}

dic.update({'a':4, 'd':5})
print(dic)

# fromkeys 예제

k = ['a', 'b', 'c', 'd']

dic1, dic2 = {}, {}

dic1 = dic1.fromkeys(k)
dic2 = dic2.fromkeys(k, 1)

print(dic1)
print(dic2)

# get 예제

dic = {'a':1, 'b':2, 'c':3}

print(dic.get('b'))
print(dic.get('d', 'Not eixst key'))

print(dic)

# keys 예제

dic = {'a':1, 'b':2, 'c':3}

for key in dic.keys():
	print(key)

# values 예제

dic = {'a':1, 'b':2, 'c':3}

for value in dic.values():
	print(value)

# items 예제

dic = {'a':1, 'b':2, 'c':3}

for key, value in dic.items():
	print(key, value)

# pop 예제

dic = {'a':1, 'b':2, 'c':3}

print(dic.pop('b'))
print(dic)

# popitem 예제

dic = {'a':1, 'b':2, 'c':3}

print(dic.popitem())
print(dic)
	
# clear 예제

dic = {'a':1, 'b':2, 'c':3}

dic.clear()
print(dic)


# 과제 1)

# 1.
menu = {'칼국수':6000,
        '비빔밥':5500,
        '돼지국밥':7000,
        '돈까스':7000,
        '김밥':2000,
        '라면':2500
        }

# 2.

for k in menu:
    if menu.get(k) < 6000:
        print('메뉴 : {}\n가격 : {}원'.format(k, menu.get(k)))

# 강사
for key in menu.keys():
    if menu[key] < 6000:
        print('메뉴 : {}\n가격 : {}원'.format(key, menu[key]))

# 3.
'''
user_menu = input('메뉴 입력 : ')
user_price = int(input('가격 입력 : '))

menu.update({user_menu:user_price})

print(menu)
'''

# 4.

from random import random



key = tuple(menu.keys())
rand = int(random() * len(key))

print('메뉴 : {}\n가격 : {}'.format(key[rand],menu[key[rand]]))












