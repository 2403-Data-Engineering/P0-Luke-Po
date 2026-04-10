from Controller.Menus.MainMenu import MainMenu
from Model.ParseJSON import ParseJSON
from Service.CourseService import CourseService
from Model.Course import Course
from Model.Student import Student
from Model.Professor import Professor
from .Menu import Menu
import json
from mdutils.mdutils import MdUtils
from Scripts.PrintReport import PrintReport

class ReportsMenu(Menu):
    def __init__(self, controller):
        super().__init__(controller)
        self.professor_controller = self.controller.professor_controller
        self.student_controller = self.controller.student_controller
        self.course_controller = self.controller.course_controller
        
    def render(self) -> None:
        print("Welcome to the Reports Menu. Please select an option:")
        print("1. Generate Enrollment Report for Course")
        print("2. Generate Professor Enrollment Report")
        print("3. Go Back to the Main Menu")
        
        user_input = input().lower()
        match user_input:
            case '1':
                print("printing enrollment report for a student")
                print("Enter the id of the student")
                try:
                    student_id: int = int(input())
                    student_dict = self.student_controller.get_student_by_id(student_id)
                    student = Student(student_dict.get('id'), student_dict.get('first_name'), student_dict.get('last_name'), student_dict.get('year'), student_dict.get('major'), student_dict.get('email'))
                    PrintReport.print_student_markdown_file(student, self.course_controller.student_enrollment_courses(student_id))
                    print("Successfully printed")
                except Exception:
                    print("error finding the student's enrollments")
                self.controller.navigate(ReportsMenu(self.controller))
                
            case '2':
                print("printing professor summary report")
                print("Enter the id of the professor")
                try:
                    prof_id = int(input())
                    prof_dict = self.professor_controller.get_professor_by_id(prof_id)
                    prof = Professor(prof_dict.get('id'), prof_dict.get('first_name'), prof_dict.get('last_name'), prof_dict.get('department'), prof_dict.get('email'))
                    all_courses = self.course_controller.get_all_courses()
                    PrintReport.print_professor_markdown_file(prof, all_courses, self.course_controller)
                    # self.print_student_markdown_file(prof_id)
                    print("Successfully printed")
                except Exception:
                    print("error printing")
                
                self.controller.navigate(ReportsMenu(self.controller))
                
            case '3':
                self.controller.navigate(MainMenu(self.controller))
            case 'q':
                self.controller.quit()
                
            case _:
                print("Invalid choice, please try again.")
                self.controller.navigate(ReportsMenu(self.controller))
                