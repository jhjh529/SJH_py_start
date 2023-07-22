eng_diict = {'house':'집','piano':'피아노','christmas':'크리스마스','frend':'친구','bread':'빵'}

def T_or_F(a,b):
    if b==eng_diict[a] :
        p='참 잘했어요!'
    else :
        p='틀렸어요!'
    return p

for i in eng_diict:
    b=input('\'%s\'에 맞는 영어 단어는? : '%eng_diict[i])
    print(T_or_F(i,b))