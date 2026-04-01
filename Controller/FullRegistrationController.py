
from Controller.Menus.Menu import Menu
from Controller.Menus.MainMenu import MainMenu
from Service.ProfessorService import ProfessorService
from Service.StudentService import StudentService
from Service.ClassService import ClassService
class FullRegistrationController():
    def __init__(self, professor_service: ProfessorService, student_service: StudentService, class_service: ClassService):
        self.professor_service = professor_service
        self.student_service = student_service
        self.class_service = class_service
        self.running = True
        self.Menu = MainMenu(self)
        
    def navigate(self, Menu: Menu):
        self.Menu = Menu
        
    def quit(self):
        self.running = False
        print("Shutting down...")