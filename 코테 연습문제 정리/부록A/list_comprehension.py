# 1차원 리스트 - 0~19에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)
print()

# 2차원 리스트 - N x M 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)
print()

# 잘못된 2차원 리스트 초기화 (컴프리헨션 미사용)
array = [[0] * m] * n
print(array)
print()

array[1][1] = 5
print(array)
# 내부적으로 포함된 3개의 리스트가 모두 동일한 객체에 대한 3개의 레퍼런스로 인식되기 때문에 위와 같이 출력됨