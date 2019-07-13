asd,ssd=map(int,input().split())
law=list(map(int,input().split()))
asd=[]
law.insert(0,0)
for p in range(ssd):
     vim=[]
     sha=0
     but,zee=map(int,input().split())
     for i in range(but,zee+1):         
         sha^=law[i]     
     asd.append(sha)
for p in asd:
     print(p)
