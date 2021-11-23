# From integrate module, import Class Integrate
import turtle
from integrate import Integrate


while True:

    # Creating an object using Class Integrate
    window = Integrate()
    
    # Calling the Class 'Board' method (Method 'draw_board' to draw the board layout) on an Object created 
    # using Class Integrate because Class Integrate is inherited.
    window.draw_board()

    # Calling the Class 'Symbol' method (Method 'display_numbers' to assign a number to each block of the 
    # board on an Object created using Class Integrate because Class Integrate is inherited.
    window.display_numbers()

    # To take the input from the players 9 times since, there are 9 blocks. 
    # Player One Input Count: 5
    # Player Two Input Count: 4
    for a in range(1, 10):

        # The digits: 1, 3, 5, 7, 9 indicates that it's Player One's turn
        if a % 2 != 0:
            string = 'One'
        else:
            # The digits: 2, 4, 6, 8 indicates that it's Player Two's turn
            string = 'Two'

        # Calling the Class 'Response' method (Method 'fetch_and_plot' to draw symbols (cross/circle) inside 
        # a block on the board) on an Object created using Class Integrate because Class Integrate is inherited.
        # Storing the result returned by the method. 
        result = window.fetch_and_plot(string)

        # If one among the two players won, then Player's identity is returned and the loop breaks to conclude
        # the game and avoid any further inputs.
        if result == 'One' or result == 'Two':
            break

            # If 'None' is returned, meaning nobody won yet and loop continues.
    
    
    # Calling the Class 'Response' method (Method 'announce_win' to announce the winner among the two players or declare a Draw) 
    # on an Object created using Class Integrate because Class Integrate is inherited.
    window.announce_win(result)

    # Calling the Class 'Board' method (Method 'clear_screen' to clear the screen) on an Object created 
    # using Class Integrate because Class Integrate is inherited.
    bool_for_screen = window.clear_screen()

    # If bool_for_screen is True, clear the screen
    if bool_for_screen:
        turtle.clearscreen()
    else:
        break # Exit the loop and end the game
