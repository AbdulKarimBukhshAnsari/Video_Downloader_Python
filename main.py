#importing all the modules
from tkinter import *

from PIL import Image,ImageTk















root =Tk()
bg_image = Image.open("intro_page.png")
screen_width = root.winfo_screenwidth()   #finding the width and height of the screen so that the tkinter window would be adjustable accprding to your screen 
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
#resizing the image 
resized_bg_image = bg_image.resize((screen_width,screen_height))
resized_bg_image_tk = ImageTk.PhotoImage(resized_bg_image)

#making label and setting the image on window
bg_image_label = Label(root,image=resized_bg_image_tk)
bg_image_label.place(relwidth=1,relheight=1)

#importing button image 
start_button = Image.open("start_button.png")
start_button_image = ImageTk.PhotoImage(start_button)
intro_button = Button(root,image=start_button_image,borderwidth=0)
intro_button.place(x=610,y=470)



root.mainloop()