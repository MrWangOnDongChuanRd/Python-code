def leapyear(y):
    if y % 4 == 0 and (y % 100 !=0 or y % 400 ==0):
        return 1

def days_before_y(y):
    sum = 0
    for i in range(2000,y):
        if leapyear(i) == 1:
            sum = sum + 366
        else:
            sum = sum + 365
    return sum

def days_after_y(y,m,d):
    sum = 0
    if leapyear(y) == 1:
        months = [31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        months = [31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range(1,m):
        sum = sum + months[i-1]
    sum = sum + d
    return sum

def main():
    year,month,day = input("Please input a date:(separate by comma):")
    if ((days_before_y(year) + days_after_y(year,month,day)) % 5 == 0) or ((days_before_y(year) + days_after_y(year,month,day)) % 5 == 4):
        print ("drying net")
    else:
        print ("fishing")

main()