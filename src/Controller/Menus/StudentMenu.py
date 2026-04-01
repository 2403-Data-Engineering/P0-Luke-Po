from .Menu import Menu
from Controller.Menus.MainMenu import MainMenu
from FullRegistrationController import FullRegistrationController
from ...Service.StudentService import StudentService

class StudentMenu(Menu):
    def __init__(self, controller):
        super().__init__(controller)
        self.student_controller = self.controller.student_controller

    def render(self) -> None:
        print("Welcome to the Student Menu. Please select an option:")
        print("1. View All Students")
        print("2. Create a Student")
        print("3. View a Student")
        print("4. Update a Student")
        print("5. Delete a Student")
        print("6. Go Back to the Main Menu")
    
        user_input = input().lower()
        match user_input:
            case '1':
                print("Viewing all Students...")
                students = self.student_controller.get_student_service().get_all_students()
                for s in students:
                    print(s)
                self.controller.navigate(StudentMenu(self.controller))
            case '2':
                print("Creating a Student...")
            case '3':
                print("Viewing a Specific Student...")
            case '4':
                print("Updating a Student...")
            case '5':
                print("Deleting a Student...")
            case '6':
                self.controller.navigate(MainMenu(self.controller))
            case _:
                print("Invalid choice, please try again.")