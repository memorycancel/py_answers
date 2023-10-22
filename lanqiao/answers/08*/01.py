#一行输入一个变量
#n =int(input())

#一行输入多个变量
#将输入的内容，通过逗号切开，变成int,赋值给n和m
#n,m = map(int,input().split(","))


#一行输出一个变量
#print(a)
#一行输出多个变量
#print(a,b,c,sep = ",",end = ".") #sep 设置间隔  end 设置结束方式
#print(",".join(lst))  #lst中一定要是字符串


lst = []
m =int(input())
n =int(input())

for i in range(m,n+1,1):
    if i%7 == 0 and i%5 != 0:
        lst.append(str(i))
print(",".join(lst))
