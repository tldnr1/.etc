"""
< 내가 쓴 코드 >
def solution(num):
  if num % 2 == 0:
    return 'Even'
  else:
    return 'Odd'
"""

""" < 비트 연산을 활용한 답 >"""
def solution(num):
  return ['Even', 'Odd'][num & 1]
  # num & 1 로 짝수 or 홀수 판단
  # 4 = 100(2) 이므로 4 & 2 => 100 & 10 => 110
  # 110 이므로 가장 마지막의 0을 이용. 따라서 [num&1]은 0이 됨
  
num = 4
print(solution(num))