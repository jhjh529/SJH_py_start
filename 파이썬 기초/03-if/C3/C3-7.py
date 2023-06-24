#할인률에 따른 지불금액 계산

b_p=int(input('구매금액은? : '))



if b_p<10000 :
  sale=0
elif b_p<50000 :
  sale=5
elif b_p<300000 :
  sale=7.5
elif b_p>=300000 :
  sale=10
sale_p=b_p*sale/100
pay=b_p-sale_p
print('구매금액 : %d원'%b_p)
print("할인률 : %.1f%%"%sale)
print("할인금액 : %d원"%sale_p)
print("지불금액 : %d원"%pay)