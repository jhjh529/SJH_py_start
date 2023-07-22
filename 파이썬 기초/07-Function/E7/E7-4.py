def km_to_mile(km):
    mile=km*0.621371
    print('%d km는 %.2f mile 이다.'%(km,mile))

a=int(input('km를 입력하세요 : '))
km_to_mile(a)