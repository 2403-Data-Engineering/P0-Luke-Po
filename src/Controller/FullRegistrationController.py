
from Controller.Menus.Menu import Menu
from Controller.Menus.MainMenu import MainMenu
from Service.ProfessorService import ProfessorService
from Service.StudentService import StudentService
from Service.CourseService import CourseService
from Controller.CourseController import CourseController
from Controller.ProfessorController import ProfessorController
from Controller.StudentController import StudentController
from Model.Course import Course
from Model.Student import Student
from Model.Professor import Professor
from mdutils.mdutils import MdUtils
class FullRegistrationController():
        
    def __init__(self, professor_controller: ProfessorController, student_controller: StudentController, course_controller: CourseController):
        self.professor_controller = professor_controller
        self.student_controller = student_controller
        self.course_controller = course_controller
        self.running = True
        self.menu = MainMenu(self)
        
    def get_controllers(self) -> list:
        return [self.professor_controller, self.student_controller, self.course_controller]

    def navigate(self, menu: Menu) -> None:
        self.menu = menu
        
    def quit(self):
        self.running = False
        print("Shutting down...")
        
        
    def print_student_markdown_file(self, student: Student) -> None:
        markdown_file = MdUtils(file_name="database_markdown_file", title="Student Enrollment Report")
        name = student.get_first_name() + student.get_last_name() #name of the student up top
        markdown_file.new_header(level=1, title=name)
        student_id = student.get_student_id()
        for course in self.course_controller.get_all_courses():
            #use map function
            student_ids = map(lambda x: x.get_student_id(), course.get_students())
            if (student_id in student_ids):
                markdown_file.new_header(level=1, title=course.get_name())
                markdown_file.new_line("")
                
        markdown_file.create_md_file() #print the file
            
            
        