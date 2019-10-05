import tkinter
def btnlogin_click(e):
    vartext1.set('X:' +str(e.x) + 'Y:' +str(e.y))
    vartext2.set('X_root'+str(e.x_root)+ 'y_root'+str(e.y_root))

root = tkinter.Tk()
root.title("manvendra Singh")
root.minsize(400,400)
btnmsg = tkinter.Button(master = root ,text = "click here",bg = "red")
btnmsg.pack()
#btnmsg.bind("<Button-1>",btnlogin_click)#this give co ordinate of cursor when leftclick diffreent positon of clickbutton
#btnmsg.bind("<Button-2>",btnlogin_click)#this give co ordinate of cursor when middleclick diffreent positon of clickbutton(button 2 work ony for mouse not touchpad)
#btnmsg.bind("<Button-3>",btnlogin_click)#this give co ordinate of cursor when rightclick diffreent positon of clickbutton
#root.bind("<Button-1>",btnlogin_click)#this give coordinate of cursor when click any where on tk
#root.bind("<B1-Motion>",btnlogin_click)# this give co ordinate of cursor when  click on touchpad and move cursor
#root.bind("<Motion>",btnlogin_click)#this give co ordinate of cursor without click on touchpad and move cursor


vartext1 = tkinter.StringVar()
txt1 =  tkinter.Entry(master  =root ,text = vartext1)
txt1.pack()

vartext2 = tkinter.StringVar()
txt2 =  tkinter.Entry(master  =root ,text = vartext2)
txt2.pack()










root.state("zoomed")
root.mainloop()