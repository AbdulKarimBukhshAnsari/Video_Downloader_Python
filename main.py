#importing all the modules
from tkinter import *

from PIL import Image,ImageTk












root =Tk()

screen_width = root.winfo_screenwidth()   #finding the width and height of the screen so that the tkinter window would be adjustable accprding to your screen 
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

"""Dealing with category page"""

#importing the background image
bg_image_2 = Image.open("category_page_1.png")

#resizing the image so it will be suitable for the window
resized_bg_image_2 = bg_image_2.resize((screen_width,screen_height))
resized_bg_image_2_tk = ImageTk.PhotoImage(resized_bg_image_2)

#Creating pages and dealing with the frame
page_2 = Frame(root)
page_2.place(relx=0,rely=0,relwidth=1,relheight=1)

#making label and setting the image on window
bg_image_label_2 = Label(page_2,image=resized_bg_image_2_tk)
bg_image_label_2.place(relwidth=1,relheight=1)

#importing youtube logo image and dealing with its size
youtube_logo = Image.open("youtube_logo.png")
youtube_logo_resize =youtube_logo.resize((180,120))
youtube_logo_resize_image = ImageTk.PhotoImage(youtube_logo_resize)

youtube_button = Button(page_2,image=youtube_logo_resize_image,borderwidth=0)
youtube_button.place(x=870,y=220)







"""Dealing with 1st page"""
#importing the background image
bg_image = Image.open("intro_page.png")

#resizing the image 
resized_bg_image = bg_image.resize((screen_width,screen_height))
resized_bg_image_tk = ImageTk.PhotoImage(resized_bg_image)

#creating 1st page as window
page_1 = Frame(root)
page_1.place(relx=0, rely=0, relwidth=1, relheight=1)  # Cover the entire root window

page_1.tkraise()
#making label and setting the image on window
bg_image_label = Label(page_1,image=resized_bg_image_tk)
bg_image_label.place(relwidth=1,relheight=1)

#importing button image 
start_button = Image.open("start_button.png")
start_button_image = ImageTk.PhotoImage(start_button)

#defining the button and setting its position.
intro_button = Button(page_1,image=start_button_image,borderwidth=0,command=lambda:page_2.tkraise())
intro_button.place(x=610,y=470)

"""End of the 1st page"""


root.mainloop()