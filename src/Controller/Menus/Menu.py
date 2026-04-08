
from __future__ import annotations
from abc import abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from FullRegistrationController import FullRegistrationController

# abstract class for menu views, each menu view will inherit from this class and implement the render method to display the menu options and handle user input
# only needs render method
class Menu():
    def __init__(self, controller: FullRegistrationController):
        self.controller = controller
    
    @abstractmethod
    def render(self) -> None:
        pass
    
    
    def check_input(self, user_input: str) -> bool: #should i move this into its own class? maybe a utility class?
        return True

    