#一行输入很多数字
#输出平均数、中位数、众数


#一行输入多个内容存在lst列表里
lst = list(map(int,input().split(",")))

#求平均数
print(format(sum(lst)/len(lst),".2f"))

#求中位数
lst.sort(reverse = True) #列表的排序
if len(lst)%2 == 1:
    print(format(lst[len(lst)//2],".2f"))
else:
    print(format((lst[len(lst)//2-1]+lst[len(lst)//2])/2,".2f"))

#求众数
#lst.count(x)统计列表中x出现的次数
n = 0 #出现的次数
x = 0 #出现次数最多的值
for i in lst:
    if lst.count(i) >= n:
        n = lst.count(i)
        if i>=x:
            x = i
print(x)
