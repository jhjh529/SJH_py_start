def member_join(*args):
    result=''
    for arg in args :
        result = result + arg +' '
    
    print('가입 회원 : ',result)

member_join('송지호','홍길동','강민지')
member_join('황선형','김철영','안서영','함소연')