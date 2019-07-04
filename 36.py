a=input()
count=0
for i in range(len(a)):
  if(a[i].isdigit() or a[i].isalpha() or a[i]==(" ")):
    continue
  else:
    count+=1
print(count)
