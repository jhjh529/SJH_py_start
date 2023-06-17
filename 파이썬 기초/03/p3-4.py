#영어 대,소문자 자음/모음판별

a=input('영어 알파벳 한가지를 입력하세요. : ')
b=a.upper()

if b=='A' or b=='E' or b=='I' or b=='O' or b=='U' :
   r='모음'
else :
  print('%s ==> %s'%(a,r))