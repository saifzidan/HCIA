import numpy as np
from numpy import random
n1 = np.array(random.randint(1000 , size=500))
print(n1)
n1.sort()
print(n1)
avg = np.average(n1)
print(avg)
even = []
odd = []
for i in n1:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
print (len(even))
print (len(odd))
t1 = tuple(even)
print (t1)
s1 = set(odd)
print (s1)