n = int(input())
num = input()[::-1]

res = ''
for i in range(n):
  res += num[i]
  if (i+1)%3==0:
    res += ','

if res[-1] == ',':
  res = res[:-1]
print(res[::-1])