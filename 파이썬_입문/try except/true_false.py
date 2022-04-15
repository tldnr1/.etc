"""
# 파이썬에서의 True, False
숫자 0을 제외한 모든 수 - true
빈 딕셔너리, 빈 리스트를 제외한 모든 딕셔너리, 리스트 - true
아무 값도 없다는 의미인 None - false
빈문자열을 제외한 모든 문자열 - true

# 예시
a = True or 1    #True   앞의 값이 True입니다.
b = False or 0     #0      앞의 값이 False이므로 뒤의 값을 따릅니다.
c = 0 or False     #False  앞의 값이 0이므로 False입니다. 따라서 뒤의 값인 False를 따릅니다.
d = 1 or False     #1      앞의 값이 1이므로 True입니다.
"""