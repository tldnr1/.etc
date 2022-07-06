# 이진탐색 쉽게 구현
# '정렬된 배열'에서 특정한 원소를 찾아야 할 때 매우 효과적

# bisect_left(a, x) : 리스트 a에 x를 삽입할 위치의 인덱스를 왼쪽 기준 반환
# bisect_right(a, x) : 리스트 a에 x를 삽입할 위치의 인덱스를 오른쪽 기준 반환

from bisect import bisect_left, bisect_right
# 파일 명이 bisect.py 였을 때 'most likely due to a circular import' 오류 발생
# "from bisect" 에서 'bisect 모듈'과 'bisect.py'를 동일하게 인식하여 그럼

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))
print()


"""
'정렬된 리스트'에서 '값이 특정 범위에 속하는 원소의 개수'를 구할 때 유용함
"""

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
  right_index = bisect_right(a, right_value)
  left_index = bisect_left(a, left_value)
  return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a, 4, 4)) # 값이 4인 데이터 개수 출력
print(count_by_range(a, -1, 3)) # 값이 [-1 ,3]인 데이터 개수 출력