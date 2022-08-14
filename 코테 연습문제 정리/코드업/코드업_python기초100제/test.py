box = [[0]*11 for _ in range(11)]
for i in range(1,11):
    line = list(map(int, input().split()))
    box[i][1:] = line
    
x, y = 2, 2
while 1:
    if box[x][y] == 2:
        box[x][y] = 9
        break
    
    if box[x][y+1] == 1 and box[x+1][y] == 1:
        break
    
    box[x][y] = 9
    if box[x][y+1] == 1: x += 1
    else: y += 1

for i in range(1,11):
  for j in range(1,11):
    print(box[i][j], end=' ')
  print()