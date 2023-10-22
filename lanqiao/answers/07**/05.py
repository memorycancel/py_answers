#1、输入一个m
#2、遍历m位的所有可能性
#3、判断是不是回文数，统计个数
#4、是回文数的同时再判断里面有没有99，统计个数

m = int(input())
s1 = 0
s2 = 0
for i in range(10**(m-1),10**m):
    a = str(i)
    if a == a[::-1]:
        s1 += 1
        if "99" in a:
            s2 += 1

print(s1)
print(s2)
