n=int(input())
m=input().split(",")
res=0
for i in range(0,n-1):
  for j in range(i+1,n):
    if int(m[i])+int(m[j])==n:
      res+=1
print(res)
