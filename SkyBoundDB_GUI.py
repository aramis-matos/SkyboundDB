from tkinter import *
from PIL import ImageTk, Image
from Character import Character
root = Tk()

#def character_images():
#    roster_list = ['Gran', 'Ferry', 'Djeeta']
#    photo_extension = '.(Granblue.Fantasy).jpg'
#
#    for i in range(0, len(roster_list)):
#        Character_photo = Image.open(roster_list[i].join(photo_extension))
#        Character_resized = Character_photo[i].resize((138,138), Image.ANTIALIAS)
#        New_Character_photo = ImageTk.PhotoImage(Character_resized[i])
#
#    return New_Character_photo[i]

label = Label(root, text = "Character Select")
label.pack()

# Open Image
Ferry_photo = Image.open("Ferry.(Granblue.Fantasy).jpg")
Gran_photo = Image.open("Gran.(Granblue.Fantasy).jpg")
Djeeta_photo = Image.open("Djeeta.(Granblue.Fantasy).jpg")
# Resize Image
Ferry_resized = Ferry_photo.resize((138,138), Image.ANTIALIAS)
Gran_resized = Gran_photo.resize((138,138), Image.ANTIALIAS)
Djeeta_resized = Djeeta_photo.resize((138,138), Image.ANTIALIAS)
# Place resized image in the button
New_Ferry_photo = ImageTk.PhotoImage(Ferry_resized)
New_Gran_photo = ImageTk.PhotoImage(Gran_resized)
New_Djeeta_photo = ImageTk.PhotoImage(Djeeta_resized)

# Ferry Button
Ferrybutton = Button(root, image = New_Ferry_photo)
Ferrybutton.pack(side = LEFT, anchor = N)
# Gran Button that prints out the frame data
Granbutton = Button(root, image = New_Gran_photo, command = Character(0,"gran").print_fd)
Granbutton.pack(side = LEFT, anchor = N)
# Djeeta Button that prints out the frame data
Djeetabutton = Button(root, image = New_Djeeta_photo, command = Character(0,"djeeta").print_fd)
Djeetabutton.pack(side = LEFT, anchor = N)

root.mainloop()