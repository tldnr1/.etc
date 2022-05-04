'''
< 내가 쓴 코드 >
def solution(s):
  p_cnt = 0
  y_cnt = 0
  for x in s:
    if x=='p' or x=='P':
      p_cnt += 1
    elif x=='y' or x=='Y':
      y_cnt += 1

  return [False, True][p_cnt == y_cnt]
'''

# count를 이용한 코드

def solution(s):
  return s.lower().count('p') == s.lower().count('y')
  #                            ㄴ 이처럼 True, False 판단은 조건식만 넘겨줘도 돌아감!