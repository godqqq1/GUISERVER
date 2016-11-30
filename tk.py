from Tkinter import *
root = Tk()
print(root.winfo_screenwidth(),root.winfo_screenheight())
frame = Frame(root,width=300,height=300)
frame.pack()
root.mainloop()
