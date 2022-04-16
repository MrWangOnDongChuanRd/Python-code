try:
    def slope(p1, p2):
        print ("The slope is %.3f") % (float(p1y-p2y)/float(p1x-p2x))

    def intercept(p1, p2):
        print ("The intercept is %.3f") % (p1y - p1x*float(p1y-p2y)/float(p1x-p2x))
    
    p1x, p1y = input("Please input p1:")
    p2x, p2y = input("Please input p2:")
    p1 = (p1x, p1y)
    p2 = (p2x, p2y)
    slope(p1, p2)
    intercept(p1, p2)

except ZeroDivisionError:
    print ("The slope does not exist")
