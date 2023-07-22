def func():
    global x        #전역변수 선언
    x = 200         #전역변수 o
    print(x)

x=100
print(x)            #전역변수 x
func()              
print(x)            #전역변수 o