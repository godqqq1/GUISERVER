from select import *
from PIL import ImageTk
import PIL.Image
import Tkinter as tk
import sys
import socket

HOST = '192.168.1.101'
#HOST = '192.168.1.24'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
timer = 10
root = tk.Tk()
photo = ImageTk.PhotoImage(PIL.Image.open('CoolingTower.png'))
labimg = tk.Label(root,image=photo)
labimg.image = photo
labimg.place(x=0,y=0)
v1 = tk.StringVar()
v2 = tk.StringVar()
v3 = tk.StringVar()
v4 = tk.StringVar()
v5 = tk.StringVar()
v6 = tk.StringVar()
iwt01 = tk.Label(root, text = '1.',font = ("Courier",20))
iwt01.place(x=544,y=0)
iwt1 = tk.Label(root, text = 'Inlet Water',font = ("Courier",10))
iwt1.place(x=584,y=0)
iwt11 = tk.Label(root, text = 'Temperature',font = ("Courier",10))
iwt11.place(x=584,y=14)
iwt2 = tk.Label(root, textvariable=v3,font = ("Courier",20))
iwt2.place(x=694,y=0)
owt01 = tk.Label(root, text = '2.',font = ("Courier",20))
owt01.place(x=544,y=50)
owt1 = tk.Label(root, text = 'Outlet Water',font = ("Courier",10))
owt1.place(x=584,y=50)
owt11 = tk.Label(root, text = 'Temperature',font = ("Courier",10))
owt11.place(x=584,y=64)
owt2 = tk.Label(root, textvariable=v4,font = ("Courier",20))
owt2.place(x=694,y=50)
rpm1 = tk.Label(root, text = '3. RPM',font = ("Courier",20))
rpm1.place(x=544,y=100)
rpm2 = tk.Label(root, textvariable=v1,font = ("Courier",20))
rpm2.place(x=694,y=100)
pwm01 = tk.Label(root, text = '4.',font = ("Courier",20))
pwm01.place(x=544,y=150)
pwm1 = tk.Label(root, text = '  Motor',font = ("Courier",11))
pwm1.place(x=584,y=150)
pwm11 = tk.Label(root, text = '  Power',font = ("Courier",11))
pwm11.place(x=584,y=167)
pwm2 = tk.Label(root, textvariable=v2,font = ("Courier",20))
pwm2.place(x=694,y=150)
iwt3 = tk.Label(root, text = '5.',font = ("Courier",20))
iwt3.place(x=544,y=200)
iwt3 = tk.Label(root, text = '  Ambient',font = ("Courier",10))
iwt3.place(x=584,y=200)
iwt3 = tk.Label(root, text = 'Temperature',font = ("Courier",10))
iwt3.place(x=584,y=214)
iwt4 = tk.Label(root, textvariable=v5,font = ("Courier",20))
iwt4.place(x=694,y=200)
owt03 = tk.Label(root, text = '5.:',font = ("Courier",20))
owt03.place(x=544,y=250)
owt3 = tk.Label(root, text = '  Ambient',font = ("Courier",10))
owt3.place(x=584,y=245)
owt3 = tk.Label(root, text = '  Relative',font = ("Courier",10))
owt3.place(x=584,y=259)
owt33 = tk.Label(root, text = 'Temperature',font = ("Courier",10))
owt33.place(x=584,y=273)
owt4 = tk.Label(root, textvariable=v6,font = ("Courier",20))
owt4.place(x=694,y=250)
v1.set('123')
v2.set('123')
v3.set('123')
v4.set('123')
v5.set('123')
v6.set('123')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(screen_width,screen_height)
root.attributes("-fullscreen", True)
root.geometry("800x480")
root.update()
while 1:
	print(timer)
	conn, addr = s.accept()
	data = conn.recv(1024)
	if data:
		print('Connected by ',addr ,' Client : ', data)
    		print(data[:4])
    		if(data[:4] == 'rtd!'):
        		v3.set(round(float(data[4:]),1))
		elif(data[:4] == 'rpm!'):
			v1.set(round(float(data[4:]),1))
		elif(data[:4] == 'am1!'):
			v5.set(round(float(data[4:]),1))
		elif(data[:4] == 'am2!'):
			v6.set(round(float(data[4:]),1))
		elif(data[:4] == 'wat!'):
			v2.set(round(float(data[4:]),1))
	else:
    		conn.close()
	try:
    		conn.sendall('abc\r')
	except Exception as e:
    		conn.close()
    		print("Lost Conn")
	#root.mainloop()
	root.update()
conn.close()


