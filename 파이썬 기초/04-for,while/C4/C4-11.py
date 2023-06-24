s = input('문장을 입력해 주세요. : ')

i =len(s)-1

while i >= 0 :
  if s[i]==" " :
    print('-',end='')
  else :
    print('%s'%s[i],end="")

  i -= 1