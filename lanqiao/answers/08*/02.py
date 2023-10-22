#0~9  48~57
#A~Z  65~90
#a~z  97~122
#ord()  将字符转化成ASCLL码
#chr()  将ASCLL码转化成字符

a = input()
z = 0
k = 0
s = 0
q = 0
for i in a:
    if 65<=ord(i)<= 90 or 97<=ord(i)<=122:
        z += 1
    elif i == " ":
        k += 1
    elif 48<=ord(i)<=57:
        s += 1
    else:
        q += 1
print(z)
print(k)
print(s)
print(q)
