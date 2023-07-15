a = [7,9,15,18,30,-3,7,12,-16,-12]
b=0
c=[]
i=1
while i < len(a) :
   
    x = a[i]
    c.append(x)
    b += x
    
    
    i += 2

print('짝수번째 요소===>  ',end='')
print(c)
print('합====>  ',end='')
print(b)