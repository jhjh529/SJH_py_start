pilgi=int(input('필기시험 점수는? : '))
silgi=int(input('실기시험 점수는? : '))

if pilgi>=80 and silgi>=80:
  r='합격'
else :
  r='불합격'

print('-'*30)
print('-필기시험 점수 : %d\n-실기 시험 점수 : %d\n-합격/불합격 여부 : %s'%(pilgi,silgi,r))