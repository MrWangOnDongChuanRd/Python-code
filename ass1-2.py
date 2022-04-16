# -*- coding: utf-8 -*-
y = input("请输入一个年份:")
b = int(y)
if  (b % 100 != 0 and b % 4 ==0) or (b % 100 == 0 and b % 400 ==0) :
    print("这个年份是闰年")
else:
    print("这个年份不是闰年")
