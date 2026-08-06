class Car:
    """
    클래스 변수(자바의 static 변수와 비슷)
    """
    p="123"
    # 생성자. self 매개변수 아님
    def __init__(self):
        self.__d=1
        self.a=1 # 필드
        self.name="pepe" # 필드
        Car.p="1234" # 클래스 변수 말하는거
        p="1" # 함수에 종속된 함수변수. 필드도 아니고 클래스 변수도 아님
        pass
    """
    파이썬 클래스의 method는 무조건 self라는거 넣어줘야함
    self 이거 매개변수 아님
    """
    def drive(self,n1=0):
        print("운전")
    pass

a1=Car()
b=Car()
#a1.drive()
#print(f"Car.p:{Car.p}") # 1234
#print(f"a1.p:{a1.p}") # 1234
#print(f"b.p:{b.p}") # 1234

"""
Car.p = "987" 이러면 static 영역에 있는 p의 값을 바꾸는 거라서, 전체 영향이 가요
그런데 그냥 instance.p=값   이러면 이건 static 영역의 값을 바꾸는게 아니라
맴버변수 하나 더 만드는게 되요
"""
b.p="987"
#print("-----b.p='987'-----")
#print(f"Car.p:{Car.p}") # 1234
#print(f"a1.p:{a1.p}") # 1234
#print(f"b.p:{b.p}") # 987


class A:
    def __init__(self,a=1,b=2):
        self.a=a
        self.b=b
    def show(self):
        print(f"a:{self.a},b:{self.b}")
    def hello(self):
        print("hello")
"""
파이썬 상속  () 안에 상속할 부모 클래스 이름 적어줌
자바의 상속보다 간단하지만, 자바처럼 부모의 필드를 전부 가져오지 못함
예를들어서 show method의 경우, B 에서도 있다고는 표시 되지만,
B 클래스에서 a,b 필드를 정의해주지 않아서 b.show() 하면
a,b 필드가 없다고 에러남
"""
class B(A):
    def __init__(self,c=3):
        self.c=c

a=A()
b=B()
b.hello()