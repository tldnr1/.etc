n = int(input())
sum = 0
_x = []
_y = []

for _ in range(n):
  a, b = map(int, input().split())
  _x.append(a)
  _y.append(b)

map = [[0] * (max(_y)+11) for _ in range(max(_x)+11)]

for k in range(n):
  x, y = _x[k], _y[k]
  for i in range(x, x+10):
    for j in range(y, y+10):
      map[i][j] = 1
  
for i in range(1,len(map)):
  for j in range(1,len(map[0])):
    if map[i][j] == 1:
      sum += 1

print(sum)