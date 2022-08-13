# import에서 일어날 수 있는 오류!
# https://hyoje420.tistory.com/45 참고할 것

'''
BaseException
  ㄴ Exception
    ㄴ AccountException (계좌 관련 예외)
      ㄴ AccountBalanceException (계좌 잔고 예외)
      ㄴ FrozenAccountException (동결 계좌 예외)
      ㄴ InvalidTransctionException (잘못된 입출금 예외)
'''

class AccountException(Exception):
  def isRaised(self):
    print('AccountException has been raised')

class AccountBalanceException(AccountException):
  def isRaised(self):
    print('AccountBalanceException has been raised')

class FrozenAccountException(AccountException):
  def isRaised(self):
    print('FrozenAccountException has been raised')

class InvalidTransctionException(AccountException):
  def isRaised(self):
    print('InvalidTransctionException has been raised')