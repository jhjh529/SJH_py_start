year_sale = {'2016':237,'2017':98,'2018':158,'2019':233,'2020':120}
a=0
for key in year_sale :
    if key=='2018' or key == '2019':
        print('%s년 자동차 판매량 : %d대'%(key,year_sale[key]))
        a += year_sale[key]

print('2년간 자동차 판매량 : %d'%a)