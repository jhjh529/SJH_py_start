#주민번호로 남여 판정

a=int(input('주민번호 뒷자리 첫번째 숫자를 입력해 주세요. : '))
if a==1 or a==3 :
  r='남성'

if a==2 or a==4 :
  r='여성'

print('%s입니다!'%r)