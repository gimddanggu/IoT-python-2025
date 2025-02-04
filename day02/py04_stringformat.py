# py04_stringformat.py
# 문자열 포맷팅

loginTemp = '안녕하세요, %s님!'
name = '유고'

# print(loginTemp % (name))
# name = input('로그이할 이름 입력 >')
# print(loginTemp % (name))

## 구세대 문자열 포맷팅팅
intro = '나는 %s(이)고 , %d살입니다. 몸무게 %fkg입니다.'
#name, age, weight = input().split()
#age = int(age)
#weight = float(weight)
print(intro %('김다현', 25, 59))
#print(intro %(name, age, weight))

intro = '나는 %10s(이)고 , %03d살입니다. 몸무게 %3.1fkg입니다.' # 10 칸을 채우라는 의미
print(intro %('김다현', 25, 59))

## 중간세대 문자열 포맷팅
## {0:>10s} 로 %10s와 동일하게 적용
intro = '나는 {0:<10}이고, {1}살입니다. 몸무개는{2}kg 입니다.'
print(intro.format('육오', 48, 65.5))

## 신세대 문자열 포맷팅
name ='ddsf'
age = 47
weight = 76.9
intro = '나는 {name}이고, {age}살입니다. 몸무개는{weight}kg 입니다.'
print(f'나는 {name}이고, {age}살입니다. 몸무개는{weight}kg 입니다.')
