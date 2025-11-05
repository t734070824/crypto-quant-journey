import  numpy  as np

a = np.arange(15)
print(a)


a = a.reshape(3,5)
print(a)


print(a.shape)

print(a.ndim)

print(a.dtype.name)

print(a.itemsize)

print(a.size)

print(type(a))

b = np.array([6,7,8])
print(b)

print(type(b))


print(a.dtype)
print(b.dtype)



a = np.array([2,3,4])
print(a.dtype)

c = np.array([[1, 2], [3, 4]], dtype=complex)
print(c)

'''[[1.+0.j 2.+0.j]
 [3.+0.j 4.+0.j]]'''


print(np.zeros((3,4)))

print(np.ones((2,3,4), dtype=np.int16))

print(np.empty((2,3)))
'''[[1.39069238e-309 1.39069238e-309 1.39069238e-309]
 [1.39069238e-309 1.39069238e-309 1.39069238e-309]]'''



print(np.arange(10,30,5))


print(np.arange(0,2,0.3))


A = np.array([[1,2], [0,1]])
B = np.array([[2, 0], [3,4]])

print(A * B)  # 元素乘

print(A @ B)  # 矩阵乘
print(A.dot(B))  # 矩阵乘



a  = np.ones((2,3), dtype=int)
print(a)
b= np.linspace(0, np.pi, 3)
print(b)

b = np.arange(12).reshape(3,4)
print(b)
print(b.sum(axis=0))  # 列求和

























