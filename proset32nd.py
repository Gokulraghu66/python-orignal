asd=int(input())
ssd=list(map(int,input().split()))
su=0
se=0
for i in range(asd):
	if i%2==0:
		su=su+ssd[i]
	else:
		se+=ssd[i]
print(max(su,se))
