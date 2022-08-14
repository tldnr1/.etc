"""
< 내가 쓴 코드 >
def solution(x):
  x_str = str(x)
  x_sum = sum(list(map(int, x_str)))
  if x % x_sum == 0:
    return True
  else:
    return False
"""

''' < 모범 답안 > '''
def solution(x):
  return x % sum([int(c) for c in str(x)]) == 0  # == 0에 대한 T,F를 반환
x = 12
print(solution(x))