import Tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
image2 =Image.open('CoolingTower.png')
background_image=root.PhotoImage(image2)
background_label = root.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(screen_width,screen_height)
root.attributes("-fullscreen", True)
root.mainloop()
