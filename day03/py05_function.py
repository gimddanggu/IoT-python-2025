# py05_function.py

# 함수, Function, Method, Procedure...
# 인자, 파라미터, 매개변수, Parameter, Argument..
# def 함수명(인자1, 파라미터2, 매개변수3):
#   함수 안으로 진입

def say_hi():
    print('안녕~!')
    return None # 정확한 표현 (생략 가능)

def say_hello(name):
    print(f'{name}야, 안녕!!')
    return

def get_age(birthYear):
    age = 2025 - birthYear
    return age

def closing():
    return '바이바이'

print('인사하기:', end=' ')
say_hi() # 함수 호출
# print('이름으로 인사하기:', say_hello('유고')) # return 값이 없어서 None 출력

name = input('이름입력 > ')
print('이름으로 인사하기: ', end = ' ')
say_hello('유고')

year = int(input('생일년도 >'))
real_age = get_age(year)
print(f'나이는 {real_age}세')

print('작별인사: ', closing())

a = [1, 2, 3]
b = a.copy()
print(a)
print(b)
print(a == b)
print(a is b)
print('=====')
a[2] = 9

print(a == b)
print(a is b)

print(a)
print(b)