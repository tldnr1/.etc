# Level_1/k번째수.py

# map + lambda의 활용 설명 : https://tykimos.github.io/2020/01/01/Python_Lambda_Map/

''' 
map 함수 형태 >> map(변환함수, iterator)
'''

def calc(x):
  return x*x

print( list(map(calc, range(1,6))) )


print( list(map(lambda x: x*x, range(1,6))) )