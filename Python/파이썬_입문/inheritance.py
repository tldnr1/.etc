'''
상속하는 클래스를 부모 클래스
상속받는 클래스를 자식 클래스
'''

# 상속(Inheritance) : 자식 클래스가 부모 클래스의 내용을 가져다 쓸 수 있는 것
# 오버라이드(Override) : 같은 이름을 가진 메소드를 덮어 쓴다는 의미
# super() : 자식클래스에서 부모클래스의 내용을 사용하고 싶은 경우
#             ㄴ super().부모클래스내용  의 형태로 사용함

# super 자세히 공부 : https://leemoney93.tistory.com/37
'''
# super
 : super() alone returns a "temporary object of the superclass" that then allows you to call that superclass's methods.

# super() vs super(클래스 이름,self)
  : 첫번째 매개변수의 클래스 이름에 따라 super가 탐색하는 범위가 달라짐!
  * 사실 super는 두 개의 파라미터를 받음
    : 1. 하위클래스의 이름
      2. 하위클래스의 object

  >> 즉, super(a, self)는 a '바로 위'의 부모클래스를 호출하는 것임
'''

class GrandParent:
  print('def 밖에 적으면 그냥 실행됩니다!')
  def __init__(self, name, age):
    print("GrandParent의 __init__ 호출")
    self.name = name
    self.age = age
    
  def get_name(self):
    print('from GrandParent 이름 : {}'.format(self.name))

  def get_age(self):
    print('from GrandParent 나이 : {}'.format(self.age))

  def get_info(self):
    self.get_name()
    self.get_age()

class Parent(GrandParent):
  def __init__(self, name, age, hobby):
    print("Parent의 __init__ 호출")
    super().__init__(name, age) # grandParent의 object를 생성했기에 get_name(), get_age()도 사용 가능!
    self.hobby = hobby

  def get_info(self):
    print('from Parent 이름 : {}, 나이 : {}, 취미 : {}'.format(self.name, self.age, self.hobby))
    
  def get_hobby(self):
    print('from Parent 취미 : {}'.format(self.hobby))

class Child(Parent):
  def __init__(self, name, age, hobby, work):
    print("Child의 __init__ 호출")
    super(Parent, self).__init__(name, age)
    self.hobby = hobby
    self.work = work

  def get_work(self):
    print('from Child 일 : {}'.format(self.work))

  # 아래의 info 들과 같이
  # 현재 클래스에 있는 함수를 우선적으로 사용됨
  # 상위 클래스의 함수를 쓰고 싶다면 super(), super(원하는 클래스의 하위클래스, self) 에다가
  # .함수이름() 을 붙여서 사용해야함
  # e.g. 1. super().get_info()
  # e.g. 2. super(Parent,self).get_info()
    
  def get_info(self):
    print('from Child 이름 : {}, 나이 : {}, 취미 : {}, 일 : {}'.format(self.name, self.age, self.hobby, self.work))

  def get_parent_info(self):
    super().get_info()

  def get_grandParent_info(self):
    super(Parent,self).get_info()
    

A = GrandParent('할아버지', 75)
A.get_info()
print()

B = Parent('아버지', 52, '골프')
B.get_info()
B.get_hobby()
print()

C = Child('아들', 22, '게임', '대학생')
C.get_info()
C.get_parent_info()
C.get_grandParent_info()
C.get_name()
C.get_hobby()
C.get_work()