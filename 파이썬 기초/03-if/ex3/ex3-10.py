print('='*30)
n_y=int(input('현재년은? : '))
n_m=int(input('현재월은? : '))
n_d=int(input('현재일은? : '))
b_y=int(input('출생년은? : '))
b_m=int(input('출생월은? : '))
b_d=int(input('출생일은? : '))

if b_m < n_m :
  age=n_y-b_y
elif b_m==n_m :
  if b_d<n_d :
    age=n_y-b_y
  else :
    age=n_y-b_y-1
else :
  age=n_y-b_y-1

print('='*30)
print('오늘날짜 %d년 %d월 %d일'%(n_y,n_m,n_d))
print('생년월일 %d년 %d월 %d일'%(b_y,b_m,b_d))
print('-'*30)
print('만 나이 : %d세'%age)
print('='*30)