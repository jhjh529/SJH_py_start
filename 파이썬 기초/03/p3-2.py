#월로 계절 판별

m=int(input('월을 숫자로 입력하세요. : '))
if m>=3 and m<=5 :
  r='봄'
if m>=6 and m<=8 :
  r='여름'
if m>=9 and m<=11 :
  r='가을'
if m==12 or m<=2 :
  r='겨울'
print('%d월은 %s입니다.'%(m,r))