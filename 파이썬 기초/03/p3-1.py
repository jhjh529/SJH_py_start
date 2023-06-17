#특정 범위 수 인지 판정

startN=int(input('시작 수는? : '))
endN=int(input('끝 수는? : '))
N=int(input('정수를 입력하세요. : '))
r='사이에 없다.'

if startN<= N and endN>= N :
  r='사이에 있다.'

print('%d은(는) %d ~ %d %s'%(N,startN,endN,r))