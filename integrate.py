# From fetch_and_plot_response module, import Class Response
from fetch_and_plot_response import Response

# A final Class inheriting all classes just for the main module to access every module/class attributes and methods
# Class Integrate inherits Class Response
class Integrate (Response):

    # Initialization
    def __init__(self):

        # Since, the class is inherited, the parent class initialization
        super().__init__()
        