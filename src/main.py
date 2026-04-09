import json
from Model.Professor import Professor
from Model.Student import Student
from Model.Course import Course
from Model.ParseJSON import ParseJSON

from DAO.CourseDAO import CourseDAO
from DAO.ProfessorDAO import ProfessorDAO
from DAO.StudentDAO import StudentDAO

from Service.ProfessorService import ProfessorService
from Service.StudentService import StudentService
from Service.CourseService import CourseService

from Controller.CourseController import CourseController
from Controller.ProfessorController import ProfessorController
from Controller.StudentController import StudentController
from Controller.FullRegistrationController import FullRegistrationController



class main:
    if __name__ == "__main__": #means executing from this file -> standard way to begin an application -> start running from this file anywhere
        professor_dao = ProfessorDAO()
        student_dao = StudentDAO()
        course_dao = CourseDAO()
        
        professor_service = ProfessorService(professor_dao)
        student_service = StudentService(student_dao)
        course_service = CourseService(course_dao)
        
        professor_controller = ProfessorController(professor_service)
        student_controller = StudentController(student_service)
        course_controller = CourseController(course_service)
        controller = FullRegistrationController(professor_controller, student_controller, course_controller)
        
        while(controller.running):
            controller.menu.render()
        
        print("Quitting Application")
