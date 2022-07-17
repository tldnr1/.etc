n, k = map(int, input().split())
t = list(map(int, input().split()))

t_sum = sum(t[:k])
t_max = t_sum

for i in range(k, n):
  t_sum += t[i] - t[i-k]
  if t_max < t_sum:
    t_max = t_sum
    
print(t_max)