## 조건문

##### 🔥 if ~ else ~

> if else 구문

>예제 1
```python
x=int(input('자연수를 입력하세요. : '))

if x%2==0 :
  print('짝수!')

else :
  print('홀수!')
```
>예제 2
```python
pilgi=int(input('필기시험 점수는? : '))
silgi=int(input('실기시험 점수는? : '))

if pilgi>=80 and silgi>=80:
  r='합격'
else :
  r='불합격'

print('-'*30)
print('-필기시험 점수 : %d\n-실기 시험 점수 : %d\n-합격/불합격 여부 : %s'%(pilgi,silgi,r))
```

> 예제 3

``` python
a=input('영어 소문자 한가지를 입력하세요. : ')
if a=='a' or a=='e' or a=='i' or a=='o' or a=='u' :
  r='모음'
else :
  r='자음'
print('%s은(는) %s이다.'%(a,r))
```
