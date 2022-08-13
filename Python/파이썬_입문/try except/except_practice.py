# 참고한 사이트 : https://python.bakyeono.net/chapter-9-4.html

'''
< raise vs. assert > 
비교                          raise 문	             assert 문
용도                         예외의 발생	           상태의 검증
언제 예외를 일으키는가?	         항상             검증식이 거짓일 때만
어떤 예외를 일으키는가?	      지정한 예외	           AssertionError

* 사용 방법
  raise 예외클래스(메시지)
  assert 검증식, 오류메시지

* 사용 시기
  raise : 오류를 체계적으로 관리해야 할 때
  assert : 간단한 오류 검사 목적
''' 


# 예제 : 은행 계좌 관련 예외
'''
BaseException
  ㄴ Exception
    ㄴ AccountException (계좌 관련 예외)
      ㄴ AccountBalanceException (계좌 잔고 예외)
      ㄴ FrozenAccountException (동결 계좌 예외)
      ㄴ InvalidTransctionException (잘못된 입출금 예외)

AccountExceptions.py 를 만들어서 끌어와보기!
'''

import AccountExceptions as AE
try:
  raise AE.AccountBalanceException()
  print(1)
except AE.AccountBalanceException() as e:
  print(e.isRaised())