a = int(input('시작 수를 입력해주세요. : '))
b = int(input('끝 수를 입력해주세요. : '))

for i in range(a, b):
  flag = True

  for j in range(2, i//2):
    if i % j == 0:
      flag = False
      break
  
  if flag:
    print(i,end=' ')