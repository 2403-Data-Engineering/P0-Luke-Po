from Model.ParseJSON import ParseJSON
from Model.Professor import Professor

from .Menu import Menu
from Service.ProfessorService import ProfessorService

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
                self.controller.navigate(ProfessorMenu(self.controller))
            case '2':
                print("Creating a Professor...")
                print("Enter a Professor you want to create in the format required (JSON):")
                print("Note that the id inputted does not matter when creating a Professor")
                print("EXAMPLE:")
                print("""{"id": 0, "first_name": "Dummy", "last_name": "Professor", "department": "Science", "email": "dummyproff@university.com"}""")
                professor_input = input()
                try:
                    professor : Professor = ParseJSON.parse_professor(professor_input)
                    self.professor_controller.create_professor(professor)
                    print("Successfully created the Professor in the Database!")
                except Exception:
                    print("Could not parse the professor from input, Navigating back to Professor Menu")
                self.controller.navigate(ProfessorMenu(self.controller))
            case '3':
                print("Viewing a Specific Professor...")
                self.controller.navigate(ProfessorMenu(self.controller))
            case '4':
                print("Updating a Professor...")
                self.controller.navigate(ProfessorMenu(self.controller))
            case '5':
                print("Deleting a Professor...")
                self.controller.navigate(ProfessorMenu(self.controller))
            case '6':
                from Controller.Menus.MainMenu import MainMenu
                self.controller.navigate(MainMenu(self.controller))
            case _:
                print("Invalid choice, please try again.")