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


