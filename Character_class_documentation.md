# Character Class Documentation

The Character class is responsible for retrieving a character's moves and frame data.
The characters that are currently implemented are gran, djeeta, zeta, ferry, katalina and zooey.
___

**For example**: 
```python
x = Character(0, "gran")

x.moves = ['c.L', 'c.M', 'c.H', 'ACXX', 'ACXXX', 'f.L', 'f.M', 'f.H', '2L', '2M', '2H', '2U', 'j.L', 'j.M', 'j.H', 'j.U', '5U', 'GT', 'AT', 'OA', '263L', '236M', '236H', '623L', '623M', '623H', '214L', '214L->214M', '214M', '214H', '236236H', '236236U']

x.stats = [0, 1, 2, 3, 4, 5, 6]

x.df =    c.L  c.M   c.H ACXX ACXXX  ... 214L->214M  214M  214H     236236H     236236U
0  400  700  1200  350   350  ...        500  1200  1200  3500->2500  4500->3500
1    m    m     m    m     m  ...          m     m     m           m       mathl
2    5    6     8  NaN   NaN  ...        NaN    16    13         6+5         8+5
3    3    3     4  NaN   NaN  ...         13    13    13         NaN         NaN
4    6   10    18  NaN   NaN  ...         29    29    37         NaN         NaN
5    2    0    -3   -3    -5  ...        -10   -10    -8         -13         -23
6    6    4     1    1    -1  ...         KD    KD   HKD         HKD         HKD
```

___

It gets this info from CharactersFrameData/**insertCharacterNameHere**_fd.csv

## Class Functions Documentation

- ```python
    def __init__(self, id_num, name)
    ```
    - **Purpose**: Constructor
    - **Precondition**: The number provided to _id_num_ is irrelevant and not used, going to be removed. The name must be the same as the one from _characterRoster_.
    - **Post-condition**: A character class object containing the data of the a specific character is created

- ```python
    @staticmethod
    def get_moves_and_stats(name)
    ```
    - **Purpose**: Access the corresponding character and get _self.moves_, _self.df_ and _self.stats_ data
    - **Precondition**: The string provided for _name_ must be an name from _characterRoster_
    - **Pre-condition**: _self.moves_, _self.df_ and _self.stats_ data is returned

- ```python
    def print_fd(self)
    ```
    - **Purpose**: Print frame data to the terminal
    - **Precondition**: The object must be properly created
    - **Post-condition**: The object's frame data is printed to the terminal

- ```python
    def print_block_name(a)
    ```
    - **Purpose**: Print the block stance for a move
    - **Precondition**: The string _a_ must contain a sequence in a specific format:
    mid = m, a = air, t = throw, high = h, l = low, airthrow = i.
    If there's any other character, replace it with a comma for it to be displayed
    - **Post-condition**: The block stance for a move is printed
    
- ```python
    @staticmethod
    def returnMoveStr(move, moveName)
    ```
    - **Purpose**: Returns a string containing move data 
    - **Precondition**: Move is the list generated from from placing _moveName_ into _self.df_ and _moveName_ is a string
    - **Post-condition**: A string containing _moveName_ plus the move's data is returned

- ```python
    @staticmethod
    def return_block_name(a)
    ```
    - **Purpose**: Similar to _def print_block_name(a)_ but returns a string containing the same thing instead of printing to terminal
    - **Precondition**: The string _a_ must contain a sequence in a specific format:
    mid = m, a = air, t = throw, high = h, l = low, airthrow = i.
    If there's any other character, replace it with a comma for it to be displayed
    - **Post-condition**: The block stance string for a move is returned

___

## Other Functions

- ```python
    def compute_advantage(dealer, dealer_move, responder, responder_move)
    ```
    - **Purpose**: Prints the advantage state of a move. Dealer is the person who threw out the first move and responder is the one reacting to that move
    - **Precondition**: _dealer_ and _responder_ are Character objects and _dealer_move_ and _responder_move_ are lists generated from placing an element from _self.moves_ into _self.df_
    - **Post-condition**: The advantage state of a move is printed to console
    
- ```python
    def advantage_color(num)
    ```
    - **Purpose**: Returns the a string literal stating the advantage color
    - **Precondition**: Parameter _num_ must be an integer
    - **Post-condition**: The color corresponding to the advantage is returned

- ```python
    def compute_advantage2(dealer, dealer_move, responder, responder_move)
    ```
    - **Purpose**: Similar to _compute_advantage(dealer, dealer_move, responder, responder_move)_ but returns a string instead as well as as what _def advantage_color(num)_ 
    - **Precondition**:  _dealer_ and _responder_ are Character objects and _dealer_move_ and _responder_move_ are lists generated from placing an element from _self.moves_ into _self.df_
    - **Post-condition**: A string containing the advantage state of a move is returned and the advantage color as well

