def sum_int(start,end):
    total=0
    for i in range(start,end+1):
        total += i
    print("%d부터 %d까지의 정수의 합계 : %d "%(start,end,total))

sum_int(20,50)
sum_int(600,800)