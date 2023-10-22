A=[]
def abc(list1,left,rihgt):##判断在交换过程中是否出现'1*003*04'
    global A
    r = rihgt
    for i in range(rihgt - 1, left, -1):##这里一定倒数循环，正面循环会提前结束
        if list1[left+1] == '0'and list1[left+2]!='*':
            list1.pop(left+1)##如果存在第一个 * 后面 0 话 删除的之后，left的位置是不变的，继续接着判断是否 0
            r-=1
        else:
            break
    for i in range(len(list1)-1,r+1,-1):
        if list1[r+1]=='0':
            list1.pop(r+1)
        else:
            break
    A.append("".join(list1))

n=int(input())
a=list(input())
for i in range(1,len(a)-n+1):
    b=a[:]
    c=n
    j = i
    while c != 0:
        b.insert(j, "*")
        j += 2
        c -= 1
    c=b[:]
    if c[0]=='0'and c[1]!='*':##'01*23*45'这种情况，一个剔除“0”
        b.remove(c[0])
        j -= 1
        abc(b, j - 4, j - 2)##判断是否有这个类型的母类01*0*010
    else:
        abc(c, j - 4, j-2)

    for z in range(j - 2, len(b) - 2):
        ##这里j-2原因是：j在while循环结束时，增加2，不是第二个"*"的位置
        ##以一个基础类型1*2*3456，再通过循环交换方式，得到他的子类：1*23*456，1*234*56，1*2345*6
        b[z],b[z+1]=b[z+1],b[z]
        c=b[:]##重新将b数组数据导入到c中
        abc(c,j-4,z+1)
print(A)
a.clear()
for i in range(len(A)):
    a.append(eval(A[i]))
print(max(a))
