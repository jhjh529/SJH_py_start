x=2
y=0
z=0
z1=0
a=[]
m=0
c=0
n=0
B=0
'''
while y<=0  :
  y=20080529%x
  print(20080529/x)
  x=x+1
  if y==0 :
    break
'''
'''
for i in range(2,99999999999999999,1) :
  y=20080529%x
  print('값=',20080529/x,'x=',x)

  if y==0 :
    print('='*50)
    print('값=',20080529/x,'x=',x)  
    print('='*50)
    z1=z+1
    if z==3 :
      c='값=',20080529/x,'x=',x
      print('='*50)
      print('='*50)
      print('='*50)
      print('='*50)
      print('='*50)
      print('='*50)
      print('='*50)
      print('='*50)
      n=len(a)
      print(a[0:n])
      break
   
    elif z!=z1 :
      a.append('값=',20080529/x,'x=',x)
    
  z=z1
  x=x+1
  '''

print('\n'*10)
print('"자신의 생년월일 = 𝒳 X 𝒴 "을(를) 찾아드립니다')
B=int(input('생년월일을 입력하세요\n(yyyymmdd,2023년 이전만 가능).\n: '))
if B>20230000 or B<10000000 :
  print('옳지않은 생년월일 입니다. 다시 입력하세요.')
  
else :
  for i in range(2,99999999999999999,1) :
    y=B%x
    e=B/x

    if y==0 :
      print('='*50)
      print('#----# ==> 값=',e,'x=',x)  
      print('='*50)
      m=m+1
      print('개수 : ',m)
    if e==1 :
      print('\n\n\n!!!=============끝!=============!!!\n\n\n')
      c=m/2
      n=int('%.0f'%c)
      print('\n'*3+'*정보( 총 개수:',m,'실제 개수:',n+m%2-1,' )')
      break
      

    x=x+1