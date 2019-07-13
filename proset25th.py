asd=input()
ssd=map(int,input().split())
pawt=[]
for g in ssd:
    enum=bin(g)
    pawt.append(enum)
f=sorted(pawt)
f.reverse()
for h in f:
    print(int(h,2))
