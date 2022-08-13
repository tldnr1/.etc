"""
< 내가 쓴 코드 > 

def solution(arr1, arr2):
  answer = []
  arr = []
  for a, b in zip(arr1, arr2):
    arr = [x+y for x,y in zip(a, b)]
    answer.append(arr)
  return answer
"""

# comprehension을 이용하여 정리한 코드
def solution(arr1, arr2):
  return [[x+y for x,y in zip(a,b)] for a,b in zip(arr1, arr2)]

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
print(solution(arr1, arr2))