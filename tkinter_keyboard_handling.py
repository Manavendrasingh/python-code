import tkinter
x1 = 50
y1 = 50
def btnlogin_click(e):
    pass

def root_Motion(e):
    btnmsg.place(x=e.x_root-25,y=e.y_root-25)
    vartxt1.set('X:'+str(e.x) + 'y:'+str(e.y))
    vartxt2.set('X_root:' + str(e.x_root) + 'y_root:' + str(e.y_root))


def root_key(e):
    obj = e.widget()
    print(obj)
    obj.title("Root_" +str(e.keycode))
    print(e.widget)
    root.title("Root_" +str(e.keycode))
    global x1,y1
    vartxt2.set(str(e.keycode))
    if (e.keycode == 37):
        x1-=5
    elif (e.keycode == 39):
        x1+=5
    elif (e.keycode == 38):
       y1-=5
    elif (e.keycode == 40):
        y1+=5
    btnmsg.place(x= x1,y = y1)

root = tkinter.Tk()
root.minsize(400,400)
root.maxsize(400,400)
btnmsg = tkinter.Button(master = root ,text = "clic khere",fg = "red")
btnmsg.pack()
#btnmsg.bind("<Button-1>",btnlogin_click)
#root.bind("<Button-1>",btnlogin_click)
#root.bind("B1-Motion>",btnlogin_click)
root.bind("<B1-Motion>",root_Motion)
#root.bind("<Key>",root_key)

vartxt1 = tkinter.StringVar()
txt1 = tkinter.Entry(master = root,text = vartxt1)
txt1.pack()


vartxt2 = tkinter.StringVar()
txt2 = tkinter.Entry(master  =root, text = vartxt2)
txt2.pack()





















root.state("zoomed")
root.mainloop()
