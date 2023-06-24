#if ~ elif ~ else ~

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