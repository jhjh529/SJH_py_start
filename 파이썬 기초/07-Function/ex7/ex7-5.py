def even_odd(n):
    if n%2==0 :
        print('%d는 짝수 입니다.'%n)
    else :
        print('%d는 홀수 입니다.'%n)

x = int(input('양의 정수를 입력하세요 : '))
print()
even_odd(x)