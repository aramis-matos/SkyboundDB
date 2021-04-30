import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from CharacterClass.Character import Character, compute_advantage, compute_advantage2, characterRoster
import os


class Character_select:
    '''
    A class used to present the gui for SkyboundDB

    Attributes
    ----------

    selected_moves : list
            a list that contains tuples that hold selected moves
    selected_num : int
            holds how many characters have been selected
    root : tkinter.Tk
            main tkinter frame
    character_frame : tkinter.Frame
            default menu, characters can be selected from here
    move_frame : tkinter.Frame
            contains the moves of a chosen character
            can be accessed through character_frame
    canvas : tkinter.canvas
            where character_moves are placed 
    scrollbar : tkinter.ttk.Scrollbar
            used to scroll through move_frame
    scrolling_frame : tkinter.Frame
            used to accommodate scrollbar 
    skyfarer : list
            contains the images of the characters from characterRoster
    dealer_move_str : str
            is a constant value
    dealer_move : tkinter.StringVar
            holds the value of the the selected dealer character.
    responder_move_str : str
            is a constant value
    responder_move : tkinter.StringVar
            holds the value of the the selected responder character
    dealer_move_label : tkinter.Label
            contains dealer_move and presents it
    responder_move_label : tkinter.Label
            contains responder_move and presents it
    buttons_text : list
            contains tkinter.StringVar objects corresponding
            to a character's moves
    moves : list
            contains the moves variable from a Character object
    skyfarer_moves : list
            contains a character's move images
    moveButtons : list
            containts the buttons containing a character's moves
    label_text : tkinter.StringVar
            presents the comparison of dealer and responder
    compare_button : tk.Button
            allows for transition to comparison_frame
    compare_screen_frame : tkinter.Frame
            is needed to hold compare_scrolling_frame
    compare_canvas : tkinter.Canvas
            needed to house compare_scrolling_frame
    compare_scrolling_frame : tkinter.Frame
            holds the comparison text and images
    compare_scrollbar : tkinter.ttk.Scrollbar
            is a scrollbar for the compare screen
    smaller_skyfarer : list
            contains images of dealer and responder in comparison frame
    
    Methods
    -------
    character_images(x_size, y size)
        creates a list that contains the protrait images of the characters
    move_images(char_id)
        creates a list that contains the move image of character
    button_mapping()
        sets up the character select frame and places character buttons
    show_moves(char_id)
        presents the moves of the character at index char_id 
        in characterRoster
    show_comparison()
        presents the comparison of the dealer and responder of a single move
    to_move_select()
        moves from character_select to move_select
    to_character_select()
        moves from move_select to character_select
    print_moves_to_button(character, move, buttons_text_id)
        places a character's move's data in a string and adds that 
        to self.buttons_text list
    print_results_to_label(dealer, dealer_move, responder, responder_move)
        adds the result of comparison to self.label_text
    select_move(char_id, move)
        adds a move to self.selected_moves
    incrementSelectedNum()
        increments self.selectedNum
    update_compare_button()
        updates the compare button state 
    to_compare_screen()
        updates root to place compare_frame
    reset_values()
        clears moves_select frame
    initialize_selectedNum()
        sets self.selected_num to 0
    from_compare_to_character_select()
        clears the compare frame and moves to character_select
    update_dealer_and_responder_labels()
        updates dealer and responder labels and adds character names
        and moves
    show_comparisons_all()
        presents the comparison of a single dealer move and all of 
        the responder's moves
    '''
    def __init__(self):
        self.selected_moves = []
        self.selectedNum = 0
        self.root = tk.Tk()
        self.root.title("SkyBoundDB")
        self.root.geometry(
            "%dx%d+0+0" % (self.root.winfo_screenwidth(), self.root.winfo_screenheight()))

        # Frames used in program
        self.character_frame = tk.Frame(self.root)
        self.move_frame = tk.Frame(self.root)
        self.compare_screen_frame = tk.Frame(self.root, bg='black')

        # Canvas/Scrollbar creation
        self.canvas = tk.Canvas(self.move_frame)
        self.scrollbar = tk.ttk.Scrollbar(
            self.move_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(
            scrollregion=self.canvas.bbox("all")))
        self.scrolling_frame = tk.Frame(self.canvas)
        self.canvas.create_window(
            (0, 0), window=self.scrolling_frame, anchor="nw")

        # Default packed frame
        self.character_frame.pack()

        self.skyfarer = Character_select.character_images(self,138,138)
        Character_select.button_mapping(self)
        self.root.mainloop()

    def character_images(self, x_size, y_size):
        """
        creates a list containing the portrait images of the character

        Parameters
        ----------
        x_size : int
                the horizontal size of the images being generated
        y_size : int
                the vertical size of the images being generated

        Returns
        -------
        New_Character_photo : list
                contains the images of the cast
        """
        baseDir = os.path.dirname(os.path.abspath(__file__))
        if baseDir.find(r'/') == -1:
            baseDir = baseDir.replace(r'/', r'\\')
            baseDir += "\\CharacterImages\\character_select_images\\"
        else:
            baseDir += "/CharacterImages/character_select_images/"
        imageSuffix = '.(Granblue.Fantasy).jpg'
        rosterList = []
        for characters in range(len(characterRoster)):
            rosterList.append(
                baseDir + characterRoster[characters] + imageSuffix)
        New_Character_photo = []
        for i in range(0, len(rosterList)):
            Character_photo = Image.open(rosterList[i])
            Character_resized = Character_photo.resize(
                (x_size, y_size), Image.ANTIALIAS)
            New_Character_photo.append(ImageTk.PhotoImage(Character_resized))

        return New_Character_photo

    def move_images(self, char_id):
        """
        creates a list containing the images of a character's moves

        Parameters
        ----------
        char_id : int
                is the index of a character in characterRoster list
        
        Returns
        -------
        New_Move_photo : list
                contains the move images of the character specified by char_id
        """
        baseDir = os.path.dirname(os.path.abspath(__file__))
        default_image_dir = baseDir[:]
        if baseDir.find(r'/') == -1:
            baseDir = baseDir.replace(r'/', r'\\')
            default_image_dir = default_image_dir.replace(r'/', r'\\')
            baseDir += f"\\CharacterImages\\{characterRoster[char_id]}_move_images\\"
            default_image_dir += "\\CharacterImages\\"
        else:
            baseDir += f"/CharacterImages/{characterRoster[char_id]}_move_images/"
            default_image_dir += "/CharacterImages/"
        imageSuffix = '_GBVS.png'
        moveList = []
        temp_character = Character(0, characterRoster[char_id])
        for characters in range(len(temp_character.moves)):
            if os.path.exists(baseDir + characterRoster[char_id] + str(temp_character.moves[characters]).encode('unicode-escape').decode() + imageSuffix):
                moveList.append(
                    baseDir + characterRoster[char_id] + str(temp_character.moves[characters]) + imageSuffix)
            else:
                moveList.append(default_image_dir + "GBVS_mainScreen.jpg")
        New_Move_Photo = []
        for i in range(0, len(moveList)):
            Move_photo = Image.open(moveList[i])
            Move_resized = Move_photo.resize(
                (46, 46), Image.ANTIALIAS)
            New_Move_Photo.append(ImageTk.PhotoImage(Move_resized))

        return New_Move_Photo

    def button_mapping(self):
        """
        presents the character select frame. Character select
        frame is now active.
        """
        faceButtons = []
        self.dealer_move_str = "Dealer: "
        self.dealer_move = tk.StringVar()
        self.dealer_move.set(self.dealer_move_str)
        self.responder_move_str = "Responder: "
        self.responder_move = tk.StringVar()
        self.responder_move.set(self.responder_move_str)
        for i in range(len(characterRoster)):
            faceButtons.append(
                tk.Button(self.character_frame, image=self.skyfarer[i],
                          command=lambda z=i: [self.to_move_select(), self.show_moves(z), self.update_compare_button()]))
            faceButtons[i].bind("<Button-3>", lambda event, k=i: [self.select_move(k, ""), self.incrementSelectedNum(),
                                                                  self.update_compare_button(), self.update_dealer_and_responder_labels()])
            faceButtons[i].pack(side=tk.LEFT, anchor=tk.N)
        self.compareButton = tk.Button(self.character_frame, text='Compare', state=tk.DISABLED,
                                       command=lambda: self.to_compare_screen())
        self.compareButton.pack()
        self.dealer_move_label = tk.Label(
            self.character_frame, textvariable=self.dealer_move)
        self.responder_move_label = tk.Label(
            self.character_frame, textvariable=self.responder_move)
        self.dealer_move_label.pack()
        self.responder_move_label.pack()

    def show_moves(self, char_id):
        """
        presents the moves select frame. Moves select frame is now active.
        """
        self.buttons_text = []
        temp_character = Character(0, characterRoster[char_id])
        self.moves = temp_character.moves
        self.skyfarer_moves = self.move_images(char_id)
        rowNum = 0
        columnNum = 0
        self.moveButtons = []
        for k in range(len(self.moves)):
            self.buttons_text.append(tk.StringVar())
            self.moveButtons.append(tk.Button(self.scrolling_frame, image=self.skyfarer_moves[k], textvariable=self.buttons_text[k], compound="left", fg='white', bg='gray',
                                              command=lambda j=k: [self.select_move(char_id, self.moves[j]),
                                                                   self.to_character_select(),  self.incrementSelectedNum(), self.update_compare_button(), self.update_dealer_and_responder_labels()]))
            self.print_moves_to_button(temp_character, self.moves[k], k)
            columnNum += 1
            if columnNum >= 3:
                columnNum = 0
                rowNum += 1
            self.moveButtons[k].grid(row=rowNum, column=columnNum)
        cancelButton = tk.Button(self.scrolling_frame, text="Cancel",
                                 command=lambda: [self.to_character_select()])
        cancelButton.grid(row=rowNum + 1, column=1, pady=5)

    def show_comparisons(self):
        """
        presents the comparison in between a single dealer move
        and a single responder move. Character select frame is removed
        and show_comparison_frame is placed
        """
        self.label_text = tk.StringVar()
        dealer = Character('0', self.selected_moves[0][0])
        dealer_move = dealer.df[(self.selected_moves[0][1])]
        responder = Character('0', self.selected_moves[1][0])
        responder_move = responder.df[(self.selected_moves[1][1])]
        dealer_color = self.print_results_to_label(
            dealer, dealer_move, responder, responder_move)
        tk.Label(self.compare_scrolling_frame, image=self.smaller_skyfarer[characterRoster.index(
            self.selected_moves[0][0])]).grid(row=0, column=0)
        self.resultLabels = tk.Label(
            self.compare_scrolling_frame, textvariable=self.label_text, fg=dealer_color, bg='gray')
        self.resultLabels.grid(row=0, column=1)
        tk.Label(self.compare_scrolling_frame, image=self.smaller_skyfarer[characterRoster.index(
            self.selected_moves[1][0])]).grid(row=0, column=2)
        returnbutton = tk.Button(
            self.compare_scrolling_frame, text="Cancel", command=self.reset_values)
        returnbutton.grid(row=1, column=1)

    def to_move_select(self):
        """
        removes character select and inserts move select
        """
        print("From Character_Select to Move_Select")
        self.character_frame.pack_forget()
        self.move_frame.pack(fill=tk.BOTH, expand=1)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def to_character_select(self):
        """
        removes moves select and places character select in frame
        """
        print("From Move_Select to Character_Select")
        self.move_frame.destroy()
        self.scrolling_frame.destroy()
        self.canvas.destroy()
        self.scrollbar.destroy()
        self.move_frame = tk.Frame(self.root)
        self.canvas = tk.Canvas(self.move_frame)
        self.scrollbar = tk.ttk.Scrollbar(
            self.move_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(
            scrollregion=self.canvas.bbox("all")))
        self.scrolling_frame = tk.Frame(self.canvas)
        self.canvas.create_window(
            (0, 0), window=self.scrolling_frame, anchor="nw")
        self.character_frame.pack()

    def print_moves_to_button(self, character, move, buttons_text_id):
        """
        adds text to label_text

        Parameters
        ----------
        character : Character
                is the character whose move you want to print
        move : str
                is an string of character.moves list
        buttons_text_id : int
                position of buttons text list
        """
        moveToPrint = character.df[move]
        string = character.returnMoveStr(moveToPrint, move)
        self.buttons_text[buttons_text_id].set(string)

    def print_results_to_label(self, dealer, dealer_move, responder, responder_move):
        """
        prints the advantage state of the dealer and responder

        Parameters
        ----------
        dealer : Character
                the one dishing out the first move  
        dealer_move : str
                the move from dealer.moves that was dealt
        responder : Character
                the one responding to the dealer's move
        responder_move : str
                the move from responder.moves that was dealt

        Returns
        -------
        dealer_color : str
                the advantage color of a comparison
        """
        resultToPrint, dealer_color = compute_advantage2(
            dealer, dealer_move, responder, responder_move)
        self.label_text.set(resultToPrint)
        return dealer_color

    def select_move(self, char_id, move):
        """
        adds a move and character to self.selected_moves

        Parameters
        ----------
        char_id : int
                is the index of a character in characterRoster list
        move : str
                the move from Character.moves that was chosen
        """
        if len(self.selected_moves) >= 2:
            self.selected_moves.pop(0)
        self.selected_moves.append((characterRoster[char_id], move))
        print(self.selected_moves)

    def incrementSelectedNum(self):
        """
        Increments self.SelectedNum, duh
        """
        self.selectedNum += 1
        print(self.selectedNum)

    def update_compare_button(self):
        """
        enables or disables the compare button
        """
        if self.selectedNum >= 2 and self.selected_moves[0][1] != '':
            self.compareButton['state'] = tk.NORMAL
        else:
            self.compareButton['state'] = tk.DISABLED

    def to_compare_screen(self):
        """
        disables character select frame and packs needed frame for character select 
        """
        self.dealer_move_label['textvariable'] = self.dealer_move.set(
            self.dealer_move_str)
        self.responder_move_label['textvariable'] = self.responder_move.set(
            self.responder_move_str)
        self.character_frame.pack_forget()
        self.compare_screen_frame = tk.Frame(self.root)
        # self.compare_screen_frame.pack()
        self.compare_canvas = tk.Canvas(self.compare_screen_frame)
        self.compare_scrollbar = tk.ttk.Scrollbar(
            self.compare_screen_frame, orient=tk.VERTICAL, command=self.compare_canvas.yview)
        self.compare_canvas.configure(
            yscrollcommand=self.compare_scrollbar.set)
        self.compare_canvas.bind("<Configure>", lambda e: self.compare_canvas.configure(
            scrollregion=self.compare_canvas.bbox("all")))
        self.compare_scrolling_frame = tk.Frame(self.compare_canvas)
        self.compare_canvas.create_window(
            (0, 0), window=self.compare_scrolling_frame, anchor="nw")
        self.compare_screen_frame.pack(fill=tk.BOTH, expand=1)
        self.compare_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.compare_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.smaller_skyfarer = self.character_images(46,46)
        if self.selected_moves[1][1] == "":
            self.show_comparisons_all()
        else:
            self.show_comparisons()

    def reset_values(self):
        """
        resets values from compare frame and moves towards
        character select
        """
        self.selected_moves.clear()
        self.selectedNum = 0
        self.update_compare_button()
        self.compare_screen_frame.destroy()
        self.compare_scrolling_frame.destroy()
        self.character_frame.pack()

    def initialize_selectedNum(self):
        """
        initializes selectedNum, duh
        """
        self.selectedNum = 0

    def from_compare_to_character_select(self):
        self.selected_moves.clear()
        self.update_dealer_and_responder_labels()
        self.initialize_selectedNum()
        self.update_compare_button()
        self.compare_screen_frame.destroy()
        self.compare_screen_frame = tk.Frame(self.root, bg='black')
        self.character_frame.pack()

    def update_dealer_and_responder_labels(self):
        """
        updates dealer and responder labels text
        """
        if len(self.selected_moves) == 1:
            self.dealer_move.set(self.dealer_move_str +
                                 str(self.selected_moves[0]))
        if len(self.selected_moves) == 2:
            self.dealer_move.set(self.dealer_move_str +
                                 str(self.selected_moves[0]))
            self.responder_move.set(
                self.responder_move_str+str(self.selected_moves[1]))

    def show_comparisons_all(self):
        """
        presents the comparison in between a single dealer move
        and a all of the responder's moves. Character select frame is removed
        and show_comparison_frame is placed
        """
        labels_text = []
        dealer = Character(
            0, characterRoster[characterRoster.index(self.selected_moves[0][0])])
        responder = Character(
            0, characterRoster[characterRoster.index(self.selected_moves[1][0])])
        dealer_move = dealer.df[self.selected_moves[0][1]]
        responder_moves = responder.moves
        rowNum = 0
        columnNum = 0
        results_labels = []
        string = ""
        advantage_color = ""
        dealer_photo_arr = []
        responder_photo_arr = []
        for k in range(len(responder_moves)):
            dealer_photo_arr.append(tk.Label(self.compare_scrolling_frame, image=self.smaller_skyfarer[characterRoster.index(
            self.selected_moves[0][0])],pady= 5))
            responder_photo_arr.append(tk.Label(self.compare_scrolling_frame, image=self.smaller_skyfarer[characterRoster.index(
            self.selected_moves[1][0])],pady= 5))
            string, advantage_color = compute_advantage2(
                dealer, dealer_move, responder, responder.df[responder_moves[k]])
            labels_text.append(tk.StringVar())
            results_labels.append(tk.Label(
                self.compare_scrolling_frame, textvariable=labels_text[k], fg=advantage_color))
            labels_text[k].set(f'{str(responder_moves[k])}\n{string}')
            if columnNum >= 3:
                columnNum = 0
                rowNum += 1
            dealer_photo_arr[k].grid(row = rowNum, column=columnNum*3)
            results_labels[k].grid(row=rowNum, column=columnNum*3+1)
            responder_photo_arr[k].grid(row = rowNum, column=columnNum*3+2)
            columnNum += 1
        cancelButton = tk.Button(self.compare_scrolling_frame, text="Cancel",
                                 command=lambda: [self.from_compare_to_character_select()], fg='black')
        cancelButton.grid(row=rowNum + 1, column=4, pady=5, rowspan=3)


p = Character_select()
