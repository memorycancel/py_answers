#素数：（质数）只能被1和他本身整除的大于1的自然数
#n  (1)  2,3,4,5,6...n-1  (n)  之中有没有因数
#1、先判断质数
def zhi(n):  #声明一个可以判断n是不是质数的函数
    if n>1:
        for i in range(2,n,1):  #遍历2~n-1 的范围
            if n%i == 0:  #发现因数，返回0
                return 0
        return 1  #没有发现，返回1，说明是质数
    else:
        return 0

#判断是不是超级质数
#过程：
#判断是不是质数
#去掉末尾
#判断
#去掉
#判断

def czhi(a):
    while  a>0:
        if zhi(a) == 0:
            return 0
        a = a//10
    return 1

#以下为主程序

n = int(input())
sum = 0
for i in range(2,n+1):#遍历从2到n的所有数字
    if czhi(i) == 1:  #判断是不是超级质数
        sum += 1
print(sum)
