questions = ['s_hool','compu_er','deco_ation','windo_','hi_tory']
answer = ['c','t','r','w','s']

for i in range(0,len(questions)):
  q = '%s : 밑줄에 들어갈 알파벳은? : '%questions[i]
  g = input(q)


  if g == answer[i] :
    print('정답!')
  else:
    print('땡!')