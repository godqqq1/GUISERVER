import globall

from Tkinter import *

from operator import eq

import tkMessageBox

class touch2():

    res = ""
    global root

    global result

    spott = False
    def some():
        print("zz")
    def __init__(self):
        self.root = Toplevel()
        self.root.protocol('WM_DELETE_WINDOW',self.some)
        self.root.geometry("300x245")
        self.root.configure(background="RoyalBlue3")

        self.root.resizable(False, False)

        self.root.title("Set")
        dummy0 = Label(self.root,text="      ",background="RoyalBlue3")

        dummy0.grid(row=0,column=0)

        self.result = Label(self.root, text=self.res,background = "white",width=14,anchor=E)  # title label

        self.result.grid(row=1, column=1,columnspan=3, sticky = W)  # merge cell

        dummy1 = Label(self.root,text="      ",background="RoyalBlue3")

        dummy1.grid(row=2,column=0)

        one = Button(self.root,text="1",width=5,height=2,command=self.addone,background="SteelBlue2",foreground="white")

        one.grid(row=3,column=0, sticky = W, padx = 3,pady = 2)

        two = Button(self.root,text="2",width=5,height=2,command=self.addtwo,background="SteelBlue2",foreground="white")

        two.grid(row=3,column=1, sticky = W, padx = 3,pady = 2)

        three = Button(self.root,text="3",width=5,height=2,command=self.addthree,background="SteelBlue2",foreground="white")

        three.grid(row=3,column=2, sticky = W, padx = 3,pady = 2)

        esc = Button(self.root,text="ESC",width=5,height=2,command=self.escape,background="SteelBlue2",foreground="white")

        esc.grid(row=3,column=3, sticky = W, padx = 3,pady = 2)

        four = Button(self.root,text="4",width=5,height=2,command=self.addfour,background="SteelBlue2",foreground="white")

        four.grid(row=4,column=0, sticky = W, padx = 3,pady = 2)

        five = Button(self.root,text="5",width=5,height=2,command=self.addfive,background="SteelBlue2",foreground="white")

        five.grid(row=4,column=1, sticky = W, padx = 3,pady = 2)

        six = Button(self.root,text="6",width=5,height=2,command=self.addsix,background="SteelBlue2",foreground="white")

        six.grid(row=4,column=2, sticky = W, padx = 3,pady = 2)

        clr = Button(self.root,text="CLR",width=5,height=2,command=self.clear,background="SteelBlue2",foreground="white")

        clr.grid(row=4,column=3, sticky = W, padx = 3,pady = 2)

        seven = Button(self.root,text="7",width=5,height=2,command=self.addseven,background="SteelBlue2",foreground="white")

        seven.grid(row=5,column=0, sticky = W, padx = 3,pady = 2)

        eight = Button(self.root,text="8",width=5,height=2,command=self.addeight,background="SteelBlue2",foreground="white")

        eight.grid(row=5,column=1, sticky = W, padx = 3,pady = 2)

        nine = Button(self.root,text="9",width=5,height=2,command=self.addnine,background="SteelBlue2",foreground="white")

        nine.grid(row=5,column=2, sticky = W, padx = 3,pady = 2) 

        bs = Button(self.root,text="Back",width=5,height=2,command=self.backspace,background="SteelBlue2",foreground="white")

        bs.grid(row=5,column=3, sticky = W, padx = 3,pady = 2) 

        dummy2 = Button(self.root,text="",width=5,height=2,background="SteelBlue2",foreground="white")

        dummy2.grid(row=6,column=0, sticky = W, padx = 3,pady = 2)

        zero = Button(self.root,text="0",width=5,height=2,command=self.addzero,background="SteelBlue2",foreground="white")

        zero.grid(row=6,column=1, sticky = W, padx = 3,pady = 2)

        spot = Button(self.root,text=".",width=5,height=2,command=self.addspot,background="SteelBlue2",foreground="white")

        spot.grid(row=6,column=2, sticky = W, padx = 3,pady = 2)    

        ent = Button(self.root,text="ENT",width=5,height=2,command=self.enter,background="SteelBlue2",foreground="white")

        ent.grid(row=6,column=3, sticky = W, padx = 3,pady = 2)    

        self.root.mainloop()

    def addone(self):

        self.res = self.res + "1"

        self.result.configure(text = self.res)

        self.root.update()

        

    def addtwo(self):

        self.res = self.res + "2"

        self.result.configure(text = self.res)

        self.root.update()

        

    def addthree(self):

        self.res = self.res + "3"

        self.result.configure(text = self.res)

        self.root.update()

        

    def addfour(self):

        self.res = self.res + "4"

        self.result.configure(text = self.res)

        self.root.update()

        

    def addfive(self):

        self.res = self.res + "5"

        self.result.configure(text = self.res)

        self.root.update()

        

    def addsix(self):

        self.res = self.res + "6"

        self.result.configure(text = self.res)

        self.root.update()

        

    def addseven(self):

        self.res = self.res + "7"

        self.result.configure(text = self.res)

        self.root.update()

        

    def addeight(self):

        self.res = self.res + "8"

        self.result.configure(text = self.res)

        self.root.update()

        

    def addnine(self):

        self.res = self.res + "9"

        self.result.configure(text = self.res)

        self.root.update()

        

    def addzero(self):

        self.res = self.res + "0"

        self.result.configure(text = self.res)

        self.root.update()

                

    def addspot(self):

        if len(self.res) != 0 :

            if self.spott == False:

                self.spott = True

                self.res = self.res + "."

                self.result.configure(text = self.res)

            self.root.update()

            

    def clear(self):

        self.res = ""

        self.spott = False

        self.result.configure(text = self.res)

        self.root.update()

        

    def backspace(self):

        if eq(self.res[len(self.res)-1:],".") == True:

            self.spott = False

        self.res = self.res[:len(self.res)-1]

        self.result.configure(text = self.res)

        self.root.update()

        

    def enter(self):

        if eq(self.res,"") == False:

            if float(self.res) >= 0 and float(self.res) <= 400:

                globall.result = str(float(self.res))
		print("====",globall.result)
      		self.root.destroy() 
		self.root.quit()



            else:

                print("not good")

                self.root.wm_attributes("-topmost", 1)

                self.root.focus_force()

                tkMessageBox.showerror("Error", "Please insert values from 0 to 400Hertz")

                self.root.wm_attributes("-topmost", 1)

                self.root.focus_force()

        else:

            self.root.wm_attributes("-topmost", 1)

            self.root.focus_force()

            tkMessageBox.showerror("Error", "Please insert any values from 0 to 400Hertz")

            self.root.wm_attributes("-topmost", 1)

            self.root.focus_force()

    def escape(self):

        self.root.destroy()

        self.root.quit()

        
