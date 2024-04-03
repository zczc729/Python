"""
Python 내장 함수

1. 크기 비교 함수
1) max(), min()

max(3,7,-1,5,4) #7 큰 값
min(3,7,-1,5,4) #-1 작은 값
"""
print(max(3,7,-1,5,4))
print(min(3,7,-1,5,4))

"""

2. 연산 함수
1)sum(), pow()
sum([2,4,5,6,10]) # 30 -> []로 감싸져서 나오는 결과값을 리스트라고 함
pow(2,3) # 8 -> 거듭 제곱 -> 2 x 2 x 2
pow(3,3) # 27 -> 3 x 3 x 3
"""
print(sum([2,4,5,6,10]))
print(pow(2,3))
print(pow(3,3))
"""

2) divmod() ->  나누기 함수 -> 몫, 나머지 출력
divmod(10, 3) # (3, 1) -> ()로 감싸져서 나오는 결과값을 튜플이라고 함
divmod(10, 2) # (5, 0)
"""
print(divmod(10, 3))
print(divmod(10, 2))
"""
3. 진법 변환 함수
1) 진법 표현 방법

진법	표현 문자				표현식
2	0,1				0b
8	0,1,2,3,4,5,6,7 		0o
10	0,1,2,3,4,5,6,7,8,9	
16	0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F	0x

0b100 # 10진수 = 4
0o100 # 10진수 = 64
100 # 10진수 = 100
0x100 # 10진수 = 256
"""
print(0b100)
print(0o100)
print(100)
print(0x100)
"""

2) 진법 변환 함수
bin() -> 2진수 값으로 변환
oct() -> 8진수 값으로 변환
hex() -> 16진수 값으로 변환

ex) -> 항상 문자열로서 출력됨
bin(100) # '0b110010'
oct(100) # '0o144'
hex(100) # '0x64'
bin(0x1A) # '0b11010'
oct(0x1A) # '0o32'
hex(0x1A) # '0x1A'
bin(4 + 4) # '0b1000'
oct(0xA + 0xB) # '0o25'
hex(0b15 * 5) # '0xA'
"""
print(bin(100))
print(oct(100))
print(hex(100))
print(bin(0x1A))
print(oct(0x1A))
print(hex(0x1A))
print(bin(4 + 4))
print(oct(0xA + 0xB))
print(hex(0b10 * 5))
"""
3) 그 외 함수
round() -> 반올림
round(11.56, 1) # 11.6 -> 11.56의 소수점 첫번째까지 사용하므로 두번째 자리에서 반올림
round(11.12 ,1) # 11.1
round(5 / 3, 3) # 1.667
"""
print(round(11.56, 1))
print(round(11.12 ,1))
print(round(5 / 3, 3))
"""
abs() -> 절대값
abs(-5) # 5
abs(5) # 5
"""
print(abs(-5))
print(abs(5))
"""
과제 1)
1. 32, 45, 48, 57, 84 중 가장 큰 값과 작은 값을 구하시오
2. 29, 95, 15, 85, 66의 총 합을 구하시오
3. 29, 95, 15, 85, 66의 평균을 구하시오
4. 29, 95, 15, 85, 66의 평균이 아닌 몫과 나머지를 구하시오
5. 3, 4, 8, 5 중 큰 값에서 작은 값의 거듭 제곱을 구하시오
"""
print('최댓값 :', max(32, 45, 48, 57, 84), '최솟값 :', min(32, 45, 48, 57, 84))
print('총 합 :', sum([29, 95, 15, 85, 66]))
print('평균 :', sum([29, 95, 15, 85, 66]) / 5)
print('몫, 나머지 :', divmod(sum([29, 95, 15, 85, 66]), 5))
print('거듭제곱 :', pow(max(3, 4, 8, 5), min(3, 4, 8, 5)))
"""
과제 2)
1. 16진수 값 3D5F의 10진수 값은 무엇인가?
2. 10진수 1024의 16진수 값은 무엇인가?
3. 0x35의 2진수 값은 무엇인가?
4. 0o35의 16진수 값은 무엇인가?
5. 3452 + 5785의 16진수 값은 무엇인가?
6. 0xAC + 200의 2진수 값은 무엇인가?
"""
print(0x3D5F)
print(hex(1024))
print(bin(0x35))
print(hex(0o35))
print(hex(3452 + 5785))
print(bin(0xAC + 200))




