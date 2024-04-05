from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("700x600")

# Load the image
bg_image = Image.open("intro_page.png")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Resize the image to fit the frame
resized_bg_image = bg_image.resize((screen_width, screen_height))
resized_bg_image_tk = ImageTk.PhotoImage(resized_bg_image)

# Create a frame
page_1 = Frame(root)
page_1.place(relx=0, rely=0, relwidth=1, relheight=1)  # Cover the entire root window

# Create a label within the frame and set the image
bg_image_label = Label(page_1, image=resized_bg_image_tk)
bg_image_label.place(x=0, y=0, relwidth=1, relheight=1)  # Fill the entire frame

root.mainloop()