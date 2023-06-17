
#if
'''
x=int(input('정수를 입력하세요 : '))

if x>0 :
  print('입력된 수는 양수 입니다.') 
  print('입력된 수는 양수 입니다.') 
'''
'''
s1=75
s2=90
print(s1>=80 and s2>=80)
s1=85
s2=95
print(s1>=80 and s2>=80)

x=10
print(x%2==0 or x%6==0)

x=16
print(x%3==0 or x%5==0)

x=25
print(not x%2 ==0)
print(not x>10)
'''

'''
age=int(input('나이는? : '))
t=2000

if age >= 65 :
  t=0

print('나이 : %d세 \n입장료 : %d원'%(age,t))
'''

'''
n=int(input('자연수를 입력하세요 : '))
r='3의 배수도 4의 배수도 아니다.'

if n%3==0 :
  r='3의 배수이다.'
if n%4==0 :
  r='4의 배수이다'
if n%3==0 and n%4==0 :
  r='3의 배수이면서 4의 배수이다.'
  
print('%d은(는) %s'%(n,r))
'''

#영어 퀴즈
'''
N1=input("Q1.'사자'의 영어 단어는 무엇일까요? : ")
r='땡! 틀렸습니다.'
if N1=='lion' :
  r='딩동댕! 정답입니다!!'
print(r)

N2=input("Q2.'오랜지'의 영어 단어는 무엇일까요? : ")
r='땡! 틀렸습니다.'
if N2=='orange' :
  r='딩동댕! 정답입니다!!'

print(r)

N3=input("Q3.'기차'의 영어 단어는 무엇일까요? : ")
r='땡! 틀렸습니다.'
if N3=='train' :
  r='딩동댕! 정답입니다!!'

print(r)
'''


#if ~ else ~
'''
x=int(input('자연수를 입력하세요. : '))

if x%2==0 :
  print('짝수!')

else :
  print('홀수!')
'''

'''
pilgi=int(input('필기시험 점수는? : '))
silgi=int(input('실기시험 점수는? : '))

if pilgi>=80 and silgi>=80:
  r='합격'
else :
  r='불합격'

print('-'*30)
print('-필기시험 점수 : %d\n-실기 시험 점수 : %d\n-합격/불합격 여부 : %s'%(pilgi,silgi,r))
'''

'''
a=input('영어 소문자 한가지를 입력하세요. : ')
if a=='a' or a=='e' or a=='i' or a=='o' or a=='u' :
  r='모음'
else :
  r='자음'
print('%s은(는) %s이다.'%(a,r))
'''

#if ~ elif ~ else ~
'''
#점수로 등급반영
s=int(input('점수는? : '))

if s>= 90 :
  g='A'
elif s>= 80 :
  g='B'
elif s>=70 :
  g='C'
elif s>=60 :
  g='D'
else :
  g='F'


print('등급 : ',g)
'''

'''
#간단 계산기
print('기능 선택')
print('1.더하기')
print('2.빼기')
print('3.곱하기')
print('4.나누기 \n')

s=int(input('계산기 기능을 선택하세요(1/2/3/4). : '))
n1=int(input('첫 번째 숫자를 입력하세요. : '))
n2=int(input('두 번째 숫자를 입력하세요. : '))

if s==1 :
  print('%d + %d = %d'%(n1,n2,n1+n2))
elif s==2 :
  print('%d + %d = %d'%(n1,n2,n1-n2))
elif s==3 :
  print('%d + %d = %d'%(n1,n2,n1*n2))
elif s==4 :
  print('%d + %d = %d'%(n1,n2,n1/n2))
else :
  print('입력 숫자가 잘못되었습니다!')
'''


'''
print('='*30)
n_y=int(input('현재년은? : '))
n_m=int(input('현재월은? : '))
n_d=int(input('현재일은? : '))
b_y=int(input('출생년은? : '))
b_m=int(input('출생월은? : '))
b_d=int(input('출생일은? : '))

if b_m < n_m :
  age=n_y-b_y
elif b_m==n_m :
  if b_d<n_d :
    age=n_y-b_y
  else :
    age=n_y-b_y-1
else :
  age=n_y-b_y-1

print('='*30)
print('오늘날짜 %d년 %d월 %d일'%(n_y,n_m,n_d))
print('생년월일 %d년 %d월 %d일'%(b_y,b_m,b_d))
print('-'*30)
print('만 나이 : %d세'%age)
print('='*30)
'''

