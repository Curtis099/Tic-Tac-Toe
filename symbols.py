# From board module, import Board Class
from board import Board

# Creating a Class named 'Symbol' that can draw symbols, and display numeric figures
# Class Symbol inherits Class Board
class Symbol (Board):

    # The following numbers are coordinates to draw crosses and circles at each block. These coordinates has to be 
    # added to 300 to achieve the correct location. Since the designed board layout is of 600 x 600 dimension, the 
    # (0, 0) or the origin lies at the centre (300, 300).

    # Note: The turtle graphics refers Cartesian coordinate system to plot any shape on the screen. 

    # Coordinates for Cross (Read the comments of 'draw_cross' method to understand the coordinates)
    CROSS_1 = [-575, -25, -425, -175, -425, -25, -575, -175]   # 1st Block
    CROSS_2 = [-375, -25, -225, -175, -225, -25, -375, -175]   # 2nd Block
    CROSS_3 = [-175, -25, -25, -175, -25, -25, -175, -175]     # 3rd Block
    CROSS_4 = [-575, -225, -425, -375, -425, -225, -575, -375] # 4th Block
    CROSS_5 = [-375, -225, -225, -375, -225, -225, -375, -375] # 5th Block
    CROSS_6 = [-175, -225, -25, -375, -25, -225, -175, -375]   # 6th Block
    CROSS_7 = [-575, -425, -425, -575, -425, -425, -575, -575] # 7th Block
    CROSS_8 = [-375, -425, -225, -575, -225, -425, -375, -575] # 8th Block
    CROSS_9 = [-175, -425, -25, -575, -25, -425, -175, -575]   # 9th Block

    # Coordinates for Circle
    CIRCLE_1 = [-500, -175] # 1st Block
    CIRCLE_2 = [-300, -175] # 2nd Block
    CIRCLE_3 = [-100, -175] # 3rd Block
    CIRCLE_4 = [-500, -375] # 4th Block
    CIRCLE_5 = [-300, -375] # 5th Block
    CIRCLE_6 = [-100, -375] # 6th Block
    CIRCLE_7 = [-500, -575] # 7th Block
    CIRCLE_8 = [-300, -575] # 8th Block
    CIRCLE_9 = [-100, -575] # 9th Block

    # Initialization
    def __init__(self):
        # Since, the class is inherited, the parent class initialization
        super().__init__()

        # After initialization, 'self.board' can be used. Keeping simplicity in mind, an object with the same name 
        # of the child class is instantiated.
        self.symbol = self.board

    # A Method to draw Cross inside a block 
    def draw_cross(self, coordinates):

        """This method draws cross inside a block of the board layout. It takes coordinates of the cross as an input argument."""

        # The centre of the board is at 300 x 300 and turtle uses Cartesian coordinate system (centre -> (0, 0) at board ->(300, 300))
        X = 300

        # The color of the pointer is set to 'red' whenever a cross is to be drawn.
        self.symbol.color('red')

        # First Line of the cross (First point -> Top Left)
        self.symbol.penup()
        self.symbol.goto(X + coordinates[0], X + coordinates[1])
        self.symbol.pendown()

        # First Line of the cross (Second point -> Bottom Right)
        self.symbol.goto(X + coordinates[2], X + coordinates[3])

        # Second Line of the cross (Third point -> Top Right)
        self.symbol.penup()
        self.symbol.goto(X + coordinates[4], X + coordinates[5])
        self.symbol.pendown()

        # Second Line of the cross (Fourth point -> Bottom Left)
        self.symbol.goto(X + coordinates[6], X + coordinates[7])


    # A Method to draw Circle inside a block
    def draw_circle(self, coordinates):

        """This method draws circle inside a block of the board layout. It takes coordinates of the circle as an input argument."""

        # The centre of the board is at 300 x 300 and turtle uses Cartesian coordinate system (centre -> (0, 0) at board ->(300, 300))
        Y = 300

        # The color of the pointer is set to 'blue' whenever a circle is to be drawn.
        self.symbol.color('blue')

        # Adjusting the pointer position to draw the circle
        self.symbol.penup()
        self.symbol.goto(Y + coordinates[0], Y + coordinates[1])
        self.symbol.pendown()

        # Drawing a circle of radius 75
        self.symbol.circle(75)

    # A Method to assign a number to each block
    def display_numbers(self):

        """This method assigns a number to each block of the board. This method accepts no arguments."""

        # Assign '1' to first block
        self.symbol.penup()
        self.symbol.goto(-275, 275)
        self.symbol.pendown()
        self.symbol.write('1', move=False, font=('Times New Roman', 12, 'bold'))

        # Assign '2' to second block
        self.symbol.penup()
        self.symbol.goto(-75, 275)
        self.symbol.pendown()
        self.symbol.write('2', move=False, font=('Times New Roman', 12, 'bold'))

        # Assign '3' to third block
        self.symbol.penup()
        self.symbol.goto(125, 275)
        self.symbol.pendown()
        self.symbol.write('3', move=False, font=('Times New Roman', 12, 'bold'))

        # Assign '4' to fourth block
        self.symbol.penup()
        self.symbol.goto(-275, 75)
        self.symbol.pendown()
        self.symbol.write('4', move=False, font=('Times New Roman', 12, 'bold'))

        # Assign '5' to fifth block
        self.symbol.penup()
        self.symbol.goto(-75, 75)
        self.symbol.pendown()
        self.symbol.write('5', move=False, font=('Times New Roman', 12, 'bold'))

        # Assign '6' to sixth block
        self.symbol.penup()
        self.symbol.goto(125, 75)
        self.symbol.pendown()
        self.symbol.write('6', move=False, font=('Times New Roman', 12, 'bold'))

        # Assign '7' to seventh block
        self.symbol.penup()
        self.symbol.goto(-275, -125)
        self.symbol.pendown()
        self.symbol.write('7', move=False, font=('Times New Roman', 12, 'bold'))

        # Assign '8' to eighth block
        self.symbol.penup()
        self.symbol.goto(-75, -125)
        self.symbol.pendown()
        self.symbol.write('8', move=False, font=('Times New Roman', 12, 'bold'))

        # Assign '9' to ninth block
        self.symbol.penup()
        self.symbol.goto(125, -125)
        self.symbol.pendown()
        self.symbol.write('9', move=False, font=('Times New Roman', 12, 'bold'))
