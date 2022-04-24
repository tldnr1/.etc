""" comprehension """
# 1 ~ 10 중 짝수의 제곱수만 출력
list = [number**2 for number in range(1,11) if number%2 == 0]
print(list)

''' swap '''
a = 1
b = 2
print(a, b)  # 1, 2

a, b = b, a
print(a, b)  # 2, 1

''' binary search '''
import bisect
mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect.bisect(mylist, 3))

''' class의 자동 string casting '''
class Coord(object):
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
      return '({}, {})'.format(self.x, self.y)

point = Coord(1, 2)
print(point)  # __str__을 호출한 것
# print( '({}, {})'.format(point.x, point.y) ) 
# 위와 같은 출력문 대신 __str__ 을 사용함

''' inf : 매~우 큰 수 '''
if 10000000000000 < float('inf'):  # float('inf')의 형태로 만들어 사용!
  print('inf는 매~우 큰 수이다')


''' 파일 입출력 with~as '''
""" 
 <with~as 의 장점>
1. 파일을 close 하지 않아도 됩니다: with - as 블록이 종료되면 파일이 자동으로 close 됩니다.
2. readlines가 EOF까지만 읽으므로, while 문 안에서 EOF를 체크할 필요가 없습니다.
"""

'''
# with ~ as 사용 안한 버전(c언어)
f = open('myfile.txt', 'r')
while True:
  line = f.readline()
  if not line:
    break
  raw = line.split()
  print(raw)
f.close()

print()
# with ~ as 를 사용한 버전
with open('myfile.txt') as file:
  for line in file.readlines():
    print(line.strip().split('\t')
'''