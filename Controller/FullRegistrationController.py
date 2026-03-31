
from Controller.Menu.menu import Menu
from Controller.Menu.MainMenu import MainMenu


class FullRegistrationController():
    def __init__(self, ProfessorService, StudentService, ClassService):
        self.professor_service = ProfessorService
        self.student_service = StudentService
        self.class_service = ClassService
        self.running = True
        self.menu = MainMenu(self)
        
    def navigate(self, menu: Menu):
        self.menu = menu
        
    def quit(self):
        self.running = False
        print("Shutting down...")