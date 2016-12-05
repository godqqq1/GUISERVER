from select import *
from PIL import ImageTk
import PIL.Image
import Tkinter as tk
import sys
import socket

HOST = '192.168.8.200'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
timer = 10
root = tk.Tk()
photo = ImageTk.PhotoImage(PIL.Image.open('CoolingTower.png'))
labimg = tk.Label(root,image=photo)
labimg.image = photo
labimg.place(x=-50,y=-20)
v1 = tk.StringVar()
v2 = tk.StringVar()
v3 = tk.StringVar()
v4 = tk.StringVar()
v5 = tk.StringVar()
v6 = tk.StringVar()
rpm1 = tk.Label(root, text = 'RPM:',font = ("Courier",20))
rpm1.place(x=50,y=20)
rpm2 = tk.Label(root, textvariable=v1,font = ("Courier",20))
rpm2.place(x=120,y=20)
pwm1 = tk.Label(root, text = 'Watt:',font = ("Courier",20))
pwm1.place(x=500,y=360)
pwm2 = tk.Label(root, textvariable=v2,font = ("Courier",20))
pwm2.place(x=580,y=360)
iwt1 = tk.Label(root, text = 'IWT:',font = ("Courier",20))
iwt1.place(x=600,y=60)
iwt2 = tk.Label(root, textvariable=v3,font = ("Courier",20))
iwt2.place(x=680,y=60)
owt1 = tk.Label(root, text = 'OWT:',font = ("Courier",20))
owt1.place(x=70,y=360)
owt2 = tk.Label(root, textvariable=v4,font = ("Courier",20))
owt2.place(x=130,y=360)
iwt3 = tk.Label(root, text = 'AT:',font = ("Courier",20))
iwt3.place(x=600,y=220)
iwt4 = tk.Label(root, textvariable=v5,font = ("Courier",20))
iwt4.place(x=680,y=220)
owt3 = tk.Label(root, text = 'AH:',font = ("Courier",20))
owt3.place(x=600,y=250)
owt4 = tk.Label(root, textvariable=v6,font = ("Courier",20))
owt4.place(x=680,y=250)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(screen_width,screen_height)
root.attributes("-fullscreen", True)
while 1:
	print(timer)
	conn, addr = s.accept()
	data = conn.recv(1024)
	if data:
		print('Connected by ',addr ,' Client : ', data)
    		print(data[:4])
    	if(data[:4] == 'rtd!'):
        	v1.set(data[4:])
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


