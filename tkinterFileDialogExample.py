import tkinter
import tkinter.filedialog
def btnMsg_Click():
    # res=tkinter.filedialog.askopenfilename()
    res = tkinter.filedialog.asksaveasfilename()
    print(res)
root =tkinter.Tk()
root.minsize(300,300)
btnMsg=tkinter.Button(master=root,text="Save File",command=btnMsg_Click)
btnMsg.pack()
root.mainloop()