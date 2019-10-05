import tkinter
def btngender_click():
    if vargender.get() == "Male":
        print("you are selected male")
    else:
        print("you are selected Female")




root = tkinter.Tk()
root.minsize(400,500)
root.maxsize(400,500)

framegender  =tkinter.LabelFrame(master  = root ,text = "Gender ")
framegender.grid(row =0 ,column = 0)


vargender = tkinter.StringVar()
rbtMale = tkinter.Radiobutton(master = framegender ,text = "Male",value = "Male",variable = vargender)
rbtMale.pack()

rbtFemale = tkinter.Radiobutton(master = framegender ,text = "FeMale",value = "FeMale",variable = vargender)
rbtFemale.pack()

vargender.set("Male")

btngender = tkinter.Button(master  = root ,text = "Choice",command = btngender_click)
btngender.grid(row= 1,column = 0)





root.state("zoomed")
root.mainloop()