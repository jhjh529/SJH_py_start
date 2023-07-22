def averagr(*args):
    num_arge=len(args)
    sum=0
    for i in range(num_arge):
        sum+=args[i]


    avg=sum/num_arge
    print('%d개의 과목평균 점수 : %.1f점'%(num_arge,avg))


averagr(100,100,90,70,70,80)
averagr(100,60,80,90)