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
        json_str = '{"id": 5, "name": "WonderClass", "students": [{"id": 2, "first_name": "Luke", "last_name": "Po", "year": 4, "major": "Computer Science", "email": "luke486@revature.net"}, {"id": 4, "first_name": "Dummy", "last_name": "Student", "year": 0, "major": "Physics", "email": "dummys@gmail.com"}], "professor": {"id": 12, "first_name": "Dummy", "last_name": "Professor", "department": "Department", "email": "dummyprofessor@gmail.com"}}'
        
        # ParseJSON.parse_course(json_str)        
        while(controller.running):
            controller.menu.render()
        
        print("Quitting Application")
