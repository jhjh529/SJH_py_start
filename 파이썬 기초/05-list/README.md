# 📜리스트(list)

>💥 리스트의 메소드
>>1️⃣ append() --> #append(값)  맨마지막에 값 추가
>```python
>arr = [5,3,12,9,2]
>print(arr)
>
>arr.append(10) #
>print(arr)
>```
>
>>2️⃣ insert() --> #insert(인덱스번호,값) 인덱스번호에 값추가
>```python
>fruits = ['apple','orange','banana','cherry']
>print(fruits)
>
>fruits.insert(1,'melon') #
>print(fruits)
>
>fruits.insert(2,'stawberry') #
>print(fruits)
>```
>
>>3️⃣ index() --> #index(인덱스번호)  인덱스번호의 값 가져옴
>```python
>number = [5,20,13,7,8,22,7,17]
>print(number)
>
>idx= number.index(7) #
>print(idx)
>```
>
>>4️⃣ remove() --> #remove(값)  값 삭제
>```python
>member = ['홍지웅',20,'경기도 김포시','abcdef@abc.com']
>print(member)
>
>member.remove(20)  #
>print(member)
>```
>
>>5️⃣ pop() --> pop(인덱스번호) 인덱스번호의 값을 추출후 삭제
>```python
>data = [10,20,30,40,50,60,70,80]
>print(data)
>
>x= data.pop(2) #
>print(x)
>print(data)
>
>x= data.pop(3) #
>print(x)
>print(data)
>```
>
>>6️⃣ clear() --> #clear()  값모두 삭제
>```python
>data = [3,12,7,-3,-9]
>print(data)
>
>data.clear() #
>print(data)
>```
>
>>7️⃣ reverae() --> #reverse()  리스트 값의 순서 거꾸로
>```python
>data=[10,20,30,40,50]
>print(data)
>
>data.reverse() #
>print(data)
>```
>
>>8️⃣ copy() --> #copy()  리스트복사
>```python
>fruits = ['apple','banana','orange']
>print(fruits)
>
>x= fruits.copy() #
>print(x)
>```
>
>>9️⃣ sort() --> #sort()  리스트의 값들을 오름차순으로 정리(<),sort(reverse=True)  리스트의 값들을 내림차순으로 정리(>)
>```python
>data = [12,8,15,32,-3,-20,15,34,6]
>print(data)
>
>data.sort()  #
>print(data)
>
>data.sort(reverse=True)  #
>print(data)
>```

>💥 내장함수
>>1️⃣ list() --> #새로운 리스트 생성
>```python
>list1 = [3,15,-12.5,'사과','딸기']
>print(list1)
>
>list2 = list(range(1,21,2))  #
>print(list2)
>```
>>2️⃣ len() --> #리스트의 길이를 구함
>```python
>colors = ['빨간색','파란색','노란색','검정색','초록색']
>
>n= len(colors) #
>for i in range(0,n):
>  print('나는 %s를 좋아한다'%colors[i])
>```
>>3️⃣ sum() --> #리스트 요소들의 합계를 구함
>```python
>scores = [80,90,85,95,100]
>
>sum=sum(scores) #
>avg=sum/len(scores)
>
>print('합계 : ',sum)
>print('평균 : ',avg)
>```