#第三题

#1、输入八个分数
#2、去掉最高分和最低分
#3、求平均数
#4、输出并保留两位小数

a,b,c,d,e,f,g,h = map(int,input().split(","))
ping = (a+b+c+d+e+f+g+h-max(a,b,c,d,e,f,g,h)-min(a,b,c,d,e,f,g,h))/6
print(format(ping,".2f"))
