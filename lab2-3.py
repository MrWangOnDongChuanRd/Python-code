from operator import truediv


def square(x):
    flag = 0
    for i in range(1,33):
        if i*i == x:
            return True
            flag = 1
            break
    if flag == 0:
        return False

def two(x):
    a = x % 10
    b = x / 10 % 10
    c = x / 100 % 10
    if a == b or a == c or b == c:
        return True
    else:
        return False

count = 0
n = input("Please input n:")
for i in range(100,n+1):
    if square(i) and two(i):
        count = count + 1
        print (i)
print ("There is(are) %d number(s) matching the condition") % (count)