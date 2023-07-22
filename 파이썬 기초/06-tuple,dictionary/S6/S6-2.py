temp = {'월':15.5,'화':17.0,'수':16.2,'목':12.9,'금':11.0,'토':10.5,'일':13.3}

l=min(list(temp.values()))

for i in temp :
    
    if temp[i] == l :
        a=i
    
print('요일 : %s요일, 최저 기온 :%.1f℃ '%(a,l))
