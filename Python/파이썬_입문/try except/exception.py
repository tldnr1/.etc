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
# try (해당 구문 안에서 에러 발생 시 처리 가능 - 필수)
# except (에러 발생시 수행 - 선택이지만 에러를 처리하려면 필수)
# else (에러 없을 때 수행 - 선택이지만 except 없이는 올 수 없음)
# finally (에러가 있거나 없거나 상관없이 항상 수행 - 선택)
# 출처: https://blockdmask.tistory.com/537 [개발자 지망생]
print('<예시 4번>')
print('4-1) try + except')
print('== Program_1 Start')
try:
  arr = ['b', 'l', 'o', 'g']
  print(arr[8]) # error
  print("== Mid")
except:
  print("== error!! but, still alive")

print("== Program_1 End", end='\n\n')


print('4-2) try + except + else')
print('== Program_2 Start')
try:
  arr = ['b', 'l', 'o', 'g']
  print(arr[0])
  #print(arr[8])  # 에러가 발생한다면 else는 작동하지 않음!
  print("== Mid")
except:
  print("== error!! but, still alive")
else:
    print("== else")

print("== Program_2 End", end='\n\n')


print('4-3) try + finally')
print('== Program_3 Start')
try:
  arr = ['b', 'l', 'o', 'g']
  print(arr[8]) # error
  print("== Mid")
except:
  print("== error!! but, still alive")
finally:
  print("== finally")  # finally는 에러가 발생해도 무조건 실행됨

print("== Program_3 End", end='\n\n')


# print('4-4) try + except + finally')  => 5와 비슷해서 생략함
print('4-5) try + except + else + finally')
print("== Program_5 Start")
try:
  arr = ['b', 'l', 'o', 'g']
  print(arr[0])
  #print(arr[8])
  print("== Mid")
except:
  print("== except")
else:
  print("== else")
finally:
  print("== finally")

print("== Program_5 End", end='\n\n\n')


# 5번) 예외 객체 살펴보기
print('<예시 5번>')
try:
  1/0
except Exception as e:  # 예외 객체를 변수 e에 대입
  exception = e  # 예외 객체를 전역변수 exception에 대입

print(type(exception))  # 예외 객체의 유형 확인
print(isinstance(exception, ZeroDivisionError))
print(isinstance(exception, BaseException))

print(str(exception))  # 문자열로 변환하면 오류의 발생원인을 나타내는 문자열이 된다!

print(end='\n\n')