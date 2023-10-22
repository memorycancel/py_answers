#第四题
#枚举法：遍历所有可能性，满足条件的即为正确答案

# 1、输入一个n（3~9）
# 2、选择三个组成三位数
# 3、百位不为0，且奇数，且不重复
# 4、输出个数

n = int(input())
s = 0
for a in range(0,n+1):         #a:0~n
  for b in range(0,n+1):     #b:0~n
    for c in range(0,n+1): #c:0~n
      if a != 0 and c%2 == 1 and a!=b and a!=c and b!=c:
        s += 1
print(s)
