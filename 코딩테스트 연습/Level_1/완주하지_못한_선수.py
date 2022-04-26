# 아래 코드는 효율성 테스트 통과 못함!!! (해시 미사용)
"""def solution(participant, completion):
  for name in completion:
    participant.remove(name)
  return ''.join(participant)"""
  
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))

