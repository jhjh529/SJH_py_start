def B(s):
    a=s[::-1]
    for i in range(0,len(a)):
        print(a[i],end='')
        



s=tuple(str(input('문자열을 입력하세요. : ')))
B(s)
