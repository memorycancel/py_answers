n=int(input())
res=0
for i in range(1,n):
  for j in range(1,n):
    for k in range(1,n):
      if i+j+k==n and i>=j and j>=k:
        res+=1
print(res)
