'''
사용자가 직접 예외처리를 하면 코드의 직관성을 높일 수 있다.
파일을 하나 만들어 예외들을 정의
 ㄴ e.g.  from 예외모음파일 import 특정예외
Exception 클래스를 상속받아 만든다
 ㄴ e.g. class 예외이름(Exception):
            예외 처리 내용  

[예시]
import BadUserName, PasswordNotMatched from error_zip
(아니면 import * from error_zip)

try:
    sign_up( )
except BadUserName:
    print( "이름으로 사용할 수 없는 입력" )
except PasswordNotMatched:
    print( "입력한 패스워드 불일치")
'''




# ! 예외 처리 좀 더 공부하기 !
# https://docs.python.org/ko/3/tutorial/errors.html

''' 에러 vs 에외 '''
# 에러 : 코딩에 존재하는 문제점을 의미
# 예외 : 코드 실행중에 발생한 에러. 즉, 에러의 하위

# 에러의 종류는 크게 2가지로 봄
# 1. 문법 에러(파싱 에러) : 문법적으로 오류가 있는 코드를 표시해줌
# 2. 예외 : 실행 중 발생한 에러. 문장이나 표현식이 문법적으로 올바르더라도 일어날 수 있음
#     ㄴ e.g. 10 * (1/0) : ZeroDivisionError
