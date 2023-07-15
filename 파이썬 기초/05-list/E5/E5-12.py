d = [[10,20,30],[40,50],[60,70,80,90]]

for i in range(len(d)):
    for j in range(len(d[i])):
        if j == 0 :
            print(d[i][j],end=' ')
    print()