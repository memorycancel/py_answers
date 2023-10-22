lst = list(map(int,input().split(",")))
n = 0  #传递次数
ping = sum(lst)/len(lst)
max_n = max(lst)
#从左到右
for i in range(len(lst)):
    if lst[i] > ping and i <= len(lst)-2:
        n += 1
        x = (len(lst)-i-1)*ping - sum(lst[i+1:])
        if x >= (lst[i]-ping):
            lst[i+1] += lst[i]-ping
            lst[i] = ping
        else:
            lst[i+1] += x
            lst[i] -= x

#从右到左
for i in range(len(lst)):
    if lst[len(lst)-i-1] > ping and i <= len(lst)-2:
        n += 1
        x = (len(lst)-i-1)*ping - sum(lst[:len(lst)-i-1])
        if x >= (lst[len(lst)-i-1]-ping):
            lst[len(lst)-i-2] += lst[len(lst)-i-1]-ping
            lst[len(lst)-i-1] = ping
        else:
            lst[len(lst)-i-2] += x
            lst[len(lst)-i-1] -= x
print(n)
