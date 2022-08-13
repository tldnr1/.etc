'''
< 내가 쓴 코드 > 
import re

def solution(n, arr1, arr2):
  answer = [bin(arr1[i] | arr2[i])[2:] for i in range(n)]  << zip 사용!!
    
  for i in range(n):
    while len(answer[i]) < n:
      answer[i] = ' ' + answer[i]  << rjust로 가능
    answer[i] = re.sub('1', '#', answer[i])  << replace로도 가능
    answer[i] = re.sub('0', ' ', answer[i])
return answer
'''

def solution(n, arr1, arr2):
  answer = []
  for i,j in zip(arr1,arr2):
    a12 = str(bin(i|j)[2:])
    a12=a12.rjust(n,'0')
    a12=a12.replace('1','#')
    a12=a12.replace('0',' ')
    answer.append(a12)
  return answer
  
n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n,arr1,arr2))