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

print(f"Car.p:{Car.p}") # 1234
print(f"a1.p:{a1.p}") # 1234
print(f"b.p:{b.p}") # 1234

"""
Car.p = "987" 이러면 static 영역에 있는 p의 값을 바꾸는 거라서, 전체 영향이 가요
그런데 그냥 instance.p=값   이러면 이건 static 영역의 값을 바꾸는게 아니라
맴버변수 하나 더 만드는게 되요
"""
b.p="987"
print("-----b.p='987'-----")
print(f"Car.p:{Car.p}") # 1234
print(f"a1.p:{a1.p}") # 1234
print(f"b.p:{b.p}") # 987