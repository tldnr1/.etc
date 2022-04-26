def solution(array, commands):
  answer = []
  for command in commands:
    # i : command[0] / j : command[1] / k : command[2]
    sorted_arr = sorted(array[command[0]-1:command[1]])
    answer.append(sorted_arr[command[2]-1])
  return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))


''' 모범 답안 '''
"""
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
"""

# map + lambda의 활용 설명 : https://tykimos.github.io/2020/01/01/Python_Lambda_Map/

# 위 링크에 map, lambda 개별 설명도 있는데 확인해보기!

# 아래 코드는 '369게임'
# list(map(lambda x: '짝' if x % 3 == 0 else x, range(1, 10)))
#  ㄴ 이런 식으로 lambda에 if-else 문을 넣어서 사용할 수도 있음