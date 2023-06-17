##if

#특정 범위 수 인지 판정
'''
startN=int(input('시작 수는? : '))
endN=int(input('끝 수는? : '))
N=int(input('정수를 입력하세요. : '))
r='사이에 없다.'

if startN<= N and endN>= N :
  r='사이에 있다.'

print('%d은(는) %d ~ %d %s'%(N,startN,endN,r))
'''

#월로 계절 판별
'''
m=int(input('월을 숫자로 입력하세요. : '))
if m>=3 and m<=5 :
  r='봄'
if m>=6 and m<=8 :
  r='여름'
if m>=9 and m<=11 :
  r='가을'
if m==12 or m<=2 :
  r='겨울'
print('%d월은 %s입니다.'%(m,r))
'''

#주민번호로 남여 판정
'''
a=int(input('주민번호 뒷자리 첫번째 숫자를 입력해 주세요. : '))
if a==1 or a==3 :
  r='남성'

if a==2 or a==4 :
  r='여성'

print('%s입니다!'%r)
'''

##if ~ else ~   

#영어 대,소문자 자음/모음판별
'''
a=input('영어 알파벳 한가지를 입력하세요. : ')
b=a.upper()

if b=='A' or b=='E' or b=='I' or b=='O' or b=='U' :
   r='모음'
else :
  print('%s ==> %s'%(a,r))
'''

#다이어트 필요성 판정(키-100*0.9<몸무게 => 필요)
'''
t=int(input('키는? : '))
k=int(input('몸무게는? : '))

a=(t-100)*0.9

if a<k :
  print('건강을 위해 다이어트가 필요합니다!')
else :
  print('표준체형 또는 마른 체형입니다.')
'''

#아르바이트 급여 계산
'''
print('아르바이트 급여 계산 프로그램 ')
print('◆  시급')
print('- 주간 근무 : 9500원')
print('- 야간 근무 : 주간시급 × 1.5')

D=9500
N=9500*1.5

a=int(input('1(=주간근무) 또는 2(=야간근무)를 입력해주세요. : '))
t=int(input('근무시간을 입력해주세요. : '))

if a==1 :
  r=9500*t
  D_N='주간'

if a==2 :
  r=N*t
  D_N='야간'
print('%d시간동안 일한 %s근무 급여는 %d원 입니다.'%(t,D_N,r))
'''

#할인률에 따른 지불금액 계산
'''
b_p=int(input('구매금액은? : '))



if b_p<10000 :
  sale=0
elif b_p<50000 :
  sale=5
elif b_p<300000 :
  sale=7.5
elif b_p>=300000 :
  sale=10
sale_p=b_p*sale/100
pay=b_p-sale_p
print('구매금액 : %d원'%b_p)
print("할인률 : %.1f%%"%sale)
print("할인금액 : %d원"%sale_p)
print("지불금액 : %d원"%pay)
'''

#만족도로 팁계산
'''
print('서비스 만족도:')
print('1.매우만족')
print('2.만족')
print('3.불만족')
a=int(input("서비스 만족도는(1/2/3)? : "))
p=int(input('음식값은? : '))
if a==1 :
  tip=int(p*0.2)
  s='매우만족'
elif a==2 :
  tip=int(p*0.1)
  s='만족'
else : 
  tip=0
  s='불만족'
print()
print("서비스 만족도: %s, 팁:%d원"%(s,tip))
'''


#세 정수중 가장큰 수

n1=int(input('첫 번째 정수는? : '))
n2=int(input('두 번째 정수는? : '))
n3=int(input('세 번째 정수는? : '))

if n1>=n2 and n1>=n3 :
  big=int(n1)
elif n2>=n1 and n2>=n3 :
  big=int(n2)
else :
  big=int(n3)

print('%d, %d, %d 중에서 가장 큰 수는 %d 입니다.'%(n1,n2,n3,big))


