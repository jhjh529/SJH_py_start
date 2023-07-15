numbers = [7,9,15,18,30,-3,7,12,-16,-12]
a=0
i=0
while i <len(numbers) :
    
    x = numbers.pop(0)
    
    a += x

print('====>  ',end='')
print(a)