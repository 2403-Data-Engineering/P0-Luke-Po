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
                # try:
                student_id: int = int(input())
                student_dict = self.student_controller.get_student_by_id(student_id)
                student = Student(student_dict.get('id'), student_dict.get('first_name'), student_dict.get('last_name'), student_dict.get('year'), student_dict.get('major'), student_dict.get('email'))
                PrintReport.print_student_markdown_file(student, self.course_controller.student_enrollment_courses(student_id))
                    
                    # self.print_student_markdown_file(student_id)
                print("Successfully printed")
                # except Exception:
                #     print("error finding the student's enrollments")
                self.controller.navigate(ReportsMenu(self.controller))
                
            case '2':
                print("printing professor summary report")
                print("Enter the id of the professor")
                try:
                    prof_id = int(input())
                    self.print_student_markdown_file(prof_id)
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
                

    def print_student_markdown_file(self, student_id: int) -> None:
        student = self.student_controller.get_student_by_id(student_id)
        markdown_file = MdUtils(file_name="student_markdown_file", title="Student Enrollment Report")
        name = student.get_first_name() + " " + student.get_last_name() #name of the student up top
        student_id_str : str = "Student ID: " + str(student.get_student_id())
        student_year: str = "Year: " + str(student.get_year())
        student_major : str = "Major: " + student.get_major()
        student_email : str = "Email: " + student.get_email()
        markdown_file.new_header(level=1, title=name)
        markdown_file.new_header(level=2, title=student_id_str)
        markdown_file.new_header(level=5, title=student_year)
        markdown_file.new_header(level=5, title=student_major)
        markdown_file.new_header(level=5, title=student_email)
        
        markdown_file.new_line("")
        markdown_file.new_header(level=5, title='Courses being Taken:')
        courses = []
        
        for course in self.course_controller.get_all_courses():
            student_ids = []
            # make the list of students in the class
            for student in course.get_students():
                student_ids.append(student.get_student_id())
                # check if student is in the class
            if (student_id in student_ids):
                courses.append(course)
                
        markdown_file.new_list(courses)
        
                
        markdown_file.create_md_file() #print the file
        
        
    def print_professor_markdown_file(self, professor_id: int) -> None:
        
        professor = self.professor_controller.get_professor_by_id(professor_id)
        markdown_file = MdUtils(file_name="professor_report", title="Professor Summary Report")
        name = professor.get_first_name() + " " + professor.get_last_name() #name of the professor up top
        professor_id_str : str = "Professor ID: " + str(professor_id)
        professor_department: str = "Department: " + str(professor.get_department())
        professor_email : str = "Email: " + professor.get_email()
        
        markdown_file.new_header(level=1, title=name)
        markdown_file.new_header(level=2, title=professor_id_str)
        markdown_file.new_header(level=5, title=professor_department)
        markdown_file.new_header(level=5, title=professor_email)
        
        
        markdown_file.new_header(level=5, title='Courses being Taught:')
        courses = self.course_controller.get_all_courses()
        for course in courses:
            if (course.get_professor().get_professor_id() is professor_id):
                markdown_file.new_header(level=6, title='Course Enrollments: ' + str(course.get_name()))
                students = course.get_students() # now have the course's students
                student_strs = []
                for student in students:
                    #get the names of each student and
                    student_name = student.get_first_name() + " " + student.get_last_name()
                    student_strs.append(student_name)
                markdown_file.new_list(student_strs) #now make a list of all the students' names and convert it into an items list in markdown
        markdown_file.create_md_file() #print the file