"""
arr1 의 주소를 arr2에 주는게 아니라
arr1이 가진 데이터들 자체를 arr2에 복붙해서 넘겨주고 싶다
"""
arr1=[1,2,3]
# 이건 안됨. 주소가 복사됨. stamp 결합도
arr2=arr1



arr2=arr1[:]
arr2[0]=9


"""
사소한 팁:
파이썬에선 class instance 빼고는 print 했을때 주소 안나와요
하지만 class instance는 주소값으로 찍혀요
"""
#print(arr1)

# set 자료형은 중복을 자동으로 제거함
set1=set([1,2,2,2,2,3])
set1={1,2,2,2,2,2,3}

set1.add(2)
set1.remove(1)
set1.update({4,5,6})

print(f"set1:{set1}")

# 튜플은 시험에 잘 안나옴.
# 수정 불가능
tp1=(1,2,3)
tp1=(4,45,3)

# dictionary. key:value 형태로 감
di1={"k1":1,"k2":2}
# 키가 없으면 새로 추가, 있으면 값 갱신
di1["k3"]=3
di1.update({"k3": 2})
del di1["k3"]
# dictionary의 key만 뽑아서 list로 만드는것
print(di1.keys()) # ['k1', 'k2']
# value만 뽑아서 list로 만드는것
print(di1.values()) # [1, 2]



keys = ["name", "age", "job"]
"""
{
    "name": None,
    "age": None,
    "job": None
}
"""
person = dict.fromkeys(keys)



m = [1, 2, 3, 4]
b = m[:]
b[0]=b[0]*2
b[2]=b[2]*2

c=m[0]+b[0]+m[1]+b[1]
#print(c)

"""
1. x in 어쩌구
2. if문같은 조건체크
3. 데이터 연산 or 선택
"""
a = [ x+1 for x in range(10) if x<5 ]
# [1,2,3,4,5]
 
a= [ 1, 2 ,3 ]
m = [[x] for x in a] # [[1],[2],[3]]



results = ["짝수" if x % 2 == 0 else "홀수" for x in range(5)]
