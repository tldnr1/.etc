# Level_1/두개_뽑아서_더하기.py

# itertools 대표기능 정리 : https://docs.python.org/ko/3/library/itertools.html

''' combinations(list,2) >> list에서 2개 원소 뽑아서 중복 없이 튜플화 '''
import itertools

numbers = [1,2,3,4,5]
combination = list(itertools.combinations(numbers, 2))
print(combination)
# 여기에 map & lambda + set 을 이용하여 연산도 가능
''' set은 중복요소 제거에 이용! '''
add_2 = list(map(lambda x: x[0]+x[1], combination))
print(list(set(add_2)))