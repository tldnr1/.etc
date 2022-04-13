'''
# 기본 예외처리
try:
    # 에러가 발생할 가능성이 있는 코드
except Exception: # 에러 종류
    #에러가 발생 했을 경우 처리할 코드

# 예외의 이름을 모르는 경우
try:
    # 에러가 발생할 가능성이 있는 코드
except Exception as ex: # 에러 종류
    print('에러가 발생 했습니다', ex) # ex는 발생한 에러의 이름을 받아오는 변수

* raise : 사용자가 직접 에러를 발생시킴
    raise Exception
'''

# raise 사용 예시
test_result = {
               '1학년' : {'1반' : 80, '2반' : 70, '3반' : 80},
               '2학년' : {'1반' : 70, '2반' : 90, '3반' : 80},
               '3학년' : {'1반' : 90, '2반' : 70, '3반' : 90}
              }

try:
  for grade, classes in test_result.items():
    for class_number, class_result in classes.items():
      if class_result == 90:
        print('{} {} {}점'.format(grade, class_number, class_result))
        raise Exception
except Exception:
  print('{}에서 90점 이상이 최초 발견됨'.format(grade))