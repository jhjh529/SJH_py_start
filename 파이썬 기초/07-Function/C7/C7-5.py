def tri_area(w,h):
    result = w * h *0.5
    return result

W=int(input('너비를 입력하세요 : '))
H=int(input('높이를 입력하세요 : '))

print('-삼각형의 너비 : ',W)
print('-삼각형의 높이 : ',H)
print('삼각형의 면적 : ',tri_area(W,H))