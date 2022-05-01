# Level_1/k번째수.py

# map + lambda의 활용 설명 : https://tykimos.github.io/2020/01/01/Python_Lambda_Map/

''' 
map 함수 형태 >> map(변환함수, iterator)
'''

def calc(x):
  return x*x

print( list(map(calc, range(1,6))) )


print( list(map(lambda x: x*x, range(1,6))) )


'''
sum + map >> list를 굳이 사용하지 않아도 map에서 요소 순회 가능!
'''

# 각 자리수 더해서 반환하기
def sol(n):
  return sum(map(int, str(n)))

n = 123
print(sol(n))