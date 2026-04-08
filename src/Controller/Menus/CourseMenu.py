from Controller.Menus.MainMenu import MainMenu
from Model.ParseJSON import ParseJSON
from Service.CourseService import CourseService
from Model.Course import Course
from Model.Student import Student
from Model.Professor import Professor
from .Menu import Menu
import json
class CourseMenu(Menu):
    def __init__(self, controller):
        super().__init__(controller)
        self.course_controller = self.controller.course_controller
        
    def render(self) -> None:
        print("Welcome to the course Menu. Please select an option:")
        print("1. View all coursees")
        print("2. Create a course")
        print("3. View a course")
        print("4. Update a course")
        print("5. Delete a course")
        print("6. Go Back to the Main Menu")
        
        user_input = input().lower()
        
        match user_input:
            case '1':
                print("Viewing all coursees...")
                #need to call the FullRegistrationController's course service
                courses = self.course_controller.get_all_courses()
                for c in courses:
                    print(c)
                self.controller.navigate(CourseMenu(self.controller))
            case '2':
                print("Creating a Course...")
                print("Enter a the course you want to create in the format required (JSON):")
                print("""{"id": 0, "name": "Dummy Class", "students": [{"id": 0, "first_name": "Dummy", "last_name": "Student", "year": 0, "major": "Physics", "email": "dummys@gmail.com"}], "professor": {"id": 0, "first_name": "Dummy", "last_name": "Professor", "department": "Department", "email": "dummyprofessor@gmail.com"}}""")

                course_input = input()
                #TODO: Still need to check whether every id is valid and everything is valid
                self.course_controller.create_course(ParseJSON.parse_course(course_input))
                
                try:
                    course : Course = ParseJSON.parse_course(course_input)
                    self.course_controller.create_course(course)
                    print("Successfully created the Course in the Database!")
                except json.JSONDecodeError:
                    print("Unable to Parse, Navigating back to the Course Menu")
                except Exception:
                    print("An Error Occurred, Navigating back to Course Menu")
                self.controller.navigate(CourseMenu(self.controller))
            case '3':
                print("Viewing a Specific Course...")
                print("Enter the course id of the course you want to view:")
                course_id_input = int(input())
                
                course : Course = self.course_controller.get_course_by_id(course_id_input)
                if (course is None):
                    print("An Error Occured, Navigating back to the Course Menu")
                else:
                    course.print_course()
                self.controller.navigate(CourseMenu(self.controller))
            case '4':
                print("Updating a Course...")
                print("Enter the course you want to update in the format required (JSON):")
                print("""{"id": 0, "name": "Dummy Class", "students": [{"id": 0, "first_name": "Dummy", "last_name": "Student", "year": 0, "major": "Physics", "email": "dummys@gmail.com"}], "professor": {"id": 0, "first_name": "Dummy", "last_name": "Professor", "department": "Department", "email": "dummyprofessor@gmail.com"}}""")

            #only need id for deletion
            case '5':
                print("Deleting a Course...")
                print("Enter the course id of the course you want to delete:")
                print("Course ID")
                course_input = input()
                self.course_controller.get_course_service().delete_course(int(course_input))
                self.controller.navigate(CourseMenu(self.controller))
            case '6':
                self.controller.navigate(MainMenu(self.controller))
            case _:
                print("Invalid choice, please try again.")
                self.controller.navigate(CourseMenu(self.controller))
                
    def render_course(self) -> None:
        print("Welcome to the Specific Course Menu. Please select an option:")
        print("1. Add a student to this course")
        print("2. Remove a Student from this course")
        print("3. Go Back to the Main Menu")
        user_input = input().lower
        match user_input:
            case '1':
                #TODO
                pass
            case '2':
                #TODO
                pass
            case '3':
                from Controller.Menus.MainMenu import MainMenu
                self.controller.navigate(MainMenu(self.controller))
            case _:
                print("Invalid choice, please try again")
                self.controller.navigate(CourseMenu(self.controller))
        
