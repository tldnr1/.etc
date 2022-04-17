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
# 에러와 예외 : https://docs.python.org/ko/3/tutorial/errors.html
# 예외의 분류-정의-발생 : https://python.bakyeono.net/chapter-9-4.html
# try, except, else, finally : https://blockdmask.tistory.com/537

''' 에러 vs 에외 '''
# 에러 : 코딩에 존재하는 문제점을 의미
# 예외 : 코드 실행중에 발생한 에러. 즉, 에러의 하위

# 에러의 종류는 크게 2가지로 봄
# 1. 문법 에러(파싱 에러) : 문법적으로 오류가 있는 코드를 표시해줌
# 2. 예외 : 실행 중 발생한 에러. 문장이나 표현식이 문법적으로 올바르더라도 일어날 수 있음
#     ㄴ e.g. 10 * (1/0) : ZeroDivisionError


''' 예외 처리 예시들 '''
# 1번) 정수를 입력받기
while True:
  print('<예시 1번>')
  try:
    x = int(input("정수를 입력하세요: "))
    break  # 성공 시 while문 종료를 위함
  except ValueError:
    print("정수가 아닙니다. 다시 입력해주세요", end="\n\n")
print('성공!', end="\n\n")


# 2번) 다양한 예외를 한번에 pass 처리하기
print('<예시 2번>')

def get(key, dataset):
    """데이터 집합(dataset)에서 인덱스(키)에 해당하는 값을 반환한다.
    데이터 집합에 해당하는 인덱스(키)가 존재하지 않는 경우,
    None을 반환한다.
    """
    try:
        value = dataset[key]
    except (IndexError, KeyError):  # 두 예외를 함께 처리
        return None
    else:
        return value
''' 이때 except(line 59)에서 IndexError와 KeyError의 상위 범주인
      LookupError를 사용해도 된다!
    단, 최상위인 BaseException과 같이 무슨 에러가 발생했는지 모를 정도로
      상위 범주의 에러를 사용해서는 안된다 '''
      

print(get(3, (1, 2, 3)))
print(get('age', {'name':'RnL'}))
print(end='\n\n')


# 3번) 예외에 속성 추가하기
print('<예시 3번>')
try:
  raise Exception('밥', '국')
except Exception as err:
  print(type(err))
  print(err.args)  # 속성은 args에 저장됨
  print(err, end='\n\n')  # __str__ 에 의해 args와 동일하게 출력되는 것

  
  err.side_dish = '김치'  # 속성을 이렇게 임의로 지정해서 저장할 수 있지만
  print('반찬 :', err.side_dish)
  print(err.args)  # 임의로 저장한 속성은 args에 저장되지 않는다
  print(err)       # args에는 처음 raise될 때의 속성만 저장된다!

  x, y = err.args
  print('x = {0}'.format(x))
  print('y = {0}'.format(y))
print(end='\n\n')


# 4번) 예외의 다른 옵션들 else, finally
# else : try가 성공했을 경우 작동하는 부분
# finally : try의 성공 여부와 관계없이 항상 작동하는 부분 (while문에서 주의!)
print('<예시 4번>')
print('4-1) try + except')

print()
print('4-2) try + except + else')

print()
print('4-3) try + finally')

print()
print('4-4) try + except + finally')

print()
print('4-5) try + except + else + finally')


print(end='\n\n')


# 5번) 사용자 정의 예외 만들기
print('<예시 5번>')


print(end='\n\n')