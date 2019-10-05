import tkinter








root = tkinter.Tk()
root.minsize(400,400)
root.title("MS-paint")
myfram = tkinter.LabelFrame(master = root,bg ="bisque" )
myfram.grid(row  = 0,column = 0)
mycanvas = tkinter.Canvas(master = root,bg ="white" )
mycanvas.pack(fill = 'both',expand = True)








root.state("zoomed")
root.mainloop()