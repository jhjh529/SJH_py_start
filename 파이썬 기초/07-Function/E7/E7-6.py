def  count(S,F):
    count=0
    for i in S:
        if i == F:
            count += 1
    print('\'%s\' 에 포함된 \'%s\' 의 개수는 %d 개 입니다.'%(S,F,count))

S=str(input('문장을 입력하세요. : '))
C_s=str(input('개수를 셀 한 글자를 입력하세요. : '))

count(S,C_s)
