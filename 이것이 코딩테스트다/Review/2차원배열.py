x = 3
y = 5

l = [[0] * x for _ in range(y)]
# [0]이 x개 있는 1차원 배열을, y번 반복한 것
# 따라서 탐색할 때는, y->x 순이여야 함

for i in range(y):  # for _ in range(y)
  for j in range(x):  # [0] * x
    print(l[i][j], end=' ')
  print()