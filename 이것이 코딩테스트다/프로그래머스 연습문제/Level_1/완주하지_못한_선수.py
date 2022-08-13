# 아래 코드는 효율성 테스트 통과 못함!!! (해시 미사용)
"""def solution(participant, completion):
  for name in completion:
    participant.remove(name)
  return ''.join(participant)"""

from collections import Counter

def solution(participant, completion):
  answer = []
  part = Counter(participant)
  comp = Counter(completion)
  for k,v in comp.items():
    part[k] -= v
  for k,v in part.items():
    for _ in range(v):
      answer.append(k)
  return answer
  

participant = ["mislav", "stanko", "mislav", "ana", "mislav"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))


''' 모범 답안 '''
''' 
from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]'''

### Counter 객체는 뺄셈이 가능하다!!!!! ###

# Hash : https://yunaaaas.tistory.com/46
# Hashing : https://comdoc.tistory.com/entry/17-%ED%95%B4%EC%8B%B1hashing-%ED%8C%8C%EC%9D%B4%EC%8D%AC