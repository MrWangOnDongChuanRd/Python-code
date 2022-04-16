def f(a,n):
    s = 0
    while n > 0:
        n = n - 1
        s = s + a * (10 ** n)
    return s

a = input("Please input a:")
n = input("Please input n:")
s = 0
for i in range(1,n+1):
    s = s + f(a,i)
print (s)
