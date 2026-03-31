from .menu import Menu
from .ProfessorMenu import ProfessorMenu
from .StudentMenu import StudentMenu
from .ClassMenu import ClassMenu

class MainMenu(Menu):
    def render(self) -> None:
        print("Hello, welcome to the University Registration System. Please select an option:")
        print("1. Professor Management")
        print("2. Student Management")
        print("3. Class Management")
        print("4. Exit")
        
        user_input: str = input().lower()
        
        match user_input:
            case '1':
                self.controller.navigate(ProfessorMenu(self.controller))
            case '2':
                self.controller.navigate(StudentMenu(self.controller))
            case '3':
                self.controller.navigate(ClassMenu(self.controller))
            case '4':
                self.controller.quit()
            case _:
                print("Invalid choice, please try again.")