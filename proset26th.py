asd=int(input())
cadt=list(map(int,input().split()))
x=[1]*asd
for pa in range(asd):
    if pa==0:
        if cadt[pa]>cadt[pa+1]:
            x[pa]=x[pa]+x[pa+1]
    elif pa>0:
        if cadt[pa]>cadt[pa-1]:
            x[pa]=x[pa]+x[pa-1]
print(sum(x))
