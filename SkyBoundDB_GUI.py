from tkinter import *
from PIL import ImageTk, Image
root = Tk()

label = Label(root, text = "Character Select")
label.pack()

# Open Image
Ferry_photo = Image.open("Ferry.(Granblue.Fantasy).jpg")
# Resize Image
Ferry_resized = Ferry_photo.resize((150,125), Image.ANTIALIAS)
# Place resized image in the button
New_Ferry_photo = ImageTk.PhotoImage(Ferry_resized)

Ferrybutton = Button(root, image = New_Ferry_photo)
Ferrybutton.pack(side = LEFT, anchor = N)

Granbutton = Button(root, text = "Insert Gran Image")
Granbutton.pack(side = LEFT, anchor = N)

root.mainloop()