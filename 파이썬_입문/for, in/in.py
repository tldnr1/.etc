# https://pydole.tistory.com/entry/Python-%ED%8F%AC%ED%95%A8Containment-%EC%97%B0%EC%82%B0%EC%9E%90-in-not-in

# in 은 if문, for문, while문 등 다양하게 사용 가능

# 또한 다양한 자료형에도 활용 가능(문자열, 리스트, 튜플, 딕셔너리)
# 단, 딕셔너리는 Key만 이용 가능

# 문자열
if 'p' in 'python':
  print(True+1)

# 리스트
if 'p' in 'python':
  print(True+2)
  
# 튜플
if 'a' in ('a', 'b', 'c'):
  print(True+3)
  
# 리스트
if 'a' in {'a':1, 'b':2}:
  print(True+4)

# 참고로 True는 1 이다
if True == 1:
  print('참고로 True는', int(True), '이다')