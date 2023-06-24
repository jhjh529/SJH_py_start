name='송지호'
print(name)
a=10
b=20
print(a,b,a-b,100)

#sep를 이용해 출력
year=2021
month=11
day=15
print(year,month,day,sep='/')

hp1='010'
hp2='1234'
hp3='5678'
print(hp1,hp2,hp3,sep='-')

price=1000
print(price,'원',sep="")

#문자열 포멧코드로 출력
x=25
y=3.3
animal='호랑이'
print('%d %f %s'%(x,y,animal))
print('%.1f'%y)

#이스케이프코드 출력
print('가나다라(\'),(\\),(/n)마바사')
'''
\n :줄바꿈
\t :탭
\\ :역슬래시(\) 출력
\' :단 따옴표(') 출력
\" :쌍 따옴표(") 출력
'''
print('안녕하세요.\n반갑습니다.')
print('안녕하세요.\t반갑습니다.')
print('\'')
print('\"')