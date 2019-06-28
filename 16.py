ge,ne=map(int,input().split())
for i in range(ge+1,ne):
  if i>1:
    for y in range(2,i):
      if(i%y==0):
        break
    else:
      print(i,end=" ")
