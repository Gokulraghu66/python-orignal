b,s = input().split()
s = int(s)
fa = False
bent = list(map(int,input().split()))
for i in range(len(bent)):
    for j in range(len(bent)):
        if bent[i]+bent[j] == s:
            fa = True
print("yes" if fa else "no") 
