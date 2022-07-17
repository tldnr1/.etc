# 모든 경우 if문으로 처리해서 푼 풀이임
# 깔끔하게 해결할 수 있는 방법 없나..?

p = [[0]*4 for _ in range(3)]
# p[0][0] : score, p[0][1~3]: point_cnt

n = int(input())
for _ in range(n):
  x = list(map(int, input().split()))
  for i in range(3):
    p[i][0] += x[i]
    p[i][x[i]] += 1

# p[0][4] : candidate number
for i in range(3):
  p[i].append(i+1)

p.sort(key = lambda x: x[0], reverse=True)

p_max = p[0][0]
if p_max == p[1][0] and p_max != p[2][0]:
  # 3 point
  if p[0][3] > p[1][3]: print(p[0][4], p_max)
  elif p[0][3] < p[1][3]: print(p[1][4], p_max)
  else: # 2 point
    if p[0][2] > p[1][2]: print(p[0][4], p_max)
    elif p[0][2] < p[1][2]: print(p[1][4], p_max)
    else:
      print(0, p_max)
elif p_max == p[1][0] and p_max == p[2][0]:
  p.sort(key = lambda x: x[3], reverse=True)
  _max = p[0][3]
  if _max != p[1][3] and _max != p[2][3]:
    print(p[0][4], p_max)
  elif _max == p[1][3] and _max != p[2][3]:
    if p[0][2] > p[1][2]: print(p[0][4], p_max)
    elif p[0][2] < p[1][2]: print(p[1][4], p_max)
    else: print(0, p_max)
  else:
    p.sort(key = lambda x: x[2], reverse=True)
    _max = p[0][2]
    if _max != p[1][2]:
      print(p[0][4], p_max)
    elif _max == p[1][2] and _max != p[2][2]:
      if p[0][2] > p[1][2]: print(p[0][4], p_max)
      elif p[0][2] < p[1][2]: print(p[1][4], p_max)
      else: print(0, p_max)
    else: print(0, p_max)
else:
  print(p[0][4], p_max)