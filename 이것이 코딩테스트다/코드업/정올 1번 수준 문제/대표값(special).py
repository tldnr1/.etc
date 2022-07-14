# Counter에 대해 공부하기!
# dict(Counter) 에서 list, map, zip 등을 연동해서 쓸 수도 있음
# most_common() 과 같이 자주 쓰이는 함수들은 기억해두기

from collections import Counter

l = []
for _ in range(10):
  n = int(input())
  l.append(n)

d = Counter(l)

print(sum(l)//10)
print(d.most_common(1)[0][0])
