
# from ... import Model
from abc import abstractmethod
from FullRegistrationController import FullRegistrationController

class Menu():
    def __init__(self, controller: FullRegistrationController):
        self.controller = controller
    
    @abstractmethod
    def render(self) -> None:
        pass
    
    

    