def cm_to_inch(cm):
    inch = cm * 0.393701
    print('%d cm → %.2f inch'%(cm,inch))

def kg_to_pound(kg):
    pound = kg * 2.204623
    print('%d kg → %.2f pound'%(kg,pound))



print('-선택 옵션\
      \n 1. 길이환산(cm → inch)\
      \n 2. 무게 환산(kg → pound)')
option=int(input('원하는 환산 단위를 입력하세요(1/2) : '))
if option == 1:
    cm = int(input('cm의 길이를 입력하세요 : '))
    cm_to_inch(cm)
if option == 2 :
    kg = int(input('kg의 무게를 입력하세요'))
    kg_to_pound(kg)

