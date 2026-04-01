from Controller.FullRegistrationController import FullRegistrationController

from Model.Class import Class
from Model.Professor import Professor
from Model.Student import Student

from DAO.ClassDAO import ClassDAO
from DAO.ProfessorDAO import ProfessorDAO
from DAO.StudentDAO import StudentDAO

from Service.ProfessorService import ProfessorService
from Service.StudentService import StudentService
from Service.ClassService import ClassService

from Controller.ClassController import ClassController
from Controller.ProfessorController import ProfessorController
from Controller.StudentController import StudentController

class main:
    if __name__ == "__main__": #means executing from this file -> standard way to begin an application -> start running from this file anywhere
        #python project is separate set of files, but they could be not linked to the rest of the project
        # controller = FullRegistrationController(ProfessorService(ProfessorDAO()), StudentService(StudentDAO()), ClassService(ClassDAO()))
        controller = FullRegistrationController(ProfessorController(ProfessorService(ProfessorDAO())), StudentController(StudentController(StudentService(StudentDAO()))), ClassController(ClassController(ClassService(ClassDAO()))))
        while(controller.running):
            controller.menu.render()
            
        print("quitting application...")