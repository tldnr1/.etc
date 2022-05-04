'''
< 내가 쓴 코드 >
def solution(arr, divisior):
  answer = [num for num in arr if num % divisor == 0]
  if len(answer) == 0:
    return [-1]
  else:
    return sorted(answer)
'''

# or 을 사용한 답안
def solution(arr, divisor):
  return sorted([n for n in arr if n%divisor == 0]) or [-1]

arr = [5, 6, 7, 10]
divisor = 5
print(solution(arr, divisor))