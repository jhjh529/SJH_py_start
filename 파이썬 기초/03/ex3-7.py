a=input('영어 소문자 한가지를 입력하세요. : ')
if a=='a' or a=='e' or a=='i' or a=='o' or a=='u' :
  r='모음'
else :
  r='자음'
print('%s은(는) %s이다.'%(a,r))