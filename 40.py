asd=int(input())
fact,fa2=0,1
print(fa2,end=" ")
for i in range(1,asd):
  fabo=fact+fa2
  print(fabo,end=" ")
  fact,fa2=fa2,fabo
