# n의 범위가 100,000 이였고 제한시간은 1초 였음
# 따라서 O(n) 내에 무조건 끝나는 코드여야 함 -> 2중 for문 금지
# 2중 for문 예시 => for for  OR  for sum 등  (sum 같은 함수도 for문으로 작동!)

n, k = map(int, input().split())
t = list(map(int, input().split()))

t_sum = sum(t[:k])
t_max = t_sum

for i in range(k, n):
  t_sum += t[i] - t[i-k]
  if t_max < t_sum:
    t_max = t_sum
    
print(t_max)