# Level_1/행렬의_덧셈.py

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

''' zip을 이용하면 여러 iterator를 동시에 순회 가능 '''
answer = []
for A,B in zip(arr1, arr2):
  arr = []
  for a,b in zip(A,B):
    arr.append(a+b)
  answer.append(arr)

print(answer)

''' 여기에 comprehension을 적용하면 요약 가능 '''
print( [[a+b for a,b in zip(A,B)] for A,B in zip(arr1,arr2)] )