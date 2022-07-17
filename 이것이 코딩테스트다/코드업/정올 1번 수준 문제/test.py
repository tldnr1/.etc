score = [0, 0, 0]
p = [[0]*3 for _ in range(3)]

n = int(input())
for _ in range(n):
  x = list(map(int,input().split()))

  for i in range(3):
    score[i] += x[i]
    p[i][x[i]-1] += 1

max_score = max(score)
max_cnt = 0
for i in range(3):
  if max_score == score[i]:
    max_cnt += 1

if max_cnt == 1:
  print(score.index(max_score)+1, max_score)
elif max_cnt == 2:
  p3 = []
  for i in range(3):
    if max_score == score[i]:
      p3.append((i+1, p[i][2]))

  if p3[0][1] > p3[1][1]:
    print(p3[0][0], max_score)
  elif p3[0][1] < p3[1][1]:
    print(p3[1][0], max_score)
  else:
    print(0, max_score)
else:
  print(0, max_score)