# SkyboundDB: The GBFVS Frame Data Calculator

## What is **SkyboundDB**?
___
SkyboundDB is a an app that calculates frame advantage for a number of characters from the fighting game Granblue Fantasy Versus. The characters that are currently available are Gran, Djeeta, Zeta, Katalina, Ferry and Zooey.  

## Motivation and background
The reason why we decided to make this was mainly due to a school project. However, it was also born out of a curiosity to go beyond our comfort zone and tackle the beast we had not previously even looked at, UI. The team is comprised of mostly C++ developers who had only worked on CLI programs. So this project really helped us widen our horizons in the development space.  
  
Another reason behind the development was due to a dissatisfaction with the current tools for calculating frame data. It's a rather pen-and-paper sort of affair for the most part and we believe it's a rather unintuitive approach for the beginner.

## Platform used and associated libraries

The project uses Python 3 along with the Pandas and Pillow modules. The reasons behind the selected language and libraries fall under two broad categories:
- Firstly, Python is a fairly straightforward language and speed was not a major concern in the development of the application.  

- Secondly, Pandas allows for fairly seamless integration of CSV files without doing manual parsing.

## Difficulties faced and possible future developments
Due to our inexperience with UI development, the use of lambdas and the completely distinct nature from anything we've ever worked with proved to be the most difficult and tedious part of the development process.

We wish to refactor the code quite a bit and add more characters in the future.

___
## System Requirements
- Python 3 interpreter
    - Pandas module
    - Pillow module

## Install process and usage
Simply install the python 3 interpreter along with pandas and pillow and run the SkyBoundDB_GUI.py script.  
Left click will select a character and present their moves. Right click will select all of their moves. Note that right click only works for the responder.

## Program Examples

**Main Menu**  
![Main Menu](https://github.com/aramis-matos/COMP4009-Proyect/blob/main/example%20pictures/main_menu.png "Main Menu")  
**Example Move List**  
![Example Move List](https://github.com/aramis-matos/COMP4009-Proyect/blob/main/example%20pictures/gran_move_list.png "Gran Move List")  
**Comparison with One Move**  
![Comparison with One Move](https://github.com/aramis-matos/COMP4009-Proyect/blob/main/example%20pictures/comparison_with_one_move.png "Comparison one move")  
**Comparison with All Moves**  
![Comparison with All Moves](https://github.com/aramis-matos/COMP4009-Proyect/blob/main/example%20pictures/comparison_with_all.png "Comparison with all moves")  

## Credits

[Aramis Matos](https://github.com/aramis-matos "Aramis Github")  
[Lenier Gerena](https://github.com/Suaniel "Lenier Github")  
[Christian Rodriguez](https://github.com/aramis-matos/COMP4009-Proyect/blob/main/example%20pictures/C90CEADE-8E44-46C8-8CF5-2893B516067A.png "Christian Github")



