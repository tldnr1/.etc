# 틀린 문제 기록

# 조건 n은 1 ~ 29 => 1의 자리에만 369 나옴
n = int(input())
for i in range(1, n+1):
    if i%10 in [3,6,9]:  # 369 게임은 3의 배수 찾는게 아니므로 10단위로 분리해줌
        print('X', end=' ')
    else:
        print(i, end=' ')