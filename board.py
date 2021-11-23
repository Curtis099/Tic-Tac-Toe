# From turtle module, import Turtle Class
from turtle import Turtle
import turtle

# Create a Class to draw the board layout.
class Board:
    # Initialization
    def __init__(self):
        # Instantiating board object with Turtle Class
        self.board = Turtle()

        # Setting the speed of the pointer
        self.board.speed(5)

        # Setting the background screen color 
        turtle.Screen().bgcolor('black')

        # Setting the thickness of pen
        self.board.width(5)

    # A method to create the board layout
    def draw_board(self):

        """This method creates a board layout of 600 x 600 dimensions with pre-feeded coordinates, and accepts no arguments."""

        # Setting the pointer's color to black
        self.board.color('white')
        
        # Designing the outer borders
        #---------------------------------
        # First coordinate (Top Left)
        self.board.penup()
        self.board.goto(-300, 300)
        self.board.pendown()

        # First Line (Vertival_Left)
        self.board.goto(-300, -300)

        # Second Line (Horizontal_Bottom)
        self.board.goto(300, -300)

        # Third Line (Vertical_Right)
        self.board.goto(300, 300)

        # Fourth Line (Horizontal_Top)
        self.board.goto(-300, 300)

        # Inner Borders
        #----------------------------------------------
        # First Line
        self.board.goto(-100, 300) # First coordinate
        self.board.goto(-100, -300) # Second coordinate

        # Second Line
        self.board.penup()
        self.board.goto(100, 300) # First coordinate
        self.board.pendown()
        self.board.goto(100, -300) # Second coordinate

        # Third Line
        self.board.penup()
        self.board.goto(-300, 100) # First coordinate
        self.board.pendown()
        self.board.goto(300, 100) # Second coordinate

        # Fourth Line
        self.board.penup()
        self.board.goto(-300, -100) # First coordinate
        self.board.pendown()
        self.board.goto(300, -100) # Second coordinate

    # A Method to ask the player to choose a mode.
    # def auto_manual_check(self) -> bool:

    #     """This method opens up a dialog box asking the user whether to play 'Player versus Computer'
    #         or 'Player versus Player'. This method accepts no arguments and returns a boolean value."""

    #     # Asking the user to choose a mode
    #     get_mode = turtle.numinput("Select a Mode", "Enter '1' for 'Player vs Computer mode' or '2' for 'Player vs Player' mode.")

    #     # If get_mode equals to 1, then return 'True' (Player wants to play in 'Player vs Computer' mode) 
    #     # otherwise, return 'False' (Player wants to play in 'Player vs Player' mode)
    #     return True if get_mode == 1 else False

    # Asking the players whether to restart the game or not.
    def clear_screen(self) -> bool:

        """This method opens up a dialog box asking the users whether to resart the game or not. And if yes, 
            then clears the screen. This method accepts no arguments and returns a boolean value."""

        # Prompting for a feedback on whether to restart the game.
        feedback = turtle.numinput("Restart the Game?", "Type: '1 for Yes' OR '2 for No")

        # If feedback equals to 1, then return 'True' otherwise, return 'False'
        return True if feedback == 1 else False
