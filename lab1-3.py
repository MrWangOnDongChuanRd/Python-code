# -*- coding: utf-8 -*-
i = 0
while i <= 3:
    print ("[1] 苹果\n[2] 梨\n[3] 橙子\n[4] 葡萄\n[0] 退出\n")
 
    x = input("请输入序号：\n")
    if x == 0:
        i = i + 4
    elif x == 1:
        print ("3.00元/千克\n")
        i = i + 1
    elif x == 2:
        print ("2.50元/千克\n")
        i = i + 1
    elif x == 3:
        print ("4.10元/千克\n")
        i = i + 1
    else:
        print ("10.20元/千克\n")
        i = i + 1
