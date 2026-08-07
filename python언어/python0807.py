


class A:
    def __init__(self,a=1,b=2):
        print(f"A생성자")
        self.a=a
        self.b=b
    def show(self):
        print(f"a:{self.a},b:{self.b}")
    def hello(self):
        print("hello")
"""
파이썬 클래스는 java처럼 생성자에 super가 자동으로 호출되지 않아요
수동으로 호출해줘야 해요
super.init 호출 안하면, 부모에 있는 필드들 못가져와요
super.init 호출하면 부모에 있는 필드 다 가져와요
"""
class B(A):
    def __init__(self,c=3):
        super().__init__()
        print(f"B생성자")
        self.c=c
        self.a=5


b=B()
b.show()