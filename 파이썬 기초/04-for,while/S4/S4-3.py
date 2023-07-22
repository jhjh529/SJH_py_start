a = int(input('시작 수를 입력해주세요. : '))
b = int(input('끝 수를 입력해주세요. : '))

while a <= b+1:
  flag = True

  for j in range(2, a):
    if a % j == 0:
      flag = False
      break
  
  if (flag):
    print(a,end=' ')

  a +=1