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