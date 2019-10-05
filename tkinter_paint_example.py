import  tkinter
X1,Y1,X2,Y2 = 0,0,0,0
def mycanvas_click(e):
    global X1,Y1
    X1=e.x
    Y1=e.y

def mycanvas_B1_motion(e):
    global X1,Y1,X2,Y2
    X2 = e.x
    Y2 = e.y
    mycanvas.create_line(X1,Y1,X2,Y2)
    X1 = X2
    Y1 = Y2

#def btnlogin_click(e):
    #pass
def newfile():
    pass
def openfile():
    pass
def savefile():
    pass
def savefileas():
    pass
def printfile():
    pass
def Zoomin_click():
    pass
def Zoomout_click():
    pass





#PPL
root = tkinter.Tk()
root.minsize(400,500)
for r in range(4):
    root.rowconfigure(index = r,minsize = 75)
for c in range(4):
    root.columnconfigure(index = c ,minsize = 75)


#btnmsg = tkinter.Button(master = frameTraing,text = "click",fg = "green")
#btnmsg.pack()

#mainmenu = tkinter.Menu(master  = root)

#filesubmenu = tkinter.Menu(master = mainmenu)
#filesubmenu.add_command(label="New ", command=newfile)
#filesubmenu.add_command(label="Open", command=openfile)
#filesubmenu.add_command(label="Save", command=savefile)
#filesubmenu.add_command(label="Save as", command=savefileas)
#filesubmenu.add_command(label="Print.", command=printfile)

#mainmenu.add_cascade(label = "File",menu = filesubmenu)

#btnmsg = tkinter.Button(master  = root ,text = "click here",fg = "green")
#btnmsg.pack()

#btnmsg.bind("<Button-1>",btnlogin_click)
#root.bind("<Button-1>",btnlogin_click)
#root.bind("<B1-Motion>",btnlogin_click)


#vartxt1 = tkinter.StringVar()
#txt1 = tkinter.Entry(master  = root,text = vartxt1)
#txt1.pack()


#vartxt2 = tkinter.StringVar()
#txt2 = tkinter.Entry(master  = root ,text = vartxt2)
#txt2.pack()


mycanvas = tkinter.Canvas(master  =root ,bg = "white")
mycanvas.place(x = 500,y = 500)
mycanvas.bind("<Button-1>",mycanvas_click)
mycanvas.bind("<B1-Motion>",mycanvas_B1_motion )


mainmenu = tkinter.Menu(master  = root)

filesubmenu = tkinter.Menu(master = mainmenu)
filesubmenu.add_command(label="New ", command=newfile)
filesubmenu.add_command(label="Open", command=openfile)
filesubmenu.add_command(label="Save", command=savefile)
filesubmenu.add_command(label="Save as", command=savefileas)
filesubmenu.add_command(label="Print.", command=printfile)

viewsubmenu = tkinter.Menu(master = mainmenu )
viewsubmenu.add_command(label = "Zoom In",command = Zoomin_click)
viewsubmenu.add_command(label = "Zoom Out",command = Zoomout_click)




mainmenu.add_cascade(label = "File",menu = filesubmenu)
mainmenu.add_cascade(label = "View",menu = viewsubmenu)
root.config(menu = mainmenu)

#shapebtn1 = tkinter.Button(master = root ,text =  "O",width = "32")
#shapebtn1.grid(row = 0,column = 0,columnspan = 2)


root.state("zoomed")
root.mainloop()