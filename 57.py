s11,s22=map(int,input().split())
count=0
ar=list(map(int,input().split()))[:s1]
for i in ar:
  if i==s22:
    count+=1
print(count)
