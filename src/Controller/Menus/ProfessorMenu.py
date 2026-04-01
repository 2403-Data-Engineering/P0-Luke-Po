from .Menu import Menu
from Controller.Menus.MainMenu import MainMenu
from FullRegistrationController import FullRegistrationController
from ...Service.ProfessorService import ProfessorService


class ProfessorMenu(Menu):
    def __init__(self, controller):
        super().__init__(controller)
        self.professor_controller = self.controller.professor_controller
        
    def render(self) -> None:
        print("Welcome to the Professor Menu. Please select an option:")
        print("1. View all Professors")
        print("2. Create a Professor")
        print("3. View a specific Professor")
        print("4. Update a Professor")
        print("5. Delete a Professor")
        print("6. Go Back to the Main Menu")
        
        user_input = input().lower()
        match user_input:
            case '1':
                print("Viewing all Professors...")
                professors = self.professor_controller.get_professor_service().get_all_professors()
                for p in professors:
                    print(p)
            case '2':
                print("Creating a Professor...")
            case '3':
                print("Viewing a Specific Professor...")
            case '4':
                print("Updating a Professor...")
            case '5':
                print("Deleting a Professor...")
            case '6':
                self.controller.navigate(MainMenu(self.controller))
            case _:
                print("Invalid choice, please try again.")