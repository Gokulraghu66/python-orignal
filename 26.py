go=int(input())
ro=list(map(int,input().split()[:go]))
ro.sort()
for i in ro:
   print(i,end=" ")
