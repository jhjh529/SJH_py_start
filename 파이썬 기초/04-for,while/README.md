# 🔁반복문(for,while)

## ✔for ==> 일정 횟수만큼 반복

>기본for문 예제 
```python
for i in range(10) : #0~9
  print(i,end=' ')
print()

for i in range(1,11): #1~10
  print(i,end=' ')
print()

for i in range(1,10,2): #1,3,5,7,9
  print(i,end=' ')
print()

for i in range(20,0,-2):  #20,18,16,·····,2
  print(i,end=' ')

'''
*기본 문법*
for 변수 in range(시작값,종료값,증가값)
  문장~~
'''
```
>이중 for문 예제
```python
for i in range(0,5):
  for j in range(0,10):
    print('*',end=' ')
  print()
```

## while ==> 어느 조건이 만족할때 반복
>while 예제
```python
sum = 0
i = 500

while i <= 600 :
  if i%5 == 0 :
    sum += i

  i += 1

print('5의 배수의 합계 : %d'%sum)

```

## 🔙break ==> 반복문 빠져나가기
>break 예제
```python
for i in range(1,1001):
  print(i)

  if i == 10 :
    break
```