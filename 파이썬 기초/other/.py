a=[1,2,3,4,5,6,7,8,9,0]
for i in range(0,11):
    print(a)
    x = a.pop(i)
    print(a)
    a.insert(i,x)
    print(a)
    print('------------------------------------')