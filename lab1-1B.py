# -*- coding: utf-8 -*-
x = input("请输入一个四位数字：\n")
x1 = x % 10
x2 = x // 10 % 10
x3 = x // 100 % 10
x4 = x //1000 % 10
new = 1000 * ((x2 + 9) % 10)+ 100 * ((x1 + 9) % 10) + 10 * ((x4 + 9) % 10) + 1 * ((x3 + 9) % 10)
if new < 1000:
    print ('0'+str(new))
else:
    print (new)
