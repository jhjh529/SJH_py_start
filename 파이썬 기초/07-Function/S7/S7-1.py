a = 2


def a(b):
    a = 2
    while a <= b+1:
        
        flag = True

        for j in range(2, a):
            if a % j == 0:
                flag = False
                break
        
        if (flag):
            print(a,end=' ')

        a +=1
        
c = int(input('끝 수를 입력해주세요. : '))
a(c)