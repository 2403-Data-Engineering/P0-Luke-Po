
from Controller.Menus.Menu import Menu
from Controller.Menus.MainMenu import MainMenu
from Service.ProfessorService import ProfessorService
from Service.StudentService import StudentService
from Service.CourseService import CourseService
from Controller.CourseController import CourseController
from Controller.ProfessorController import ProfessorController
from Controller.StudentController import StudentController

class FullRegistrationController():
    # def __init__(self, professor_service: ProfessorService, student_service: StudentService, course_service: CourseService):
    #     self.professor_service = professor_service
    #     self.student_service = student_service
    #     self.course_service = course_service
    #     self.running = True
    #     self.menu = MainMenu(self)
        
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
        
        
    