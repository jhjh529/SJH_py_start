c = 0

for i in range(1,101):
  if i%5 == 0 :
    if c%5==0:
      print()
    print(i,end=' ')
    c += 1