# 문제 조건 빼먹어서 틀린 문제
# 문제 조건 확실하게 파악하고 코드 작성할 것!!

extra_pay = 0
extra_time = 0

for _ in range(5):
  s, e = map(float, input().split())
  if e-s-1 >= 4:
    extra_time += 4
  elif e-s-1 > 0:
    extra_time += e-s-1

extra_pay = extra_time * 10000

if extra_time <= 5:
  extra_pay *= 1.05
elif extra_time >= 15:
  extra_pay *= 0.95

print(int(extra_pay))
