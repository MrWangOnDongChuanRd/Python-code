from tkinter import *
from math import *
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
    c = Canvas(root,width=700,height=700,bg='white')
    c.pack()
    x = 0
    w = cal_width(n)
    wb = cal_width_between(n)
    for k in range(1,n+1):
        col = c.create_rectangle(x,710,x + w,700-cal_height(res,a,i,k),outline="dodgerblue",fill="dodgerblue")
        now = round(a*((1+i)**k),3)
        txt = c.create_text(x + w/2,700-cal_height(res,a,i,k),text=now,anchor=S,fill="black")
        x = x + wb + w
    
def main():
    a = input("Please input a:")
    i = float(input("Please input i:"))
    n = input("Please input n:")
    res = a*((1+i)**n) 

main()