import random as rd
no = rd.randint(1 , 10000)
no0 = rd.randint(0 , no)
no1 = no - no0
pno0 = no0/no
pno1 = no1/no
print(no)
print(pno0*100)
print(pno1*100)