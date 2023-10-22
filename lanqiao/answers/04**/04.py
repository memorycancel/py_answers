lst=list(map(int,input().split(",")))
res=-1
tar=int(input())
for i in range(len(lst)-1):
  for j in range(i+1,len(lst)):
    he=lst[i]+lst[j]
    if he<tar and he>res:
      res=he
print(res)
