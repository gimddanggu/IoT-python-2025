# py02_datastruct.py
# 복합자료형
# 자료구조 및 알고리즘

# 리스트 []
# 리스트 이전전
a = 1
b = 2
c = 3
d = 4
e = 5

sum = a + b + c + d + e
print(sum)

# 리스트(배열) 사용 - 다른 언어에서는 리스트와 배열은 다름
f = [1, 2, 3, 4, 5]
print(f)
print(type(f))

f = ['Life', 'is', True, 0, None, [1, 2 , 3]]
print(f)
print(f[0])

# 리스트의 한 요소에도 값을 집어넣을 수 있음
f[3] = 100
print(f)

## 튜플 ()
# 리스트와 거의 흡사. 갑을 변경할 수 없음
t = (1, 2, 3, 4)
print(t)
print(t[3])
# t[0] = 5  # 주석 토글 Ctrl + /
# # 튜플은 값을 변경하지 못 한다.

print(type(t))

## 딕셔너리(사전형) {key : value}의 집합
spiderman = {'name':'Peter Parker', 'age': 20, 'weapon': 'Web Shooter'}
print(spiderman)
print(type(spiderman))

print(spiderman['name'])
spiderman['age'] = 21
print(spiderman)


## 집합 Set (), {}, [] 모두 사용 가능, 수학의 집합과 동일, 중복제거, 리스트처럼 인덱스가 없음음
# 일반적으로 [] 사용
s = set([1, 3, 5, 7, 9, 5])
print(s)
print(type(s))

s = set('Hello World')
print(s)

## 변수명 지정 방식
## 의미있는 단어들의 조합으로 만들 것
phoneNumber = '010-6667=773'
salaryBankAccount ='866-12-335566'
samsung = ' ' 
samsung1 = ''
# 1samsung = ''  # 숫자로 변수명을 시작불가
_samsung = '' # _이외의 특수문자는 사용불가
# samsung! = ''
# samsung* \ ''
# samsung-apple = '' # 파이썬 연산자는 사용불가