phone_list1 = ['010-1234-5678','010-9876-5432','010-4321-9876']
print(phone_list1)

phone_list2 = []
for number in phone_list1 :
  x= number.replace('-','')

  phone_list2.append(x)

print(phone_list2)