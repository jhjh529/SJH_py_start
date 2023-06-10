###############1
'''
y=input('년은? :')
m=input('월은? :')
d=input('일은? :')
print(y,m,d,sep='.')
print('-'*20)
'''
##############2
'''
width=int(input('사각형의 가로길이는? :'))
height=int(input('사각형의 세로길이는? :'))
lenght=2*width+2*height
area=width*height
print('-'*15+'계산결과'+'-'*15)
print('사각형의 가로길이:%dcm'%width)
print('사각형의 세로길이:%dcm'%height)
print('사각형의 둘레:%dcm'%lenght)
print('사각형의 넓이:%dcm'%area)
'''
#############3
'''
r=float(input('반지름을 입력하세요 :'))
r_lenght=2*r*3.14
r_area=r**2*3.14

print('-'*15+'계산결과'+'-'*15)
print('원의 반지름:%.2fcm'%r)
print('원의 둘레:%.2fcm'%r_lenght)
print('원의 넓이:%.2fcm²'%r_area)
'''
############4
'''
inch=float(input('인치는?'))
cm=inch*2.54
print('%.1f inch => %.1f cm'%(inch,cm))
'''
############5
'''
book=int(input('책의 가격은? :'))
seal=int(input('할인률은? :'))
delivery=int(input('배송료는? :'))

totla=book-(book*(seal/100))+delivery

print('-'*15+'계산결과'+'-'*15)
print('책 값:%d원'%book)
print('할인률:%d'%seal+'%')
print('배송료:%d원'%delivery)
print('결제금액:%d원'%totla)
'''