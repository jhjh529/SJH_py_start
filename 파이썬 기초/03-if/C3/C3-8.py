#만족도로 팁계산

print('서비스 만족도:')
print('1.매우만족')
print('2.만족')
print('3.불만족')
a=int(input("서비스 만족도는(1/2/3)? : "))
p=int(input('음식값은? : '))
if a==1 :
  tip=int(p*0.2)
  s='매우만족'
elif a==2 :
  tip=int(p*0.1)
  s='만족'
else : 
  tip=0
  s='불만족'
print()
print("서비스 만족도: %s, 팁:%d원"%(s,tip))