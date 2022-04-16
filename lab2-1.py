n = input("Please input n:")
x = 0
while n > 0:
    for i in range(0,n):
        if x >= 26:
            x = x-26
        print ("%s ") % chr(ord('A')+x),
        x = x + 1
    print (" ")
    n = n - 1
