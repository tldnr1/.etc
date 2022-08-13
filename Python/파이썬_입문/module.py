# import datetime : 날짜 관련 기능
import datetime
now = datetime.datetime.now()
print('현재 연도 :', now.year)
print('현재 날짜 :', datetime.date.today())
print()

# import math : 수학 관련 기능
# import random : 랜덤 관련 기능
import random
list = ['a', 'b', 'c', 'd', 'e']
random_int = random.randint(0,10)
random.shuffle(list)
print('randint :', random_int)
print('shuffle list :', list)


# import urllib.request : 인터넷의 내용을 가져오는 기능
# request : 가져오기 / post : 보내기

"""
# module 만들기
1. 사용할 함수, 메소드 코드를 작성한 모듈 파일을 생성
2. 모듈이 쓰일 파일에 import를 사용하여 모듈을 호출
3. 사용 방법은 기존의 모듈과 동일
4. 주의할 점은 사용자가 만든 모듈과 모듈을 쓸 파일이 같은 폴더에 있어야 한다.

* 공식문서
    필요한 내용을 둘러보고 싶을때
    파이썬 내장 모듈과 함수의 정보가 필요할 때
* 구글 또는 stackoverflow.com
    문제의 구체적인 해결 방법이 알고 싶을 때
    구글 검색시 사이트 제한 기능 활용 site:stackoverflow.com

"""