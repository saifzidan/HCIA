import numpy as np
n1 = np.array([1 , 2 , 3 , 4])
n2 = np.array([1 , 3 , 2 , 5])
n3 = np.array([7 , 1 , 2 , 3])
r = np.array([np.multiply(np.sum([n1 , n2]) , n3)])
print(r)
print(r.ndim)
print(r.shape)
print(r.size)
print(r.reshape(4,1))
r1 = r[r<=40]
print(r1)