
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
youtube_button.place(x=840,y=220)

