# py04_module.py
import math

# 수학모듈: 수학함수들이 모여있는 파이썬 모듈
import math

print(math.pi)

PI = 3.141592
# 2 ** 10 -> int
print(math.pow(2, 10)) # float
print(math.sqrt(4))
print(math.log2(5))
print(math.cos(30))

# import 는 파일 맨 위에 올리는게 좋다.
# TIP!! Alt + 방향키 한 줄씩 코드 올릴 수 있음
import random

numbers = [i for i in range(1, 45 + 1)] # 1~45 리스트로
result = []

for i in range(6): # 여섯번 반복
    result.append(random.choice(numbers))

print(result)
# 초간단 로또
# weight: 가중치
numbers = weight=list(range(1, 45+1))
random.shuffle(weight)
result = random.choices(numbers, weights=weight, k=6)
print(result)