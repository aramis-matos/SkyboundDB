from tkinter import *
from PIL import ImageTk, Image
from Character import Character
root = Tk()

def character_images():
    roster_list = ['Gran.(Granblue.Fantasy).jpg', 'Ferry.(Granblue.Fantasy).jpg', 'Djeeta.(Granblue.Fantasy).jpg']
    New_Character_photo = []

    for i in range(0, len(roster_list)):
        Character_photo = Image.open(roster_list[i])
        Character_resized = Character_photo.resize((138,138), Image.ANTIALIAS)
        New_Character_photo.append(ImageTk.PhotoImage(Character_resized))

    return New_Character_photo

label = Label(root, text = "Character Select")
label.pack()

skyfarer = character_images()

# Ferry Button
Ferrybutton = Button(root, image = skyfarer[1])
Ferrybutton.pack(side = LEFT, anchor = N)
# Gran Button that prints out the frame data
Granbutton = Button(root, image = skyfarer[0], command = Character(0,"gran").print_fd)
Granbutton.pack(side = LEFT, anchor = N)
# Djeeta Button that prints out the frame data
Djeetabutton = Button(root, image = skyfarer[2], command = Character(0,"djeeta").print_fd)
Djeetabutton.pack(side = LEFT, anchor = N)

root.mainloop()