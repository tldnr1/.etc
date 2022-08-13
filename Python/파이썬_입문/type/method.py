''' 클래스에 사용되는 특수한 메소드! '''
# __init__ (초기화 함수)   : 인스턴스를 만들 때 실행되는 함수(보통, 초기 정보 설정으로 사용)
# __str__  (문자열화 함수) : 인스턴스 자체를 출력할 때의 형식을 지정해주는 함수

class Human():
    
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    def __str__(self):
        return "{} (몸무게 {}kg)".format(self.name, self.weight)
    
    def eat(self):
        self.weight += 0.1
        print("{}가 먹어서 {}kg이 되었습니다.".format(self.name, self.weight))
    
    def walk(self):
        self.weight -= 0.1
        print("{}가 걸어서 {}kg이 되었습니다.".format(self.name, self.weight))

# 아래에서 person을 이름과 몸무게를 가지는 Human클래스의 인스턴스로 만들어보세요.
person = Human('사람', 60.5)
person.walk()
person.walk()
person.eat()
print(person)