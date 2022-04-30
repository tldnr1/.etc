'''
< 통과 못한 코드 >
def solution(n, lost, reserve):
  _reserve = [r for r in reserve if r not in lost]  # 여벌을 잃지 않은 학생
  _lost = [l for l in lost if l not in reserve]  # 여벌이 없으나 잃은 학생

  for r in _reserve:
    f = r - 1  # 앞 번호
    b = r + 1  # 뒷 번호
    if f in _lost:  # 여벌 있는 r 기준, f가 여벌이 없다면 삭제
      _lost.remove(f)
    elif b in _lost:
      _lost.remove(b)
  return n - len(_lost)
'''

def solution(n, lost, reserve):
    # 도난 당한 사람, 여분 있는 사람 둘 다 중복해 있는 사람 제거하고 수행
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    answer = n - len(set_lost)
    return answer
  
n = 2
lost = [1,2]
reserve = [1,2]
print(solution(n, lost, reserve))