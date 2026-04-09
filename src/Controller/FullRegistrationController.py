
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
        
        
            
            
        