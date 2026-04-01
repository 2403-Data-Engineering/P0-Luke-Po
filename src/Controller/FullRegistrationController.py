
from Controller.Menus.Menu import Menu
from Controller.Menus.MainMenu import MainMenu
from Service.ProfessorService import ProfessorService
from Service.StudentService import StudentService
from Service.ClassService import ClassService
from Controller.ClassController import ClassController
from Controller.ProfessorController import ProfessorController
from Controller.StudentController import StudentController

class FullRegistrationController():
    # def __init__(self, professor_service: ProfessorService, student_service: StudentService, class_service: ClassService):
    #     self.professor_service = professor_service
    #     self.student_service = student_service
    #     self.class_service = class_service
    #     self.running = True
    #     self.menu = MainMenu(self)
        
    def __init__(self, professor_controller: ProfessorController, student_controller: StudentController, class_controller: ClassController):
        self.professor_controller = professor_controller
        self.student_controller = student_controller
        self.class_controller = class_controller
        self.running = True
        self.menu = MainMenu(self)
        
    def get_controllers(self) -> list:
        return [self.professor_controller, self.student_controller, self.class_controller]

    def navigate(self, menu: Menu) -> None:
        self.menu = menu
        
    def quit(self):
        self.running = False
        print("Shutting down...")
        
        
    