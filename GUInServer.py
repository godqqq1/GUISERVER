from select import *

from PIL import ImageTk

import PIL.Image

import globall

import threading

import touch2

import Tkinter as tk
import RPi.GPIO as GPIO
import sys

import socket
import serial

import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, True)
HOST = '192.168.8.200'

#HOST = '192.168.1.24'

PORT = 50007
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
try:
    ser = serial.Serial('/dev/ttyACM0',9600)
    p1 = 1
except:
    print("ser error")
try:
    ser2 = serial.Serial('/dev/ttyACM1',9600)
    p2 = 1
except:
    print("ser2 error")
try:
    ser3 = serial.Serial('/dev/ttyACM2',9600)
    p3 = 1
except:
    print("ser3 error")
try:
    ser4 = serial.Serial('/dev/ttyUSB0',9600)
    p4 = 1
except:
    print("ser4 error")
try:
    ser5 = serial.Serial('/dev/ttyUSB1',9600)
    p5 = 1
except:
    print("ser5 error")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST,PORT))

s.listen(1)

timer = 10

        

root = tk.Tk()
global tc
fanonoff = False
dbck = False

photo = ImageTk.PhotoImage(PIL.Image.open('CoolingTower.png'))
photo2 = ImageTk.PhotoImage(PIL.Image.open('on.png'))
photo3 = ImageTk.PhotoImage(PIL.Image.open('off.png'))
photo4 = ImageTk.PhotoImage(PIL.Image.open('open.png'))
photo5 = ImageTk.PhotoImage(PIL.Image.open('close.png'))
photo6 = ImageTk.PhotoImage(PIL.Image.open('openg.png'))
photo7 = ImageTk.PhotoImage(PIL.Image.open('closeg.png'))
labimg = tk.Label(root,image=photo,background="black")

def tuch3():
    global fanonoff
    if(fanonoff == False):
        Fanonoff2.configure(image=photo2)
        GPIO.output(18, False)
        fanonoff = True
    else:
        Fanonoff2.configure(image=photo3)
        GPIO.output(18, True)
        fanonoff = False
def tuch4(depp):
    if(p1 == 1):
        ser.writelines(depp)
    if(p2 == 1):
        ser2.writelines(depp)
    if(p3 == 1):
        ser3.writelines(depp)
    if(p4 == 1):
        ser4.writelines(depp)
    if(p5 == 1):
        ser5.writelines(depp)
		
def tuch2():
	global tc
	global dbck
	if dbck == False:
		dbck = True
        	tc = touch2.touch2()
        	watpow2.configure(text = globall.result+" Hz")
        	if(p1 == 1):
                    ser.writelines(globall.result)
        	if(p2 == 1):
                    ser2.writelines(globall.result)
        	if(p3 == 1):
                    ser3.writelines(globall.result)
        	if(p4 == 1):
                    ser4.writelines(globall.result)
        	if(p5 == 1):
                    ser5.writelines(globall.result)
		dbck = False
def clickk(event):
    tuch2()
def ddo(event):
    ddop.configure(image = photo6)
    print("damp1")
    tuch4("damp1")
def ddc(event):
    ddcl.configure(image = photo7)
    print("damp2")
    tuch4("damp2")
def dwo(event):
    dwop.configure(image = photo6)
    print("damp3")
    tuch4("damp3")
def dwc(event):
    dwcl.configure(image = photo7)
    print("damp4")
    tuch4("damp4")
def ddd(event):
    ddop.configure(image = photo4)
    ddcl.configure(image = photo5)
    dwop.configure(image = photo4)
    dwcl.configure(image = photo5)
    print("damp5")
    tuch4("damp5")
labimg.image = photo
labimg.grid(row=0,column=0)

v1 = tk.StringVar()

v2 = tk.StringVar()

v3 = tk.StringVar()

v4 = tk.StringVar()

v5 = tk.StringVar()

v6 = tk.StringVar()

v7 = tk.StringVar()

Fanonoff2 = tk.Button(root,command=tuch3,image=photo3,font = ("Courier",10,"bold"))

Fanonoff2.place(x=30,y=93,width=100,height=30)

watpow2 = tk.Label(root,text="0 Hz",font = ("Courier",8,"bold"),background='white')
watpow2.bind("<Button-1>",clickk)
watpow2.place(x=21,y=377,width=110,height=15)

iwt2 = tk.Label(root, textvariable=v3,font = ("Courier",10,"bold"),background='white')

iwt2.place(x=668,y=41,width=110,height=15)

owt2 = tk.Label(root, textvariable=v4,font = ("Courier",10,"bold"),background='white')

owt2.place(x=668,y=116,width=110,height=15)

rpm2 = tk.Label(root, textvariable=v1,font = ("Courier",10,"bold"),background='white')

rpm2.place(x=21,y=297,width=110,height=15)

#pwm2 = tk.Label(root, textvariable=v2,font = ("Courier",10,"bold"),background='white')

#pwm2.place(x=670,y=305,width=100,height=20)

iwt4 = tk.Label(root, textvariable=v5,font = ("Courier",10,"bold"),background='white')

iwt4.place(x=668,y=196,width=110,height=15)

owt4 = tk.Label(root, textvariable=v6,font = ("Courier",10,"bold"),background='white')

owt4.place(x=668,y=276,width=110,height=15)



ddop = tk.Label(root,background='white',image=photo4)
ddop.bind("<Button-1>",ddo)
ddop.bind("<ButtonRelease-1>",ddd)
ddop.place(x=665,y=355,width=55,height=18)

ddcl = tk.Label(root,background='white',image=photo5)
ddcl.place(x=726,y=355,width=55,height=18)
ddcl.bind("<Button-1>",ddc)
ddcl.bind("<ButtonRelease-1>",ddd)

dwop = tk.Label(root,background='white',image=photo4)
dwop.place(x=665,y=430,width=55,height=18)
dwop.bind("<Button-1>",dwo)
dwop.bind("<ButtonRelease-1>",ddd)

dwcl = tk.Label(root,background='white',image=photo5)
dwcl.place(x=726,y=430,width=55,height=18)
dwcl.bind("<Button-1>",dwc)
dwcl.bind("<ButtonRelease-1>",ddd)


v1.set('Not Connected')

v2.set('Not Connected')

v3.set('Not Connected')

v4.set('Not Connected')

v5.set('Not Connected')

v6.set('Not Connected')

v7.set('Not Connected')

screen_width = root.winfo_screenwidth()

screen_height = root.winfo_screenheight()

print(screen_width,screen_height)

root.attributes("-fullscreen", True)

root.geometry("800x480")

root.update()

while 1:

    print(timer)

    conn, addr = s.accept()
    conn.settimeout(0.1)
    try:
    	data = conn.recv(50)
    
    	if data:

        	print('Connected by ',addr ,' Client : ', data)

        	print(data[:4])

        	try:

	            if(data[:4] == 'rtd!'):

        	    	v3.set(str(round(float(data[4:]),1))+' C')

            	    elif(data[:4] == 'rpm!'):

                	v1.set(str(round(float(data[4:]),1))+' RPM')

            	    elif(data[:4] == 'am1!'):

                	v5.set(str(round(float(data[4:]),1))+' C')

            	    elif(data[:4] == 'am2!'):

                	v6.set(str(round(float(data[4:]),1))+' %')

            	    elif(data[:4] == 'pow!' and data.find('end!') != -1):

                	v2.set(str(round(float(data[4:data.find('end!')]),1))+' V')
                
        	except Exception as e:

            		print('')

        	try:

    			conn.sendall('abc\r')

        	except Exception as e:

        		conn.close()



    	else:

            conn.close()

    #root.mainloop()
    	root.update()
    except socket.timeout:
	root.update()
	print("timeout")
    nowww = ""
    if(p1 == 1):
        nowww = ser.readline()
    if(p2 == 1):
        nowww = ser2.readline()
    if(p3 == 1):
        nowww = ser3.readline()
    if(p4 == 1):
        nowww = ser4.readline()
    if(p5 == 1):
        nowww = ser5.readline()
#nowww
    print("noww = ",nowww)
conn.close()






