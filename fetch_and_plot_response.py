# import turtle module
import turtle

# From symbols module, import Symbol Class
from symbols import Symbol

# Creating a Class named Response that can fetch the user's input and plot the symbol inside the block of the board accordingly
# Class Response inherits Class Symbol
class Response (Symbol):

    # Initialization
    def __init__(self):
        # Since, the class is inherited, the parent class initialization
        super().__init__()

        # After initialization, 'self.symbol' can be used. Keeping simplicity in mind, an object with the same name 
        # of the child class is instantiated.
        self.response = self.symbol
        
        # Creating two lists, self.One and self.Two to track the user inputs and store them inside the list.

        # List to store Player one's inputs (cross)
        self.One = []

        # List to store Player two's inputs (circle)
        self.Two = []

        # Every possible winning combination. The numbers denotes the respective block on the board.
        self.win_combination = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    # A Method to draw symbols inside a block on the board layout.
    def fetch_and_plot(self, player) -> str:

        """This method draws symbols (cross/circle) inside a block on the board layout. It takes player's identity as 
            an input argument. The method returns a string."""

        while True:

            # Getting Player's input in numeric form
            x = turtle.numinput(f"Player {player}", "Your Turn: ")

            # Checking for presence of input digit, if the digit is already entered by either of the user.

            # For each digit in 'self.One' list, if the entered digit is present in this list, expression evaluates to 'True'
            check_for_presence_One = any(x == each_item for each_item in self.One)

            # For each digit in 'self.One' list, if the entered digit is present in this list, expression evaluates to 'True'
            check_for_presence_Two = any(x == each_item for each_item in self.Two)

            # If the entered number is not present in either of the list, accept the digit and break the loop.
            if check_for_presence_One is False and check_for_presence_Two is False:
                break

        # Drawing the symbol inside a block by matching the Player's identity and based on the player's input.

        if x == 1 and player == 'One':
            self.draw_cross(Symbol.CROSS_1)
        elif x == 1 and player == 'Two':
            self.draw_circle(Symbol.CIRCLE_1)

        if x == 2 and player == 'One':
            self.draw_cross(Symbol.CROSS_2)
        elif x == 2 and player == 'Two':
            self.draw_circle(Symbol.CIRCLE_2)

        if x == 3 and player == 'One':
            self.draw_cross(Symbol.CROSS_3)
        elif x == 3 and player == 'Two':
            self.draw_circle(Symbol.CIRCLE_3)

        if x == 4 and player == 'One':
            self.draw_cross(Symbol.CROSS_4)
        elif x == 4 and player == 'Two':
            self.draw_circle(Symbol.CIRCLE_4)

        if x == 5 and player == 'One':
            self.draw_cross(Symbol.CROSS_5)
        elif x == 5 and player == 'Two':
            self.draw_circle(Symbol.CIRCLE_5)

        if x == 6 and player == 'One':
            self.draw_cross(Symbol.CROSS_6)
        elif x == 6 and player == 'Two':
            self.draw_circle(Symbol.CIRCLE_6)

        if x == 7 and player == 'One':
            self.draw_cross(Symbol.CROSS_7)
        elif x == 7 and player == 'Two':
            self.draw_circle(Symbol.CIRCLE_7)

        if x == 8 and player == 'One':
            self.draw_cross(Symbol.CROSS_8)
        elif x == 8 and player == 'Two':
            self.draw_circle(Symbol.CIRCLE_8)

        if x == 9 and player == 'One':
            self.draw_cross(Symbol.CROSS_9)
        elif x == 9 and player == 'Two':
            self.draw_circle(Symbol.CIRCLE_9)

        # Storing the Player's input in their respective list to keep track and compare it with the elements of 'self.win_combination'.
        if player == 'One':
            self.One.append(x)
        elif player == 'Two':
            self.Two.append(x)
 
        # Comparing both lists with the list of every possible winning combinations
        for each_combination in self.win_combination:

            # Returns True if all the elements of 'each_combination' are present in 'self.One', else, returns False.
            bool1 = all(item in self.One for item in each_combination)

            # Returns True if all the elements of 'each_combination' are present in 'self.Two', else, returns False.
            bool2 = all(item in self.Two for item in each_combination)
            
            if bool1: # (bool1 == True)
                # returns the player's identity (In this case, 'One')
                return player
            elif bool2: # (bool2 == True)
                # returns the player's identity (In this case, 'Two')
                return player

        # If none of the combination matches, 'None' is returned.
        return None

    # A Method to declare the winner
    def announce_win(self, player):

        """This method announces the winner among the two players. It takes player's identity as an input argument."""

        # Player's identity is not None, i.e. one among the two players won.
        if player is not None:

            # If Player One won, set color to 'red' or set to 'blue' if Player two won.
            color = 'red' if player == 'One' else 'blue'
            # Setting the pointer's color
            self.response.color(color)
            
            # Declaring the winner by displaying a text
            #--------------------------------------------

            # Get the pointer to a specific position to display the text correctly
            self.response.penup()
            self.response.goto(-125, 0) 
            self.response.pendown()

            # Displaying the Text
            self.response.write(f'Player {player} wins...!', move=False, font=('Times New Roman', 25, 'bold'))
        else: # Nobody Won and its a draw.

            # Setting the pointer's color to 'black'
            self.response.color('black')

            # Get the pointer to a specific position to display the text correctly
            self.response.penup()
            self.response.goto(-75, 0)
            self.response.pendown()

            # Displaying the Text
            self.response.write("It's a Draw...!", move=False, font=('Times New Roman', 25, 'bold'))
    