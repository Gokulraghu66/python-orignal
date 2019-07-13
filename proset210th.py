a=input().split()
t=int(a[0])
con=int(a[1])
l=input().split()
l=[int(i) for i in l]
l=sorted(l,reverse=True)
tem=0
count=0
for i in range(0,len(l)):
  while True:
    if(tem==con):
      break
    elif(tem>con):
      count-=1
      tem-=l[i]
      break
    elif(tem<con):
      tem+=l[i]
      count+=1
print(count)
