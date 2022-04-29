# Counter 공식 레퍼런스 : https://docs.python.org/3/library/collections.html#collections.Counter

''' 
Counter 자료형 >> Counter({ ... }) 의 형태를 가짐
                 그래서 Counter(...).items() 처럼 사용하는 경우가 많음
'''

'''
Counter의 대표적인 기능들

1. subtract (뺄셈)


2. most_common(n)  (n = None, 1, 2, 3, ...)

 Counter('hello world').most_common() # [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]

 Counter('hello world').most_common(1) # [('l', 3)]
'''