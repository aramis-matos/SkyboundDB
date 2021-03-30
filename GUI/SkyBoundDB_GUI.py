import tkinter as tk
from PIL import ImageTk, Image
from CharacterClass.Character import Character, compute_advantage
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
        Character_select.button_mapping(self)
        Character_select.example_selection_mapping(self)
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
        self.button_text = tk.StringVar()
        move_ACXXXbutton = tk.Button(self.frame2, textvariable=self.button_text, command=lambda:[self.test_move_printing(Character(0, "djeeta"), "c.L")])
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


    def test_move_printing(self ,character, move):
        moveToPrint = character.df[move]
        string = character.returnMoveStr(moveToPrint, move)
        self.button_text.set(string)

#do without taking any parameters
#    def test_move_formatting(self, to_format):
#        for move_get in range(len(to_format)):
#        return


p = Character_select()