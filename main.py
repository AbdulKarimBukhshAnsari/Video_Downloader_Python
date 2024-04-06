#importing all the modules
from tkinter import *

from PIL import Image,ImageTk



root =Tk()

screen_width = root.winfo_screenwidth()   #finding the width and height of the screen so that the tkinter window would be adjustable accprding to your screen 
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")


""""Dealing with the youtube page"""
#making the frame
page_3 = Frame(root)
page_3.place(relx=0,rely=0,relwidth=1,relheight=1)

#setting the background image

#importing the background image
bg_image_3 = Image.open(r"photos\youtube_page.png")

#resizing the image so it will be suitable for the window
resized_bg_image_3 = bg_image_3.resize((screen_width,screen_height))
resized_bg_image_3_tk = ImageTk.PhotoImage(resized_bg_image_3)

#making label and setting the image on window
bg_image_label_3 = Label(page_3,image=resized_bg_image_3_tk)
bg_image_label_3.place(relwidth=1,relheight=1)   # make sure that this picture will cover all the background

#making the widgets
url_label =Label(page_3,text="Enter the URL here:",font=("Arial",25,"bold"),bg="#FFF6EA")
url_label.pack(pady=("10p","3p"))
url_entry = Entry(page_3,width = 50,font=("Arial",18))
url_entry.pack(pady=("10p","5p"),ipady=5)
#making download button
#importing button image 
download_button = Image.open(r"photos\download_button.png")
download_button_final = download_button.resize((200,70))
download_button_image = ImageTk.PhotoImage(download_button_final)

#defining the button and setting its position.
download_button_button = Button(page_3,image=download_button_image,borderwidth=0)
download_button_button.pack(pady=("30p","5p"))























"""Dealing with category page"""

#importing the background image
bg_image_2 = Image.open(r"photos\category_page_1.png")

#resizing the image so it will be suitable for the window
resized_bg_image_2 = bg_image_2.resize((screen_width,screen_height))
resized_bg_image_2_tk = ImageTk.PhotoImage(resized_bg_image_2)

#Creating pages and dealing with the frame
page_2 = Frame(root)
page_2.place(relx=0,rely=0,relwidth=1,relheight=1)  # to cover the whole window

#making label and setting the image on window
bg_image_label_2 = Label(page_2,image=resized_bg_image_2_tk)
bg_image_label_2.place(relwidth=1,relheight=1)   # make sure that this picture will cover all the background

#importing youtube logo image and dealing with its size
youtube_logo = Image.open(r"photos\youtube_logo.png")
youtube_logo_resize =youtube_logo.resize((180,120))
youtube_logo_resize_image = ImageTk.PhotoImage(youtube_logo_resize)

youtube_button = Button(page_2,image=youtube_logo_resize_image,borderwidth=0,command =lambda: page_3.tkraise())
youtube_button.place(x=870,y=220)

#importing facebook logo and image dealing with its size
facebook_logo = Image.open(r"photos\facebook_logo.png")
facebook_logo_resize =facebook_logo.resize((150,150))
facebook_logo_resize_image = ImageTk.PhotoImage(facebook_logo_resize)

facebook_button = Button(page_2,image=facebook_logo_resize_image,borderwidth=0)
facebook_button.place(x=250,y=190)


#importing instagram logo and dealing with its size
insta_logo = Image.open(r"photos\instagram_logo.png")
insta_logo_resize =insta_logo.resize((170,170))
insta_logo_resize_image = ImageTk.PhotoImage(insta_logo_resize)

insta_button = Button(page_2,image=insta_logo_resize_image,borderwidth=0)
insta_button.place(x=550,y=380)

"""End of the category page"""


"""Dealing with 1st page"""
#importing the background image
bg_image = Image.open(r"photos\intro_page.png")

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
start_button = Image.open(r"photos\start_button.png")
start_button_image = ImageTk.PhotoImage(start_button)

#defining the button and setting its position.
intro_button = Button(page_1,image=start_button_image,borderwidth=0,command=lambda:page_2.tkraise())
intro_button.place(x=600,y=470)

"""End of the 1st page"""


root.mainloop()