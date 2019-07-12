s11,s22=map(int,input().split())
count=0
arr=list(map(int,input().split()))[:s11]
for i in arr:
  if i==s22:
    count+=1
if(count!=0):
  print("yes")
else:
  print("no")
