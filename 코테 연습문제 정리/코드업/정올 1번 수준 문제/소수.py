# 소수 판별 알고리즘 이해

m = int(input())
n = int(input())
sum = 0
min = 1e9
flag = 0

for i in range(m, n+1):
  if i == 1:  # 1은 소수 아님
    continue
  if i == 2:  # 2는 유일한 짝수 소수
    sum += 2
    min = 2
  if i%2 == 1: # 2가 아닌 짝수는 소수 아님
    flag = 0
    for j in range(3,int(i**0.5)+1): # 홀수 중 소수 판별 조건!!
      if i % j == 0:
        flag = 1
        break
    if flag == 0:
      sum += i
      if i < min:
        min = i

print(sum)
print(min)
