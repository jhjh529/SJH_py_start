f_n = ['file1.py','file2.txt','file3.pptx','file4.doc']

for i in range(0,len(f_n)):
    a=f_n[i]
    b=a.split('.')
    #print(b)
    print('<  %s => 파일명: %s , 확장자: .%s  >'%(a,b[0],b[1]),end='\n\n')
    