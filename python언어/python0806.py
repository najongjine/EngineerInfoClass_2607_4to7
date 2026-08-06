class Car:
    """
    클래스 변수(자바의 static 변수와 비슷)
    """
    p="123"
    # 생성자. self 매개변수 아님
    def __init__(self):
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


print(a1.p)
b.p # "123"
a1.p # "123"
Car.p # "123"