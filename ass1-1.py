# -*- coding: utf-8 -*-
weight = input('Weight(kg):')
height = input('Height(m):')
BMI = float(float(weight)/(float(height)**2))
if BMI <=19:
    print('轻体重')
elif BMI  < 25:
    print('健康体重')
elif BMI < 28:
    print('超重')
else:
    print('肥胖')
