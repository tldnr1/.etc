a, b = 5, 3
for _ in range(b):
  print('*'*a)

print()
print(('*' * a + '\n') * b)  # 이렇게 괄호로 묶어서 한번 더 곱셈 가능