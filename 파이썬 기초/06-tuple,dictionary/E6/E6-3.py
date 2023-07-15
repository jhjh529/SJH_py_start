year_sale = {'2016':237,'2017':98,'2018':158,'2019':233,'2020':120}
a=0
for key in year_sale :
    print('%s년 자동차 판매량 : %d대'%(key,year_sale[key]))
    a += year_sale[key]

avg = a/len(year_sale)

print('5년간 총 판매량 : %d'%a)
print('5년간 연 평균 판매량 : %d'%avg)