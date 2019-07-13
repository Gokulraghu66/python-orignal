c=int(input())
array=[]
s=[]
for i in range(c):
    array.append(list(map(int,input().split())))
for llist in array:
    for num in llist:
        s.append(num)
s.sort()
for i in s:
    print(i,end=' ')
