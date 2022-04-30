'''
< 통과 못한 코드 >
def solution(n, lost, reserve):
  # reserve.sort() 추가하면 정답이 됨
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


< 코드 분석 > 
1. 아래는 set을 사용해서 set * for로 시간복잡도가 O(n)인 반면,
    위의 코드는 for, lost로 인해 O(n^2)이다.

2. reserve가 정렬되어 있지 않은 경우 틀리게 됨!
    왜냐하면 Greedy 알고리즘에 의해 순서대로 앞 or 뒤에서 차례로 빌려줘야 하는데,
    reserve가 정렬이 안되어있으면 막 빌려주게 되어서 최선의 결과가 안나옴
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