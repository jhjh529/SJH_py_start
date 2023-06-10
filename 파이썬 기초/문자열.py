
#문자열 추출
s="안녕하세요. 반갑습니다."
print(s[0])
print(s[1])
print(s[3:10])

#문자열 연결 연산자
name="송지호"
hello="안녕하세요!"
print(name +"님"+ hello)

score=80
print("성적:"+str(score))

#문자열 반복 연산자
x='토끼'*10
print(x)

print('-'*20)

#문자열 길이
y='가는 말이 고와야 오는 말이 곱다.'
n=len(y)
print('문자열의 길이:'+str(n))

#문자열 포멧팅
animal='고양이'
x='나는 %s를 좋아합니다.'%animal
print(x)

age=25
print('내 나이는 %d살 입니다.'%age)
'''
%s: 문자열
%d: 정수형 숫자or변수
%f: 실수형 숫자or변수
'''
kor=88
eng=95
math=97
sum=kor+eng+math
avg=sum/3
print('합계:%d,평균:%.2f'%(sum,avg))

#키보드 입력
'''
person=input('이름을 입력하세요:')
print(person+"님 안녕하세요.")
'''
a= input('첫번째 정수를 입력하세요 :')
b=input('두번째 정수를 입력하세요 :')
c=int(a)+int(b)
print(str(a)+'+'+str(b)+'='+str(c))

