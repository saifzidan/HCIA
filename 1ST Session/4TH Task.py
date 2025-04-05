list1 = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
list_Odd = []
list_Even = []
y = 0
z = 0
for i in list1:
    x = i % 2
    if x == 0:
        list_Even.append(i)
        z = z + 1
    else:
        list_Odd.append(i)
        y = y + 1
print (list_Odd)
print (list_Even)
print (z)
print (y)
