s=input()
abc=[0,0,0]
for c in s:
  if c=='A':
    abc[0]+=1
  if c=='B':
    abc[1]+=1
  if c=='C':
    abc[2]+=1
print(min(abc))
