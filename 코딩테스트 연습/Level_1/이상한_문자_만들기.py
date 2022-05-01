''' 못풀고 답을 본 문제임 '''
''' 알고리즘은 맞았지만, 아래의 사유로 실패 '''
# 사유
# 1) s.split()과 s.split(' ') 의 차이
# 2) "".join과 " ".join의 차이
def solution(s):
  s_split = s.split(" ")
  wrong_s_split = s.split()  # 띄워쓰기를 다 날려버림!
  print(list(s_split))
  print(list(wrong_s_split))

  for k in range(len(s_split)):
    s_list = list(s_split[k])
    
    for i in range(len(s_list)):
      if i % 2 == 0:
        s_list[i] = s_list[i].upper()
      elif i % 2 == 1:
        s_list[i] = s_list[i].lower()

    s_split[k] = "".join(s_list)

  answer = " ".join(s_split)
  return answer


s = 'try hello  world'
print(solution(s))