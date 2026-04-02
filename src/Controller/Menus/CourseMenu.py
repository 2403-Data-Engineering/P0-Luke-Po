from Controller.Menus.MainMenu import MainMenu
from Model.ParseJSON import ParseJSON
from ...Service.CourseService import CourseService
from FullRegistrationController import FullRegistrationController
from ...Model.Course import Course
from ...Model.Student import Student
from ...Model.Professor import Professor
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
                print("Enter a the course you want to create in the format required:")
                print("Course Name, Professor ID")
                
                course_input = input().split(",")
                
                #TODO: Still need to check whether professor id is valid
                self.course_controller.create_course(Course(0, course_input[0], [], Professor(int(course_input[1]))))
                
                # try:
                #     self.course_controller.create_course(Course(course_input[0], course_input[1], int(course_input[2])))
                # except Exception as e:
                #     print("Error creating course, going back to Course Menu")
                # else:
                #     print("Course created successfully!")
                    
                    
                self.controller.navigate(CourseMenu(self.controller))
            case '3':
                print("Viewing a Specific Course...")
                print("Enter the course id of the course you want to view:")
                course_id_input = input()
                
                c = self.course_controller.get_course_by_id(int(course_id_input))
                print(c)
                self.controller.navigate(CourseMenu(self.controller))
            case '4':
                print("Updating a Course...")
                print("Enter the course you want to update in the format required:")
                print("Course ID, Course Name, Professor ID")
                print("EX: 0, Intro to Computer Science, 0")

            case '5':
                print("Deleting a Course...")
                print("Enter the course id of the course you want to delete:")
                print("Course ID")
                course_input = input()
                self.course_controller.get_course_service().delete_course(ParseJSON.parse_course(course_input))
                self.controller.navigate(CourseMenu(self.controller))
            case '6':
                self.controller.navigate(MainMenu(self.controller))
            case _:
                print("Invalid choice, please try again.")
                self.controller.navigate(CourseMenu(self.controller))
        