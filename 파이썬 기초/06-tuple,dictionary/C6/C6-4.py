words = {'꽃':'flower','나비':'buttertly','학교':'school','자동차':'car','비행기':'airplane'}
print('<영어 단어 맞추기 퀴즈>')

for kor in words:
    input_words=input("'%s'에 해당되는 영어 단어를 입력하세요 :  "%kor)

    if input_words==words[kor]:
        print('정답입니다!')
    else:
        print('오답입니다~!')


