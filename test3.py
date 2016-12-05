from PIL import ImageTk
import PIL.Image
import Tkinter as tk
root = tk.Tk()
photo = ImageTk.PhotoImage(PIL.Image.open('CoolingTower.png'))
labimg = tk.Label(root,image=photo)
labimg.image = photo
labimg.place(x=-50,y=-20)
rpm1 = tk.Label(root, text = 'RPM:',font = ("Courier",20))
rpm1.place(x=50,y=20)
rpm2 = tk.Label(root, text = '123',font = ("Courier",20))
rpm2.place(x=120,y=20)
pwm1 = tk.Label(root, text = 'Watt:',font = ("Courier",20))
pwm1.place(x=500,y=360)
pwm2 = tk.Label(root, text = '123',font = ("Courier",20))
pwm2.place(x=580,y=360)
iwt1 = tk.Label(root, text = 'IWT:',font = ("Courier",20))
iwt1.place(x=600,y=60)
iwt2 = tk.Label(root, text = '123',font = ("Courier",20))
iwt2.place(x=680,y=60)
owt1 = tk.Label(root, text = 'OWT:',font = ("Courier",20))
owt1.place(x=70,y=360)
owt2 = tk.Label(root, text = '123',font = ("Courier",20))
owt2.place(x=130,y=360)
iwt1 = tk.Label(root, text = 'AT:',font = ("Courier",20))
iwt1.place(x=600,y=220)
iwt2 = tk.Label(root, text = '123',font = ("Courier",20))
iwt2.place(x=680,y=220)
owt1 = tk.Label(root, text = 'AH:',font = ("Courier",20))
owt1.place(x=600,y=250)
owt2 = tk.Label(root, text = '123',font = ("Courier",20))
owt2.place(x=680,y=250)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(screen_width,screen_height)
root.attributes("-fullscreen", True)
root.mainloop()
