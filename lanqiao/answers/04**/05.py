# 解题思路：
# 1、明确输出目标是装入书包的商品的最大价值
# 2、
# ①明确目标后，那么价值肯定只从大到小依次加起来，但要注意使用sort()指令排序话，无法使得两个列表排序之后还是对应关系的~
# ②所以要借助index()索引值指令以及第三个列表帮助
# 3、考虑是否全部加起来没有超过体积大小的情况~

m,n=map(int,input().split(","))
a=list(map(int,input().split(",")))##体积列表
b=list(map(int,input().split(",")))##价值列表
c=b[:]##建立价值2列表，不影响原来的对应关系
if sum(a)<m:##是否全部加起来没有超过体积大小
  print(sum(b))
else:
  # 暴力枚举所有的可能
  for i in range(n):
    key = a[i]
    t = a[i]  ##体积
    s = b[i]  ##价值
    for j in range(n):
      if (i != j and key + a[j] < m):
        c.append(b[i] + b[j])
        t += a[j]
        s += b[j]
        if t > m:
            t -= a[j]
            s -= b[j]
        c.append(s)
print(max(c))
