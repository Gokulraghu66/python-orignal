asd,ssd=map(int,input().split())
lostt=list(map(int,input().split()))
lawt=[]
for p in range(0,ssd):
     shat,shet=map(int,input().split())
     lawt.append([shat,shet])
for p in range(ssd):
     last=lawt[p][0]
     upot=lawt[p][1]
     yawt=sum(lostt[last-1:upot])
     print(yawt)
