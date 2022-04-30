import itertools

def solution(numbers):
  combination = list(itertools.combinations(numbers, 2))
  answer = list(map(lambda x: x[0]+x[1], combination))
  return sorted(list(set(answer)))

numbers = [5,0,2,7]
print(solution(numbers))