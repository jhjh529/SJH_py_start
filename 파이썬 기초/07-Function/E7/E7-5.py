def P(x,y):         # +
    a=x+y
    return a

def S(x,y):         # -
    a=x-y
    return a

def M(x,y):         # *
    a=x*y
    return a

def D(x,y):         # /
    a=x/y
    return a

print('-선택옵션\
      \n 1. 더하기\
      \n 2. 빼기\
      \n 3. 곱하기\
      \n 4. 나누기')

option =int(input('원하는 연산을 입력하세요.(1/2/3/4) : '))
ask1 = float(input('첫 번째 숫자를 입력하세요 : '))
ask2 = float(input('두 번째 숫자를 입력하세요 : '))

if option == 1:
    print('%.2f'%P(ask1,ask2))
if option == 2:
    print('%.2f'%S(ask1,ask2))
if option == 3:
    print('%.2f'%M(ask1,ask2))
if option == 4:
    print('%.2f'%D(ask1,ask2))
