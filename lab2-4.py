num = input("Please input a number:")
new = 0
while True:
    a = num % 10
    b = num / 10 % 10
    c = num / 100 % 10
    if a > b:
        n1 = a
        n3 = b
    else:
        n1 = b
        n3 = a
    if c < n3:
        n3 = c
    if c > n1:
        n1 = c
    n2 = a + b + c - n1 - n3
    max = 100 * n1 + 10 * n2 + n3
    min = 100 * n3 + 10 * n2 + n1
    new = max - min
    print ("%d-%3d=%3d") % (max,min,new)
    an = new % 10
    bn = new / 10 % 10
    cn = new / 100 % 10
    if an > bn:
        n1n = an
        n3n = bn
    else:
        n1n = bn
        n3n = an
    if cn < n3n:
        n3n = cn
    if cn > n1n:
        n1n = cn
    n2n = an + bn + cn - n1n - n3n
    if n1 == n1n and n2 == n2n and n3 == n3n:
        print ("Blackhole has been found!")
        break
    num = new