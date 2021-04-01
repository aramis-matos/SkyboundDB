import tkinter as tk
from PIL import ImageTk, Image
from CharacterClass.Character import Character, compute_advantage, characterRoster
import os


class Character_select:
    def __init__(self):
        self.selected_moves = []
        self.root = tk.Tk()
        self.root.title("SkyBoundDB")

        self.frame = tk.Frame(self.root)
        self.frame2 = tk.Frame(self.root, bg='black')

        # Default packed frame
        self.frame.pack()

        self.skyfarer = Character_select.character_images(self)
        Character_select.button_mapping(self)
        self.root.mainloop()

    def character_images(self):
        baseDir = os.path.dirname(os.path.abspath(__file__))
        if baseDir.find(r'/') == -1:
            baseDir = baseDir.replace(r'/', r'\\')
            baseDir += "\\CharacterImages\\"
        else:
            baseDir += "/CharacterImages/"
        imageSuffix = '.(Granblue.Fantasy).jpg'
        rosterList = []
        for characters in range(len(characterRoster)):
            rosterList.append(baseDir + characterRoster[characters] + imageSuffix)
        New_Character_photo = []

        for i in range(0, len(rosterList)):
            Character_photo = Image.open(rosterList[i])
            Character_resized = Character_photo.resize((138, 138), Image.ANTIALIAS)
            New_Character_photo.append(ImageTk.PhotoImage(Character_resized))

        return New_Character_photo

    def button_mapping(self):
        faceButtons = []
        for i in range(len(characterRoster)):
            faceButtons.append(
                tk.Button(self.frame, image=self.skyfarer[i],
                          command=lambda z=i: [self.change_state(), self.show_moves(z)]))
            faceButtons[i].pack(side=tk.LEFT, anchor=tk.N)

    def show_moves(self, char_id):
        self.buttons_text = []

        temp_character = Character(0, characterRoster[char_id])
        self.moves = temp_character.moves
        rowNum = 0
        columnNum = 0
        self.moveButtons = []
        for k in range(len(self.moves)):
            self.buttons_text.append(tk.StringVar())
            self.moveButtons.append(tk.Button(self.frame2, textvariable=self.buttons_text[k], fg='white', bg='gray',
                                              command=lambda j=k: [self.select_move(char_id, self.moves[j]),
                                                                   self.change_state2()]))
            self.print_moves_to_button(temp_character, self.moves[k], k)
            columnNum += 1
            if columnNum >= 3:
                columnNum = 0
                rowNum += 1
            self.moveButtons[k].grid(row=rowNum, column=columnNum)

        cancelButton = tk.Button(self.frame2, text="Cancel",
                                 command=lambda: [self.change_state2()], fg='red')
        cancelButton.grid(row=rowNum + 1, column=1, pady=5)

    def change_state(self):
        print("From Character_Select to Move_Select")
        self.frame.pack_forget()
        self.frame2.pack()

    def change_state2(self):
        print("From Move_Select to Character_Select")
        self.frame2.destroy()
        self.frame2 = tk.Frame(self.root, bg='black')
        self.frame.pack()

    def print_moves_to_button(self, character, move, buttons_text_id):
        moveToPrint = character.df[move]
        string = character.returnMoveStr(moveToPrint, move)
        self.buttons_text[buttons_text_id].set(string)

    def select_move(self, char_id, move):
        if len(self.selected_moves) >= 2:
            self.selected_moves.pop(0)
        self.selected_moves.append((characterRoster[char_id], move))
        print(self.selected_moves)

    def setEntryValue(self):
        self.tempVal = self.getNameOfMove.get()


p = Character_select()
