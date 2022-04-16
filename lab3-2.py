from tkinter import *
def cal_height(res,a,i,n):
    now = a*((1+i)**n)    
    h = now/res * 600
    return h

def cal_width(n):
    w = 500/n
    return w

def cal_width_between(n):
    wb = 200/(n - 1)
    return wb

def draw(res,a,i,n):
    root = Tk()
    c = Canvas(root,width=500,height=500,bg='lightskyblue')
    c.pack()
    x = 0
    w = cal_width(res,a,i,n)
    wb = cal_width_between(res,a,i,n)
    for k in range(1,n+1):
        col = c.create_rectangle(x,700,x + w,cal_height(res,a,i,k),outline="white",fill="white")
        x = x + wb + w
    
def main():
    a,i,n = input("Please input a,i,n(separate by comma):")
    res = a*((1+i)**n)
    draw(res,a,i,n)

main()