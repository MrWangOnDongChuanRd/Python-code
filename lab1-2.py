# -*- coding: utf-8 -*-
import math
x = input("请输入一个数字：\n")
s = math.sin(x)
c = math.cos(x)
if x > 0:
    f = math.pow(s * s + c + 1,3) - 3 * (s * s + c)
elif x < 0:
    f = 4 * s * s + 4 * c - 1
else:
    f = math.pi
print (f)
