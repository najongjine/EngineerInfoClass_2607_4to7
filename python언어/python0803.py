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
# remove:= 하나만 찾아서 제거. 왼쪽부터 오른쪽으로 검색해 감
arr1.remove('e') # ['h', 'l', 'l', 'o', ' ', 'P', 'e']
print(arr1)
