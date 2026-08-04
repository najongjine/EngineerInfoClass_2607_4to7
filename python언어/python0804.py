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


m = [1, 2, 3, 4]
b = m[:]
b[0]=b[0]*2
b[2]=b[2]*2

c=m[0]+b[0]+m[1]+b[1]
#print(c)


a = [ x+1 for x in range(10) if x<5 ]
 


