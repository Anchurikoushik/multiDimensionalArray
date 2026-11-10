import numpy as np
my_str1=[1,2,3,4,5]
my_str2=[3,4,5,6,3]
my_str3=[4,5,4,6,5]

arr=np.array([my_str1,my_str2,my_str3])
print(arr)
print(type(arr))
arr.shape
print(arr.shape)
arr.reshape(5,3)
print(arr)
arr.shape
print(arr.shape)
