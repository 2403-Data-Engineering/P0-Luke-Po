from json import JSONDecodeError

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
                except JSONDecodeError:
                    print("Unable to Parse, Navigating back to the Professor Menu")
                except Exception:
                    print("An Error Occurred, Navigating back to Professor Menu")
                self.controller.navigate(ProfessorMenu(self.controller))
            case '3':
                print("Viewing a Specific Professor...")
                print("Enter the professor id of the professor you want to view:")
                professor_id_input = int(input()) #get the professor id from input
                #find the professor from id
                professor : Professor = self.professor_controller.get_professor_by_id(professor_id_input)
                if (professor is None):
                    print("An Error Occured, Navigating back to the Professor Menu")
                else:
                    print(professor)
                self.controller.navigate(ProfessorMenu(self.controller))
            case '4':
                print("Updating a Professor...")
                print("Enter the Professor you want to update in the format required (JSON) (Remember to use double quotes for every field and string)")
                print("The format is listed below:")
                print("""{"id": 1, "first_name": "Luke", "last_name": "Po", "department": "Magic", "email": "luke486@revature.net"}""")
                try:
                    professor : Professor = ParseJSON.parse_professor(input())
                    self.professor_controller.update_professor(professor)
                    print("Update Complete!")
                except JSONDecodeError:
                    print("Unable to Parse, Navigating back to the Professor Menu")
                except Exception:
                    print("An Error Occured, Navigating back to the Professor Menu")
                self.controller.navigate(ProfessorMenu(self.controller))
            case '5':
                print("Deleting a Professor...")
                print("Enter the Professor ID of the Professor you wish to delete")
                professor_id = int(input())
                try:
                    self.professor_controller.delete_professor(professor_id)
                    print("Deletion Complete!")
                except Exception:
                    print("Unable to delete specified Student")
                self.controller.navigate(ProfessorMenu(self.controller))
            case '6':
                from Controller.Menus.MainMenu import MainMenu
                self.controller.navigate(MainMenu(self.controller))
            case _:
                print("Invalid choice, please try again.")