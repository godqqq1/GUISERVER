from select import *
from PIL import ImageTk

import PIL.Image

import globall

import threading

import touch2

from operator import eq

import tkMessageBox

import Tkinter as tk
import RPi.GPIO as GPIO
import sys

import socket
import serial

import time


class M1(threading.Thread):
    def run(self):
        HOST = '192.168.8.200'
        PORT = 50007
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST,PORT))
        s.listen(1)
        while 1:
            conn, addr = s.accept()
            try:
                data = conn.recv(50)
                if data:
                        print('Connected by ',addr ,' Client : ', data)
                        try:
                            if(data[:4] == 'rtd!'):
                                globall.rtd1 = str(round(float(data[4:]),1))+' C'
                                #v3.set(str(round(float(data[4:]),1))+' C')
                            elif(data[:4] == 'hrz!'):
                                globall.hrz = str(round(((round(float(data[4:]),1))/400*41),1))+' Hz'
                                #v1.set(str(round(float(data[4:]),1))+' RPM')
                            elif(data[:4] == 'am1!'):
                                globall.outem = str(round(float(data[4:]),1))+' C'
                                #v5.set(str(round(float(data[4:]),1))+' C')
                            elif(data[:4] == 'am2!'):
                                globall.outhm = str(round(float(data[4:]),1))+' %'
                                #v6.set(str(round(float(data[4:]),1))+' %')
                            elif(data[:4] == 'pow!' and data.find('end!') != -1):
                                globall.volt = str(round(float(data[4:data.find('end!')]),1))+' V'
                                #v2.set(str(round(float(data[4:data.find('end!')]),1))+' V')
                        except Exception as e:
                                print('')
                else:
                    conn.close()
            except socket.timeout:
                print("timeout")
        conn.close()


class M2(threading.Thread):
    
    def run(self):
        def fanlrr():
            if(vat.get() == 0):
                globall.fanlr = False
            else:
                globall.fanlr = True
        def tuch3():
            if(globall.fanonoff == False):
                Fanonoff2.configure(image=photo2)
                globall.fanonoff = True
                globall.flag3 = True
            else:
                Fanonoff2.configure(image=photo3)
                globall.fanonoff = False
                globall.flag3 = True
        def tuch2():
            if globall.dbck == False:
                    globall.dbck = True
                    m4 = M4()
                    m4.put_back()
                    m4.root.mainloop()
        def longclickon(event):
            if(event.x >= 20 and event.x < 138):
                if(event.y >= 273 and event.y <= 310):
                   tuch2()
            if(event.x >= 11 and event.x < 77):
                if(event.y >= 352 and event.y <= 390):
                    ddop.configure(image = photo6)
                    print("damp1t")
                    globall.damcom = "damp1t"
                    globall.flag2 = True
            if(event.x >= 77 and event.x < 146):
                if(event.y >= 352 and event.y <= 390):
                    ddcl.configure(image = photo7)
                    print("damp2t")
                    globall.damcom = "damp2t"
                    globall.flag2 = True
            if(event.x >= 11 and event.x < 77):
                if(event.y >= 429 and event.y <= 467):
                    dwop.configure(image = photo6)
                    print("damp3t")
                    globall.damcom ="damp3t"
                    globall.flag2 = True
            if(event.x >= 77 and event.x < 146):
                if(event.y >= 429 and event.y <= 467):
                    dwcl.configure(image = photo7)
                    print("damp4t")
                    globall.damcom = "damp4t"
                    globall.flag2 = True
        def longclickoff(event):            
            if(event.x >= 11 and event.x < 77):
                if(event.y >= 352 and event.y <= 390):
                    ddop.configure(image = photo4)
                    ddcl.configure(image = photo5)
                    dwop.configure(image = photo4)
                    dwcl.configure(image = photo5)
                    print("damp5t")
                    globall.damcom = "damp5t"
                    globall.flag2 = True
            if(event.x >= 77 and event.x < 146):
                if(event.y >= 352 and event.y <= 390):
                    ddop.configure(image = photo4)
                    ddcl.configure(image = photo5)
                    dwop.configure(image = photo4)
                    dwcl.configure(image = photo5)
                    print("damp5t")
                    globall.damcom = "damp5t"
                    globall.flag2 = True
            if(event.x >= 11 and event.x < 77):
                if(event.y >= 429 and event.y <= 467):
                    ddop.configure(image = photo4)
                    ddcl.configure(image = photo5)
                    dwop.configure(image = photo4)
                    dwcl.configure(image = photo5)
                    print("damp5t")
                    globall.damcom = "damp5t"
                    globall.flag2 = True
            if(event.x >= 77 and event.x < 146):
                if(event.y >= 429 and event.y <= 467):
                    ddop.configure(image = photo4)
                    ddcl.configure(image = photo5)
                    dwop.configure(image = photo4)
                    dwcl.configure(image = photo5)
                    print("damp5t")
                    globall.damcom = "damp5t"
                    globall.flag2 = True
        
        def clickk(event):
            tuch2()
        def ddo(event):
            ddop.configure(image = photo6)
            print("damp1t")
            globall.damcom = "damp1t"
            globall.flag2 = True
        def ddc(event):
            ddcl.configure(image = photo7)
            print("damp2t")
            globall.damcom = "damp2t"
            globall.flag2 = True
        def dwo(event):
            dwop.configure(image = photo6)
            print("damp3t")
            globall.damcom ="damp3t"
            globall.flag2 = True
        def dwc(event):
            dwcl.configure(image = photo7)
            print("damp4t")
            globall.damcom = "damp4t"
            globall.flag2 = True
        def ddd(event):
            ddop.configure(image = photo4)
            ddcl.configure(image = photo5)
            dwop.configure(image = photo4)
            dwcl.configure(image = photo5)
            print("damp5t")
            globall.damcom = "damp5t"
            globall.flag2 = True
        root = tk.Tk()
        photo = ImageTk.PhotoImage(PIL.Image.open('CoolingTower.png'))
        photo2 = ImageTk.PhotoImage(PIL.Image.open('on_button.png'))
        photo3 = ImageTk.PhotoImage(PIL.Image.open('off_button.png'))
        photo4 = ImageTk.PhotoImage(PIL.Image.open('open.png'))
        photo5 = ImageTk.PhotoImage(PIL.Image.open('close.png'))
        photo6 = ImageTk.PhotoImage(PIL.Image.open('openg.png'))
        photo7 = ImageTk.PhotoImage(PIL.Image.open('closeg.png'))
        labimg = tk.Label(root,image=photo,background="black")
        labimg.image = photo
        labimg.grid(row=0,column=0)

        iwt = tk.StringVar()
        hz = tk.StringVar()

        owt = tk.StringVar()

        rpm = tk.StringVar()

        outem = tk.StringVar()

        outhm = tk.StringVar()
        
        voltt = tk.StringVar()
        
        ampt = tk.StringVar()
        
        wattt = tk.StringVar()
        vat = tk.IntVar()
        
        Fanonoff2 = tk.Button(root,command=tuch3,image=photo3,font = ("Courier",10,"bold"))

        Fanonoff2.place(x=27,y=93,width=100,height=30)

        watpow2 = tk.Label(root,textvariable=hz,font = ("Courier",8,"bold"),background='white')
        watpow2.place(x=21,y=289,width=110,height=15)

        iwt2 = tk.Label(root, textvariable=iwt,font = ("Courier",10,"bold"),background='white')

        iwt2.place(x=668,y=129,width=110,height=15)

        owt2 = tk.Label(root, textvariable=owt,font = ("Courier",10,"bold"),background='white')

        owt2.place(x=668,y=220,width=110,height=15)

        rpm2 = tk.Label(root, textvariable=rpm,font = ("Courier",10,"bold"),background='white')

        rpm2.place(x=668,y=40,width=110,height=15)

            #pwm2 = tk.Label(root, textvariable=v2,font = ("Courier",10,"bold"),background='white')

            #pwm2.place(x=670,y=305,width=100,height=20)

        iwt4 = tk.Label(root, textvariable=outem,font = ("Courier",10,"bold"),background='white')

        iwt4.place(x=668,y=307,width=110,height=15)

        owt4 = tk.Label(root, textvariable=outhm,font = ("Courier",10,"bold"),background='white')

        owt4.place(x=668,y=397,width=110,height=15)

        voltl = tk.Label(root, textvariable=voltt,font = ("Courier",10,"bold"),background='white')

        voltl.place(x=21,y=170,width=110,height=15)

        ampl = tk.Label(root, textvariable=ampt,font = ("Courier",10,"bold"),background='white')

        ampl.place(x=21,y=190,width=110,height=15)

        wattl = tk.Label(root, textvariable=wattt,font = ("Courier",10,"bold"),background='white')

        wattl.place(x=21,y=210,width=110,height=15)
        root.bind("<Button-1>",longclickon)
        root.bind("<ButtonRelease-1>",longclickoff)


        ddop = tk.Label(root,background='white',image=photo4)
        ddop.bind("<Button-1>",ddo)
        ddop.bind("<ButtonRelease-1>",ddd)
        ddop.place(x=21,y=362,width=55,height=18)

        ddcl = tk.Label(root,background='white',image=photo5)
        ddcl.place(x=81,y=362,width=55,height=18)
        ddcl.bind("<Button-1>",ddc)
        ddcl.bind("<ButtonRelease-1>",ddd)

        dwop = tk.Label(root,background='white',image=photo4)
        dwop.place(x=21,y=439,width=55,height=18)
        dwop.bind("<Button-1>",dwo)
        dwop.bind("<ButtonRelease-1>",ddd)

        dwcl = tk.Label(root,background='white',image=photo5)
        dwcl.place(x=81,y=439,width=55,height=18)
        dwcl.bind("<Button-1>",dwc)
        dwcl.bind("<ButtonRelease-1>",ddd)


        iwt.set('Not Connected')

        owt.set('Not Connected')

        rpm.set('Not Connected')
        hz.set('0 Hz')

        outem.set('Not Connected')

        outhm.set('Not Connected')

        voltt.set('Not Connected')

        ampt.set('Not Connected')

        wattt.set('Not Connected')

        screen_width = root.winfo_screenwidth()

        screen_height = root.winfo_screenheight()

        print(screen_width,screen_height)

        root.attributes("-fullscreen", True)

        root.geometry("800x480")
       
        while 1 :
            if (float(globall.volter) > 1):
                Fanonoff2.configure(image=photo2)
            else:
                Fanonoff2.configure(image=photo3)
            hz.set(globall.hrz)
            iwt.set('32 C')
            owt.set('27 C')
            rpm.set(str(round(((float(globall.volter)/380)*350),1))+ " RPM")
            outem.set(globall.outem)
            outhm.set(globall.outhm)
            tmp2 = str(globall.volter)
            voltt.set(tmp2 + " V")
            tmp3 = str(globall.amper)
            ampt.set(tmp3 +" A")
            tmp = str(round((float(globall.volter) * float(globall.amper) * 1.75/1000),1))
            wattt.set(tmp +" kW")
            root.update()
class M3(threading.Thread):
    def run(self):
        try:
            ser = serial.Serial('/dev/ttyACM0',115200,timeout=3)
            globall.p1 = 1
        except:
            print("ser error")
        """
        try:
            ser2 = serial.Serial('/dev/ttyACM1',115200,timeout=3)
            globall.p2 = 1
        except:
            print("ser2 error")
        try:
            ser3 = serial.Serial('/dev/ttyACM2',115200,timeout=3)
            globall.p3 = 1
        except:
            print("ser3 error")
        try:
            ser4 = serial.Serial('/dev/ttyUSB0',115200,timeout=3)
            globall.p4 = 1
        except:
            print("ser4 error")
        try:
            ser5 = serial.Serial('/dev/ttyUSB1',115200,timeout=3)
            globall.p5 = 1
        except:
            print("ser5 error")
            """
        while 1:
            if(globall.p1 == 1):
                if(globall.flag3 == True):
                    if(globall.fanonoff == True):
                        if(globall.fanlr == False):
                            ser.writelines("morr1t")
                            globall.flag3 = False
                        else:
                            ser.writelines("morr2t")
                            globall.flag3 = False
                    else:
                        ser.writelines("morr3t")
                        globall.flag3 = False
                if(globall.flag1 == True):
                    print("shot")
                    ser.writelines(globall.result+"t")
                    globall.flag1 = False
                if(globall.flag2 == True):
                    ser.writelines(globall.damcom)
                    globall.flag2 = False
                tar = ser.readline()
                
                try:
                    if(tar[:6].find('volter') >= 0):
                        
                        globall.volter = float(tar[6:])
                    if(tar[:6].find('ampper')>= 0):
                        globall.amper = float(tar[6:])
                    if(tar[:6].find('watter')>= 0):
                        globall.watt = float(tar[6:])
                    
                except Exception:
                    print("")
            if(globall.p2 == 1):
                
                if(globall.flag3 == True):
                    if(globall.fanonoff == True):
                        if(globall.fanlr == False):
                            ser2.writelines("morr1t")
                            globall.flag3 = False
                        else:
                            ser2.writelines("morr2t")
                            globall.flag3 = False
                    else:
                        ser2.writelines("morr3t")
                        globall.flag3 = False
                if(globall.flag1 == True):
                    print("shot")
                    ser2.writelines(globall.result+"t")
                    globall.flag1 = False
                if(globall.flag2 == True):
                    ser2.writelines(globall.damcom)
                    globall.flag2 = False
                tar = ser2.readline()
                
                try:
                    if(tar[:6].find('volter') >= 0):
                        
                        globall.volter = float(tar[6:])
                    if(tar[:6].find('ampper')>= 0):
                        globall.amper = float(tar[6:])
                    if(tar[:6].find('watter')>= 0):
                        globall.watt = float(tar[6:])
                    
                except Exception:
                    print("")
            if(globall.p3 == 1):
                if(globall.flag3 == True):
                    if(globall.fanonoff == True):
                        if(globall.fanlr == False):
                            ser3.writelines("morr1t")
                            globall.flag3 = False
                        else:
                            ser3.writelines("morr2t")
                            globall.flag3 = False
                    else:
                        ser3.writelines("morr3t")
                        globall.flag3 = False
                if(globall.flag1 == True):
                    print("shot")
                    ser3.writelines(globall.result+"t")
                    globall.flag1 = False
                if(globall.flag2 == True):
                    ser3.writelines(globall.damcom)
                    globall.flag2 = False
                tar = ser3.readline()
                
                try:
                    if(tar[:6].find('volter') >= 0):
                        
                        globall.volter = float(tar[6:])
                    if(tar[:6].find('ampper')>= 0):
                        globall.amper = float(tar[6:])
                    if(tar[:6].find('watter')>= 0):
                        globall.watt = float(tar[6:])
                    
                except Exception:
                    print("")
            if(globall.p4 == 1):
                if(globall.flag3 == True):
                    if(globall.fanonoff == True):
                        if(globall.fanlr == False):
                            ser4.writelines("morr1t")
                            globall.flag3 = False
                        else:
                            ser4.writelines("morr2t")
                            globall.flag3 = False
                    else:
                        ser4.writelines("morr3t")
                        globall.flag3 = False
                if(globall.flag1 == True):
                    print("shot")
                    ser4.writelines(globall.result+"t")
                    globall.flag1 = False
                if(globall.flag2 == True):
                    ser4.writelines(globall.damcom)
                    globall.flag2 = False
                tar = ser4.readline()
                
                try:
                    if(tar[:6].find('volter') >= 0):
                        
                        globall.volter = float(tar[6:])
                    if(tar[:6].find('ampper')>= 0):
                        globall.amper = float(tar[6:])
                    if(tar[:6].find('watter')>= 0):
                        globall.watt = float(tar[6:])
                    
                except Exception:
                    print("")
            if(globall.p5 == 1):
                if(globall.flag3 == True):
                    if(globall.fanonoff == True):
                        if(globall.fanlr == False):
                            ser5.writelines("morr1t")
                            globall.flag3 = False
                        else:
                            ser5.writelines("morr2t")
                            globall.flag3 = False
                    else:
                        ser5.writelines("morr3t")
                        globall.flag3 = False
                if(globall.flag1 == True):
                    print("shot")
                    ser5.writelines(globall.result+"t")
                    globall.flag1 = False
                if(globall.flag2 == True):
                    ser5.writelines(globall.damcom)
                    globall.flag2 = False
                tar = ser5.readline()
                
                try:
                    if(tar[:6].find('volter') >= 0):
                        
                        globall.volter = float(tar[6:])
                    if(tar[:6].find('ampper')>= 0):
                        globall.amper = float(tar[6:])
                    if(tar[:6].find('watter')>= 0):
                        globall.watt = float(tar[6:])
                    
                except Exception:
                    print("")
class M4():
    global root
    def __init__(self):
        global res
        res = ""
        

        global result
        global spott
        spott = False
        def addone():
            global res
            res = res + "1"

            result.configure(text = res)

            root.update()

            

        def addtwo():
            global res

            res = res + "2"

            result.configure(text = res)

            root.update()

            

        def addthree():
            global res

            res = res + "3"

            result.configure(text = res)

            root.update()

            

        def addfour():
            global res

            res = res + "4"

            result.configure(text = res)

            root.update()

            

        def addfive():
            global res

            res = res + "5"

            result.configure(text = res)

            root.update()

            

        def addsix():
            global res

            res = res + "6"
            
            result.configure(text = res)    

            root.update()

            

        def addseven():
            global res

            res = res + "7"

            result.configure(text = res)

            root.update()

            

        def addeight():
            global res

            res = res + "8"

            result.configure(text = res)

            root.update()

            

        def addnine():
            global res

            res = res + "9"

            result.configure(text = res)

            root.update()

            

        def addzero():
            global res

            res = res + "0"

            result.configure(text = res)

            root.update()

                    

        def addspot():
            global res
            global spott

            if len(res) != 0 :

                if spott == False:

                    spott = True

                    res = res + "."

                    result.configure(text = res)

                root.update()

                

        def clear():
            global res
            global spott

            res = ""

            spott = False

            result.configure(text = res)

            root.update()

            

        def backspace():
            global res
            global spott

            if eq(res[len(res)-1:],".") == True:

                spott = False

            res = res[:len(res)-1]

            result.configure(text = res)

            root.update()

            

        def enter():
            global res

            if eq(res,"") == False:

                if float(res) >= 0 and float(res) <= 400:

                    globall.result = str(float(res))
                    print("====",globall.result)
                    globall.dbck = False
                    globall.flag1 = True
                    root.destroy() 
                    root.quit()



                else:

                    print("not good")

                    root.wm_attributes("-topmost", 1)

                    root.focus_force()

                    tkMessageBox.showerror("Error", "Please insert values from 0 to 400Hertz")

                    root.wm_attributes("-topmost", 1)

                    root.focus_force()

            else:

                root.wm_attributes("-topmost", 1)

                root.focus_force()

                tkMessageBox.showerror("Error", "Please insert any values from 0 to 400Hertz")

                root.wm_attributes("-topmost", 1)

                root.focus_force()

        def escape():

            root.destroy()
            root.quit()
        
        def some():
            print("zz")
        def put_back(self):
            self.root.lower()
            self.root.after(100,self.put_back())
        
        root = tk.Tk()
        root.overrideredirect(True)
        root.protocol('WM_DELETE_WINDOW',some)
        root.geometry("300x245+270+150")
        root.configure(background="RoyalBlue3")

        root.resizable(False, False)

        root.title("Set")
        dummy0 = tk.Label(root,text="      ",background="RoyalBlue3")

        dummy0.grid(row=0,column=0)

        result = tk.Label(root, text=res,background = "white",width=14,anchor=tk.E)  # title label

        result.grid(row=1, column=1,columnspan=3, sticky = tk.W)  # merge cell

        dummy1 = tk.Label(root,text="      ",background="RoyalBlue3")

        dummy1.grid(row=2,column=0)

        one = tk.Button(root,text="1",width=5,height=2,command=addone,background="SteelBlue2",foreground="white")

        one.grid(row=3,column=0, sticky = tk.W, padx = 3,pady = 2)

        two = tk.Button(root,text="2",width=5,height=2,command=addtwo,background="SteelBlue2",foreground="white")

        two.grid(row=3,column=1, sticky = tk.W, padx = 3,pady = 2)

        three = tk.Button(root,text="3",width=5,height=2,command=addthree,background="SteelBlue2",foreground="white")

        three.grid(row=3,column=2, sticky = tk.W, padx = 3,pady = 2)

        esc = tk.Button(root,text="ESC",width=5,height=2,command=escape,background="SteelBlue2",foreground="white")

        esc.grid(row=3,column=3, sticky = tk.W, padx = 3,pady = 2)

        four = tk.Button(root,text="4",width=5,height=2,command=addfour,background="SteelBlue2",foreground="white")

        four.grid(row=4,column=0, sticky = tk.W, padx = 3,pady = 2)

        five = tk.Button(root,text="5",width=5,height=2,command=addfive,background="SteelBlue2",foreground="white")

        five.grid(row=4,column=1, sticky = tk.W, padx = 3,pady = 2)

        six = tk.Button(root,text="6",width=5,height=2,command=addsix,background="SteelBlue2",foreground="white")

        six.grid(row=4,column=2, sticky = tk.W, padx = 3,pady = 2)

        clr = tk.Button(root,text="CLR",width=5,height=2,command=clear,background="SteelBlue2",foreground="white")

        clr.grid(row=4,column=3, sticky = tk.W, padx = 3,pady = 2)

        seven = tk.Button(root,text="7",width=5,height=2,command=addseven,background="SteelBlue2",foreground="white")

        seven.grid(row=5,column=0, sticky = tk.W, padx = 3,pady = 2)

        eight = tk.Button(root,text="8",width=5,height=2,command=addeight,background="SteelBlue2",foreground="white")

        eight.grid(row=5,column=1, sticky = tk.W, padx = 3,pady = 2)

        nine = tk.Button(root,text="9",width=5,height=2,command=addnine,background="SteelBlue2",foreground="white")

        nine.grid(row=5,column=2, sticky = tk.W, padx = 3,pady = 2) 

        bs = tk.Button(root,text="Back",width=5,height=2,command=backspace,background="SteelBlue2",foreground="white")

        bs.grid(row=5,column=3, sticky = tk.W, padx = 3,pady = 2) 

        dummy2 = tk.Button(root,text="",width=5,height=2,background="SteelBlue2",foreground="white")

        dummy2.grid(row=6,column=0, sticky = tk.W, padx = 3,pady = 2)

        zero = tk.Button(root,text="0",width=5,height=2,command=addzero,background="SteelBlue2",foreground="white")

        zero.grid(row=6,column=1, sticky = tk.W, padx = 3,pady = 2)

        spot = tk.Button(root,text=".",width=5,height=2,command=addspot,background="SteelBlue2",foreground="white")

        spot.grid(row=6,column=2, sticky = tk.W, padx = 3,pady = 2)    

        ent = tk.Button(root,text="ENT",width=5,height=2,command=enter,background="SteelBlue2",foreground="white")

        ent.grid(row=6,column=3, sticky = tk.W, padx = 3,pady = 2)    
        

            
        
m1 = M1()
m1.start()
m2 = M2()
m2.start()
m3 = M3()
m3.start()
