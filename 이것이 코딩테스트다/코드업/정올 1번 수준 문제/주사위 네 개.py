# Counter에 sorted 활용하는 방법 익히기

from collections import Counter
n = int(input())
max_score = 0
score = 0

for _ in range(n):
  l = list(map(int, input().split()))
  count = sorted(dict(Counter(l)).items(), key = lambda item: item[1], reverse = True)

  if count[0][1] == 4:
    score = 50000 + l[0]*5000
  elif count[0][1] == 3:
      score = 10000 + count[0][0]*1000
  elif count[0][1] == 2:
    if count[1][1] == 2:
      score = 2000 + (count[0][0] + count[1][0])*500
    else:
      score = 1000 + count[0][0]*100
  else:
    score = max(l) * 100

  if max_score < score:
    max_score = score

print(max_score)
