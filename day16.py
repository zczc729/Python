# 인덱싱

st = 'string indexing'

print(st[0])
print(st[7])

# 슬라이싱

st = 'string indexing'

print(st[:6])
print(st[7:])

# 문자열 반복문

st = 'stirng for'

for x in st:
	print(x)


# find 예제

st = 'python string'

print(st.find('string'))

# count 예제

st = 'python string'

print(st.count('t'))

# lower() 예제

st = 'PYTHON STRING'

print(st.lower())
print(st)

# upper() 예제

st = 'python string'

print(st.upper())
print(st)

# strip 예제

st = '  python string  '

print('|' + st + '|')
print('|' + st.strip() + '|')
print('|' + st.lstrip() + '|')
print('|' + st.rstrip() + '|')
print('|' + st + '|')

# replace 예제

st = 'python string'

print(st.replace('string','문자열'))
print(st)

# split 예제

st = 'python string'

print(st.split(' '))

st = 'python,string,integer,float'

print(st.split(','))


user_id = input('아이디 입력 : ')

while True:
    if len(user_id) < 10:
        print('아이디는 10자리 이상이여야 합니다.')
    else:
        user_pw = input('비밀번호  입력 : ')
        if 8 <= len(user_pw) <= 16:
            if user_pw not in user_id:
                cnt = 0
                for k in '~!@#$%^&*_?':
                    if k in user_pw:
                       cnt = 1
                       break;
                if cnt == 0:
                    print('패스워드에는 특수 문자가 반드시 하나 이상 포함 되야 합니다.')
                    break
                else:
                    print('회원 가입 성공')
                    break
            else:
                print('패스 워드에는 아이디가 포함 될 수 없습니다.')
                break;
        else:
            print('패스 워드는 8 ~ 16 자리 사이여야 합니다.')
            break

'''
# 강사 
while True:
    username = input('아이디 입력 : ')
    if len(username) < 10:
        print('아이디는 10자리 이상이여야 합니다.')
    else:
        break;
    password = input('패스 워드 입력 : ')
    if 8 <= len(username) <= 16:
        if username not in password:
            chk = 0
            for s in '~!@#$%^&*_?':
                if s in password:
                    print('회원 가입 완료')
                    chk = 1
                    break;
            if chk == 0:
                    print('패스워드에는 특수 문자가 반드시 하나 이상 포함 되야 합니다.')
            else:
                break;      
            else:
                print('아이디가 패스워드에 포함 될 수 없습니다.')
        else:
            print('패스 워드는 8 ~ 16 자리 사이여야 합니다.')
        
'''







