
# from ... import Model
from abc import abstractmethod
from FullRegistrationController import FullRegistrationController

# abstract class for menu views, each menu view will inherit from this class and implement the render method to display the menu options and handle user input
# only needs render method
class Menu():
    def __init__(self, controller: FullRegistrationController):
        self.controller = controller
    
    @abstractmethod
    def render(self) -> None:
        pass
    
    
    def check_input(self, user_input: str) -> bool:
        return True

    