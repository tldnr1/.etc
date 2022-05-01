"""
< 내가 쓴 코드 >
def solution(n):
  answer = list(map(int, str(n)))
  return list(reversed(answer))
"""

''' < 간단하게 요약한 코드 > '''
# reversed는 list에 쓰는 것이므로 str에도 가능하다!

def solution(n):
  print(reversed(str(n)))
  print(type(reversed(str(n))))
  return list(map(int, reversed(str(n))))
  
n = 12345
print(solution(n))