# 클래스 생성 설명 : https://nirsa.tistory.com/110
# self에 대한 설명 : https://wikidocs.net/1742

class Human():
  '''사람'''

# 클래스에 속성 추가
person1 = Human()
person1.name = '한국인'
person1.language = '한국어'

def speak(person):
  print('{}이(가) {}로 이야기합니다'.format(person.name, person.language))

# 클래스에 메소드 추가
Human.speak = speak

speak(person1)
person1.speak()

'''위와 다르게 info, 클래스 내에 메소드 생성 등을 활용하면 아래와 같음'''
# 이렇게 현실의 개념을 코드에 나타내기 위해 정돈하는 것을 '모델링(modeling)' 이라고 함
class Human2:
  # 속성 생성
  def __init__(self, name, language):
    self.name = name
    self.language = language

  # 메소드 생성
  def speak(self):
    print('{0}이(가) {1}로 이야기합니다'.format(self.name, self.language))

'''
    self는 파이썬에서 자동으로 넘겨주는 1번 인자임
    즉, self를 안적어주면 안돌아감!
'''

person2 = Human2('미국인', 'English')
person2.speak()