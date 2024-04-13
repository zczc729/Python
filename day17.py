def func():
    pass

def func():
    '''
        함수 기능 설명
        함수 결과 예제
    '''
    pass

func()

def funcHello():
	print('Hello Python')

def funcVersion():
	print('''
	Title: Python Programming Basic
	Version : 1.0 Ver''')

funcHello()
funcVersion()

# 정수, 실수, 문자열

def funcInt():
	return(10)

var = funcInt() + 10
print(var)

# 실수 반환

def funcFloat():
	return 0.1

var = funcFloat() + 10
print(var)

# 문자열 반환

def funcStr():
	return 'string'

var = funcStr() + 'python'
print(var)

# 튜플

def funcTuple():
	return (1, 2, 3)

var = funcTuple()
print(var)

# 리스트

def funcList():
	return [1, 2, 3]

var = funcList()
print(var[0], var[1], var[2])

# 사전

def funcDict():
	return {'a':1, 'b':2}

var = funcDict()
print(var['a'], var['b'])

def func(arg):
	print(arg)

func(1)

def func(arg1, arg2):
	print(arg1, arg2)

func('a', 'b')

def func(arg = 1):
	print(arg)

func(5)
func()

def func(arg1, arg2 = 2):
	print(arg1, arg2)

func(5, 10)
func(5)

def func(arg1, arg2):
	print(arg1, arg2)

func(5, 10)
func(arg2 = 3, arg1 = 1)

def func(arg1, arg2 = 1, arg3 = 2):
	print(arg1, arg2, arg3)

func(5, 2, 4)
func(5, arg3 = 4)

def func(arg, *args):
	print(arg, args)

func(1, 2, 3, 4, 5)


def func(arg, **kwargs):
	print(arg, kwargs)

func(1, key1 = 10, key2 = 'a')

a = 1
b = 2

def func():
	print(a,b)

func()
print(a,b)

def func():
	a = 1
	b = 2
	print(a, b)

func()
# print(a, b) 에러

a, b = 1, 2

def func():
	a, b = 3, 4
	print(a, b)

func()
print(a, b)

# 과제 1

# 1)

def programInfo():
        print('''
    Version : 1.0
    Update Date : 2017-01-01
    Author : Project Python
            ''')

programInfo()

'''
def pyMax():
    if n1 < n2:
        print('큰 값 :', n2)
    elif n2 < n1:
        print('큰 값 :', n1)

def pyMin():
    if n1 < n2:
        print('작은 값 : ', n1)
    elif n2 < n1:
        print('작은 값 : ', n2)
'''

# 2)

def pyMax(*args):
    mx = args[0]
    for x in args[1:]:
        if mx < x:
            mx = x
    return mx

def pyMin(*args):
    mn = args[0]
    for x in args[1:]:
        if x < mn:
            mn = x
    return mn
        

print('큰 값 :', pyMax(145,16,7,131256,1714))
print('작은 값 :', pyMin(145,16,7,131256,1714))


# 3)

from random import random

# 0 ~ N, M ~ N
def myrandom(min, max = 0):
    if max == 0:
        min, max = max, min
        
    return int(random() * (max - min + 1)) + min

print(myrandom(5))
print(myrandom(1, 5))


