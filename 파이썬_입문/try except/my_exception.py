'''
사용자가 직접 예외처리를 하면 코드의 직관성을 높일 수 있다.
파일을 하나 만들어 예외를 정의
 ㄴ e.g.  from 예외모음파일 import 특정예외
Exception 클래스를 상속받아 만든다
 ㄴ e.g. class 예외이름(Exception):
            예외 처리 내용  
'''

''' e.g.
try:
    sign_up( )
except BadUserName:
    print( "이름으로 사용할 수 없는 입력" )
except PasswordNotMatched:
    print( "입력한 패스워드 불일치")
'''

# ! 예외 처리 좀 더 공부하기 !