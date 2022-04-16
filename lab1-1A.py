# -*- coding: utf-8 -*-
x = input("请输入一个四位数字：\n")
new = 1000 * ((int(x[2]) + 9) % 10)+ 100 * ((int(x[3]) + 9) % 10) + 10 * ((int(x[0]) + 9) % 10) + 1 * ((int(x[1]) + 9) % 10)
if new < 1000:
    print ('0'+str(new))
else:
    print (new)
