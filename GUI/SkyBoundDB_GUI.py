import tkinter as tk
from PIL import ImageTk, Image
from CharacterClass.Character import Character, compute_advantage, characterRoster
import os


class Character_select:
    def __init__(self):
        self.selected_moves = []
        self.selectedNum = 0
        self.root = tk.Tk()
        self.root.title("SkyBoundDB")
        self.character_frame = tk.Frame(self.root)
        self.move_frame = tk.Frame(self.root, bg='black')
        self.compare_screen_frame = tk.Frame(self.root, bg='red')

        # Default packed frame
        self.character_frame.pack()

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
            rosterList.append(
                baseDir + characterRoster[characters] + imageSuffix)
        New_Character_photo = []
        for i in range(0, len(rosterList)):
            Character_photo = Image.open(rosterList[i])
            Character_resized = Character_photo.resize(
                (138, 138), Image.ANTIALIAS)
            New_Character_photo.append(ImageTk.PhotoImage(Character_resized))

        return New_Character_photo

    def button_mapping(self):
        faceButtons = []
        for i in range(len(characterRoster)):
            faceButtons.append(
                tk.Button(self.character_frame, image=self.skyfarer[i],
                          command=lambda z=i: [self.to_move_select(), self.incrementSelectedNum(), self.show_moves(z),
                                               self.update_compare_button()]))
            faceButtons[i].bind("<Button-3>", lambda event, k=i: [self.select_move(k, ""), self.incrementSelectedNum(),
                                                                  self.update_compare_button()])
            faceButtons[i].pack(side=tk.LEFT, anchor=tk.N)
        self.compareButton = tk.Button(self.character_frame, text='Compare', state=tk.DISABLED,
                                       command=lambda: [print(self.selected_moves), self.to_compare_screen(), self.compare_screen()])
        self.compareButton.pack()

    def show_moves(self, char_id):
        self.buttons_text = []
        temp_character = Character(0, characterRoster[char_id])
        self.moves = temp_character.moves
        rowNum = 0
        columnNum = 0
        self.moveButtons = []
        for k in range(len(self.moves)):
            self.buttons_text.append(tk.StringVar())
            self.moveButtons.append(tk.Button(self.move_frame, textvariable=self.buttons_text[k], fg='white', bg='gray',
                                              command=lambda j=k: [self.select_move(char_id, self.moves[j]),
                                                                   self.to_character_select()]))
            self.print_moves_to_button(temp_character, self.moves[k], k)
            columnNum += 1
            if columnNum >= 3:
                columnNum = 0
                rowNum += 1
            self.moveButtons[k].grid(row=rowNum, column=columnNum)
        cancelButton = tk.Button(self.move_frame, text="Cancel",
                                 command=lambda: [self.to_character_select()], fg='red')
        cancelButton.grid(row=rowNum + 1, column=1, pady=5)

    def to_move_select(self):
        print("From Character_Select to Move_Select")
        self.character_frame.pack_forget()
        self.move_frame.pack()

    def to_character_select(self):
        print("From Move_Select to Character_Select")
        self.move_frame.destroy()
        self.move_frame = tk.Frame(self.root, bg='black')
        self.character_frame.pack()

    def print_moves_to_button(self, character, move, buttons_text_id):
        moveToPrint = character.df[move]
        string = character.returnMoveStr(moveToPrint, move)
        self.buttons_text[buttons_text_id].set(string)

    def select_move(self, char_id, move):
        if len(self.selected_moves) >= 2:
            self.selected_moves.pop(0)
        self.selected_moves.append((characterRoster[char_id], move))
        print(self.selected_moves)

    def incrementSelectedNum(self):
        self.selectedNum += 1
        print(self.selectedNum)

    def update_compare_button(self):
        if self.selectedNum >= 2:
            self.compareButton['state'] = tk.NORMAL
        else:
            self.compareButton['state'] = tk.DISABLED

    def to_compare_screen(self):
        self.character_frame.pack_forget()
        self.compare_screen_frame.pack()

    def initialize_selectedNum(self):
        self.selectedNum = 0

    def compare_screen(self):
        self.comparison = tk.Label(self.compare_screen_frame, text='myShit')
        self.comparison.pack()
        cancelButton = tk.Button(self.compare_screen_frame, text="return", command= self.from_compare_to_character_select)
        cancelButton.pack()

    def from_compare_to_character_select(self):
        self.selected_moves.clear()
        self.initialize_selectedNum()
        self.update_compare_button()
        self.compare_screen_frame.destroy()
        self.compare_screen_frame = tk.Frame(self.root, bg='red')
        self.character_frame.pack()



p = Character_select()
