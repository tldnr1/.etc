# Counter 공식 레퍼런스 : https://docs.python.org/3/library/collections.html#collections.Counter

''' 
Counter 자료형 >> Counter({ ... }) 의 형태를 가짐
                 그래서 Counter(...).items() 처럼 사용하는 경우가 많음
'''

'''
Counter의 대표적인 기능들

1. subtract (뺄셈)   # 그냥 - 로 연산해도 적용된다!
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)  # c-d와 같은 결과  
print(c)    # Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})

2. most_common(n)  (n = None, 1, 2, 3, ...)
    ㄴ 빈도수가 높은 순서대로 n개를 출력

 Counter('hello world').most_common() # [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]

 Counter('hello world').most_common(1) # [('l', 3)]
'''
from collections import Counter
print(Counter('hello world').most_common(4))
    # [('l', 3), ('o', 2), ('h', 1), ('e', 1)]