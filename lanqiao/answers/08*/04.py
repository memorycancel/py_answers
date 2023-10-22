#[1,11,-2,3,1] 没有0层，不能通过简单加减法计算楼层数
#分类讨论：
#1、前后两个数字楼层同正或同负  不经过0层  楼层数就是大的减小的
#2、前后两个数字楼层一正一负    经过0层   楼层数大的减小的之后还要减一层
lst = list(map(int,input().split(",")))   #一行输入多个数字存入列表中
dian = 0  #用电量初始0
for i in range(len(lst)-1):  #遍历列表所有楼层（除最后一个）
  if(lst[i]>0 and lst[i+1]>0) or (lst[i]<0 and lst[i+1]<0): #同正或同负
    if lst[i+1] > lst[i]:   #后者大，上楼
        dian += 1*(lst[i+1] - lst[i])
    else:                   #后者小，下楼
      dian += 0.3*(lst[i] - lst[i+1])
  else:                        #一正一负
    if lst[i+1] > lst[i]:          #后者大，上楼
        dian += 1*(lst[i+1] - lst[i] - 1)   #减1 减的是0层
    else:                   #后者小，下楼
      dian += 0.3*(lst[i] - lst[i+1] -1)
print(dian)
