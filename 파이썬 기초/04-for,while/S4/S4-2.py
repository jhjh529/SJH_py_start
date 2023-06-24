g='y'

while g=='y' or g=='Y' :
  a=int(input('성적을 입력하세요. : '))
  if a>=90 :
    print('등급 : 수')
  elif  a>=80 :
    print('등급 : 우')
  elif  a>=70 :
    print('등급 : 미')
  elif  a>=60 :
    print('등급 : 양')
  elif  a<60 :
    print('등급 : 가')

  g=input('계속하시겠습니까?(중단:q,계속:y)')