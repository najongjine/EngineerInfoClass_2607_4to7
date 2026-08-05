"""
pop 을 쓰면 진짜 원소에서 제저가 되요.
"""
data = [10, 20, 30, 40, 50]
#print([data.pop() for _ in range(3)])
#print(data)


data = [1, 2, 3, 4, 5]

data2=[x + data.pop() for x in data]
#print(data2) # [6,6,6]


nums = [1, 2, 3, 4, 5, 6]
result = [nums.pop(0) for _ in range(len(nums)//2)]
#print(result) # [1, 2, 3]
#print(nums) # [4, 5, 6]

a=1
if(a>0):
    print("a는 0보다 커요 ")
    a=2
elif a==0:
    print("a는 0이랑 같아요")
else:
    print("a는 0보다 작아요")

a="money23ㅈ2"
b="I like money. money money 해"
if a in b:
    print(f"b 에 a 있어")
    if 1:
        pass
else:
    print(f"b 에 a 없어")

a=[1,2,3]
for x in a:
    #print(x)
    pass

for i in range(3):
    #passprint("0~2까지. 3에서 빠져나옴")
    pass
print(f"i란거 아직도 살아있음 {i}")

for i in range(1,5):
    #print(f"i~4 까지")
    pass

for i in range(1,5,2):
    #print(f"2칸씩. {i}")
    pass

for a in range(2,10):
    for b in range(2,10):
        #print(f"{a}*{b}={a*b}")
        pass


a=1
"""
python에서 함수, class 는 scope 개념이 존재 해요
나머지는 scope 개념 없어요
"""
def myf():
    # myf scope 안에 a를 따로 만든것
    a=9
    pass

"""
python 함수는 overloading override 없애버리고
매개변수에 기본값을 정해줄수 있어요
"""
def myf2(a=0,b=1,c=0,d=0,e=0,f="gg"):
    a=10
    b=11
    pass

myf();
# 이러면 모든 매개변수 다 전달하지 않고, 필요한것만 전달하면 되요
myf2(f=1);
print(f"a:{a}")

"""
a 에 데이터 전달해주면 전달해준걸로 사용
a에 데이터 잔달된게 없으면 {"k1":1} 으로 사용
"""
def change1(a={"k1":1}):
    del a["k2"]

aa={"k2":2,"k3":3}
# java, python은 숫자, 문자열, 문자, boolean 빼고는 다 stamp 결합도
# 원본에 손상이 감
change1(aa)
print(f"aa:{aa}")

