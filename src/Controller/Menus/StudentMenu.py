from json import JSONDecodeError

from .Menu import Menu
from Model.ParseJSON import ParseJSON
from Model.Student import Student
from Controller.Menus.MainMenu import MainMenu
from Service.StudentService import StudentService

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
                print("Enter a Student you want to create in the format required (JSON):")
                print("Note that the id inputted does not matter when creating a student")
                print("EXAMPLE:")
                print("""{"id": 0, "first_name": "Dummy", "last_name": "Student", "year": 0, "major": "Physics", "email": "dummys@gmail.com"}""")
                try:
                    student_input = input()
                    self.student_controller.create_student(ParseJSON.parse_student(student_input))
                    self.controller.navigate(StudentMenu(self.controller))
                except JSONDecodeError:
                    print("Error parsing input")
                except Exception:
                    print("Error creating student")
                    

            case '3':
                print("Viewing a Specific Student...")
                print("Enter the student id of the student you want to view:")
                student_id_input = int(input()) #get the student id from input
                #find the student from id
                student : Student = self.student_controller.get_student_by_id(student_id_input)
                if (student is None):
                    print("An Error Occured, Navigating back to the Student Menu")
                else:
                    print(student)
                self.controller.navigate(StudentMenu(self.controller))
            case '4':
                print("Updating a Student...")
                print("Enter the Student you want to update in the format required (JSON) (Remember to use double quotes for every field and string)")
                print("The format is listed below:")
                print("""{"id": 2, "first_name": "Luke", "last_name": "Po", "year": 4, "major": "Computer Science", "email": "luke486@revature.net"}""")
                try:
                    student : Student = ParseJSON.parse_student(input())
                    self.student_controller.update_student(student)
                    print("Update Complete!")
                except JSONDecodeError:
                    print("Unable to Parse, Navigating back to the Student Menu")
                except Exception:
                    print("An Error Occured, Navigating back to the Student Menu")
                self.controller.navigate(StudentMenu(self.controller))
            case '5':
                print("Deleting a Student...")
                print("Enter the Student ID of the Student you wish to delete")
                student_id_input = int(input())
                try:
                    self.student_controller.delete_student(student_id_input)
                except Exception:
                    print("Unable to delete specified Student")
                self.controller.navigate(StudentMenu(self.controller))
            case '6':
                from Controller.Menus.MainMenu import MainMenu
                self.controller.navigate(MainMenu(self.controller))
            case 'q':
                self.controller.quit()
            case _:
                print("Invalid choice, please try again.")