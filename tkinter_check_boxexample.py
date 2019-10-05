import tkinter
"""this function print which option is selected"""
def btngender_click():
    strcourse = ""
    if varPython.get() == 1:
        strcourse+= "Python "
    if varMl.get() == 1:
        strcourse+= "Machine Learning "
    if varJava.get()  == 1:
        strcourse+="Java"
    print(strcourse )






root = tkinter.Tk()
root.minsize(400,500)
root.maxsize(400,500)
frameTraing  =tkinter.LabelFrame(master  = root ,text = "select Traing  ")
frameTraing.place(x= 20,y = 20)

varPython = tkinter.IntVar()
chkPython  = tkinter.Checkbutton(master  =frameTraing,text = "python",onvalue = 1,offvalue = 0,variable = varPython)
chkPython.pack()
varPython.set(1)

varMl = tkinter.IntVar()
chkMl  = tkinter.Checkbutton(master  =frameTraing,text = "machine Learing",onvalue = 1,offvalue = 0,variable = varMl)
chkMl.pack()


varJava = tkinter.IntVar()
chkJava  = tkinter.Checkbutton(master  =frameTraing,text = "java",onvalue = 1,offvalue = 0,variable = varJava)
chkJava.pack()

btncourses = tkinter.Button(master  = root ,text = "Read courese",command = btngender_click)
btncourses.grid(row= 1,column = 0)






root.state("zoomed")
root.mainloop()