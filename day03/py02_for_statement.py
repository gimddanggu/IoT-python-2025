# py02_forstatement.py

# for문 : 프로그래밍의 꽃
# 반목을 처리할 때 사용
# for 변수 in 반복할값:
#   구문안으로..

# range() 범위 생성 클래스
# 마지막수: max - 1
# range(8) -> range(0, 8)
# range(init, max, add)
# for i in [0, 1, 2, 3, 4, 5, 6, 7] <- 이 조건이 참인동안 반복
for i in range(0, 8):
    print(i)

num = int(input('최대별수: '))

for i in range(1, num+1):
    print('*' * i)


# 구구단
# 2단부터 2x9 ~ 9x9
# 2 x 1 = 2, 2 x 2 = 4, 2 x 3 = 6, 2 x 4 = 8
# 9 x 1 = 9, 9 x 2 = 18, 9 x 3 = 27, 9 x 4 = 36
# 요사1 - 한 줄에 각 단씩 나오도록
# 요사2 - i * j 값이 항상 두 줄씩 표현되도록
for i in range(2, 10):
    if i == 8: break

    print(f'{i}단 시작 ')
    for j in range(1, 10):
        if j == 8: break
        print(f'{i} x {j} = {i*j:2d}', end= '   ')

    print() # 그냥 한 줄 내리기
print('구구단 종료\n\n\n\n')

## 반복문을 빠져나올 때: break
## 반복문에서 특정 조건을 지나칠 때: continue