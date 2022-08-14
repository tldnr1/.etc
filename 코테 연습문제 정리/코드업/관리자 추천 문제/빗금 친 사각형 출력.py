# '출력하기' 문제들 중에서
# 자료의 저장이 굳이 필요하지 않다면
# 간단하게 출력만 해줘도 된다!

n, k = map(int, input().split())

for i in range(1, n+1):
  for j in range(1, n+1):
    if i==1 or i==n or j==1 or j==n:
      print('*', end='')
    elif (i+j-1)%k == 0:
      print('*', end='')
    else:
      print(' ', end='')
  print()