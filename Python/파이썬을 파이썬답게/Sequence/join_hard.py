'''
<문제>
  입력받은 문자열에 대해 가장 많이 등장하는 문자를 출력하기
  단, 입력되는 문자열은 띄워쓰기가 없고 모두 소문자 알파벳이다.

(파이썬을 파이썬답게/Modules/Counter.py 의 문제임)
(출력 부분만 제대로 알아보자)
'''

from collections import Counter

my_str = input("str>> ").strip()
# print(type(my_str))
# print(my_str, end='\n\n')
max_count = max(Counter(my_str).values())
print(''.join(sorted([k for k,v in Counter(my_str).items() if v == max_count])))


# https://python-explorer.tistory.com/3
# split() : 문자열 내부에 있는 공백 또는 특별한 문자를 구분해서, 리스트 아이템으로 만듦
# strip() 함수 :  문자열 앞뒤의 공백 또는 특별한 문자 삭제
#    ㄴ 즉, my_str 을 input().strip()으로 받아야 my_str가 str 타입을 갖는다!!!