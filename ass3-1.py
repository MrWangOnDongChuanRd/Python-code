from tkinter import *
def snowman():
    body = c.create_oval(60,550,230,750,fill="white")
    head = c.create_oval(90,430,200,550,fill="white")
    eye_l = c.create_oval(100,460,120,480,fill="dimgray")
    eye_r = c.create_oval(130,460,150,480,fill="dimgray")
    nose = c.create_polygon(125,480,125,480+20,60,480+10,fill="darkorange")
    mouth = c.create_arc(100,495,150,525,start=180,extent=180,fill="orangered",style="chord")
    cap_l = c.create_arc(90,420,200,480,start=0,extent=180,outline="midnightblue",fill="midnightblue",style="chord")
    for i in range(2,9):
        c.move(i,300,20)
    arm1 = c.create_line(320,560,370,620,fill="sienna",width=5)
    arm2 = c.create_line(380,550,440,650,fill="sienna",width=5)
    
def tree():
    truck_light = c.create_rectangle(170,720,200,749,outline="sienna",fill="sienna")
    truck_dark = c.create_rectangle(155,720,170,749,outline="saddlebrown",fill="saddlebrown")
    leaf3 = c.create_polygon(75,720,280,720,177.5,580,outline="darkgreen",fill="darkgreen")
    #snow3 = c.create_line(75,720,177.5,580,280,720,fill="white",width=7)
    leaf2 = c.create_polygon(75+20,720-100,280-20,720-100,177.5,580-100,outline="forestgreen",fill="forestgreen")
    #snow2 = c.create_line(75+20,720-100,177.5,580-100,280-20,720-100,fill="white",width=7)
    leaf1 = c.create_polygon(75+40,720-200,280-40,720-200,177.5,580-200,outline="mediumseagreen",fill="mediumseagreen")
    #snow1 = c.create_line(75+40,720-200,177.5,580-200,280-40,720-200,fill="white",width=7)
    
root = Tk()
c = Canvas(root,width=600,height=800,bg='lightskyblue')
c.pack()
ground = c.create_rectangle(0,750,610,810,outline="white",fill="white")
snowman()
tree()
sun = c.create_oval(400,60,500,160,fill="tomato",outline="tomato")
txt = c.create_text(590,790,text="2022.4.5 王宇尘 520111910178",anchor=SE,fill="black")
root.mainloop()
