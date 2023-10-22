n = int(input()) #输入整数n
s = 0            #和为0

if n%2 == 0:     #偶数
  for i in range(2,n+1,2):  #i:2,4,6...n
    s += 1/i

if n%2 == 1:     #奇数
  for i in range(1,n+1,2):  #i:1,3,5...n
    s += 1/i

print(format(s,".2f"))  #保留两位小数输出
