# 넓이 구하기 문제 등과 같이 중복영역이 많은 문제는 배열(리스트) 활용
#  ㄴ 값으로 처리하려하면 반복되는 공간을 뺐다 더했다해주기 힘들어짐
#  ㄴ 그냥 배열에 중복되는 위치 1로 고정해두고 나중에 1 개수 세는게 편함

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


'''
위에 코드 map 출력해보면
문제랑 x, y축 바뀌어있음

복습할 때 코드 새로 짜서
x, y축 맞춰보기!!
'''