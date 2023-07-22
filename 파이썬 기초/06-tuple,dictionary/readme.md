# 📃 튜플(tuple),딕셔너리(dictionary)
***


            
##  💥튜플(tuple)
* 기본문법           
변수 = (데이터,데이터,데이터,·····)
```python
a = ('토끼','거북이','사자','여우')
print(a)

n = tuple(range(10))
print(n)
```         

* 데이터 추출
```python
n = tuple(range(10,21))
print(n)

print('n[0]=',n[0])
print('n[2:5]=',n[2:5])
print('n[2:]=',n[2:])
print('n[:5]',n[:5])
print('n[-2]',n[-2])
print('n[::-1]',n[::-1])   #순서 반대로
```

* 튜플 병합
```python
tup1 = (10,20,30)
tup2 = (40,50,60)
tup3 = tup1 + tup2

print(tup3)
```
## 💥딕셔너리(dictionary)

* 기본문법          
변수 = {key:요소,key:요소,key:요소,·····}

```python
member = {'name':"황예린",'age':22,'email':'yerin@hanmail.net'}
print(member)

score = dict([('국어',80),('영어',90),('수학',100)])
print(score)

```
* 요소 추출
```python
user = {"id":'kim55','name':'강성준','level':7,'point':10000}

print(user)
print(user['id'])
print(user['name'])
print(user['point'])

```
* 요소 추가
```python
user = {"id":'kim55','name':'강성준','level':7,'point':10000}

print(user)
print(user['id'])
print(user['name'])
print(user['point'])

```

* 요소 변경
```python
scores = {'kor':90,'eng':89,'math':98}
print(scores)

scores['music']=100
print(scores)
```

* 요소 삭제
```python
car = {'brand':'현대','model':'아반떼','start':1990,'year':2021}
print(car)

x=car.pop('start')
print(x)

print(car)
```

* 전체삭제
```python
car = {'brand':'현대','model':'아반떼','start':1990,'year':2021}
print(car)

car.clear()
print(car)
```