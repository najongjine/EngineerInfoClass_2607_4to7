arr1=[1,2,3]
arr1.append(5) # [1,2,3,5]
arr1.append([9,8]) # [1,2,3,5,[9,8]]
arr1.extend([11,12]) # [1, 2, 3, 5, [9, 8], 11, 12]


arr1=[1,2]
arr2=[3,4]
arr3=arr1+arr2 # [1, 2, 3, 4]

arr1=[1,2,3]
arr1.insert(1,5) # [1, 5, 2, 3]

"""
      0     1     2     3     4
      -5   -4   -3    -2   -1
"""
arr1=[1  ,  2  ,  3  ,  4  ,  5  ]
arr1[0] # 1
arr1[3] # 4
arr1[-1] # 5


str1="Hello Python"
# 0~ 3 전까지. 0~2
str1[0:3] # Hel
# : 앞에 아무것도 없으면 0이랑 같음.
str1[:3] # Hel
# 0부터 끝까지
str1[:] # Hello Python
# 0 ~ -2 전까지. 즉 0 ~ -3
str1[:-2] # Hello Pyth


# 0 ~ 끝까지. 2칸씩
str1[::2] # HloPto


arr1=['h','e','l','l','o',' ','P','e']

"""
.index:= 왼쪽부터 오른쪽으로 검색하면서 'l' 이라는거 찾고,
그곳의 엔덱스 번호를 return
"""
idx_num=arr1.index('l') # 2

"""
python에서 pop()은 stack 개념이랑 비슷하면서도 룰을 어길수도 있어요
pop() 이렇게 하면 리스트에서 맨 마지막꺼 뿅 꺼내와요
pop(2) 이렇게하면 리스트에서 인덱스 2번째의 원소 뿅 꺼내와요
그리고 중요한건 pop()을 하고나면 진짜 원본 리스트에서도 원소가 제거되요
"""
# mye=arr1.pop() # e
mye=arr1.pop(2) # l
print(f"mye:",mye)
print(f"arr1:",arr1)

# remove:= 하나만 찾아서 제거. 왼쪽부터 오른쪽으로 검색해 감
arr1.remove('e') # ['h', 'l', 'l', 'o', ' ', 'P', 'e']
