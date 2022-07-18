x = 3
y = 5

l = [[0] * x for _ in range(y)]

for i in range(y):
  for j in range(x):
    print(l[i][j], end=' ')
  print()