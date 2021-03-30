import tkinter as tk
from PIL import ImageTk, Image
from CharacterClass.Character import Character
import os

#idea: use config to change to different Frames and thus access others
class Character_select:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SkyBoundDB")

        self.frame = tk.Frame(self.root)
        self.frame2 = tk.Frame(self.root)

        # Default packed frame
        self.frame.pack()

        self.skyfarer = Character_select.character_images(self)
        self.print_buttons = Character_select.button_mapping(self)
        self.print_button_list = Character_select.example_selection_mapping(self)
        self.root.mainloop()

    def character_images(self):
        baseDir = os.path.dirname(os.path.abspath(__file__))
        baseDir = baseDir+"/CharacterImages/"
        roster_list = [baseDir+'Gran.(Granblue.Fantasy).jpg', baseDir+'Ferry.(Granblue.Fantasy).jpg', baseDir+'Djeeta.(Granblue.Fantasy).jpg']
        New_Character_photo = []

        for i in range(0, len(roster_list)):
            Character_photo = Image.open(roster_list[i])
            Character_resized = Character_photo.resize((138,138), Image.ANTIALIAS)
            New_Character_photo.append(ImageTk.PhotoImage(Character_resized))

        return New_Character_photo

    def button_mapping(self):
        # Ferry Button
        Ferrybutton = tk.Button(self.frame, image = self.skyfarer[1], command = lambda:[self.change_state(1)])
        Ferrybutton.pack(side = tk.LEFT, anchor = tk.N)
        # Gran Button that prints out the frame data
        Granbutton = tk.Button(self.frame, image = self.skyfarer[0], command = lambda:[self.change_state(0)])
        Granbutton.pack(side = tk.LEFT, anchor = tk.N)
        # Djeeta Button that prints out the frame data
        Djeetabutton = tk.Button(self.frame, image = self.skyfarer[2], command = lambda:[self.change_state(2)])
        Djeetabutton.pack(side = tk.LEFT, anchor = tk.N)
#how will it print different buttons for each move?
    def example_selection_mapping(self):
        move_ACXXXbutton = tk.Button(self.frame2, text = self.test_move_printing(), command = self.change_state2)
        move_ACXXXbutton.pack(pady = 10)

    def change_state(self, state):
        print("From Character_Select to Move_Select")
        if (state == 1):
            pass
        elif (state == 0):
            Character(0,"gran").print_fd()
        elif (state == 2):
            Character(0,"djeeta").print_fd()
        self.frame.pack_forget()
        self.frame2.pack()

    def change_state2(self):
        print("From Move_Select to Character_Select")
        self.frame2.pack_forget()
        self.frame.pack()


    def test_move_printing(self):
        chr_name = 'gran'
        make_touple = ["Damage: ", "Guard: ", "Startup: ", "Active: ", "Recovery: ", "On Block: ", "On Hit: "]

        chr_selected = Character('0', str(chr_name))
        chr_selectedMove = list(chr_selected.df[chr_selected.moves[4]])
        string_format = "Move: " + chr_selected.moves[4] + "\n"
        for i in range(len(chr_selectedMove)):
            string_format = string_format + str(make_touple[i]) + str(chr_selectedMove[i]) + "\n"
        print(string_format)
        return string_format

#do without taking any parameters
#    def test_move_formatting(self, to_format):
#        for move_get in range(len(to_format)):
#        return


p = Character_select()