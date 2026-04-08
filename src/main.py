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
        
        print("quitting application")
        
        #python project is separate set of files, but they could be not linked to the rest of the project
        # controller = FullRegistrationController(ProfessorService(ProfessorDAO()), StudentService(StudentDAO()), ClassService(ClassDAO()))

        # while(controller.running):
        #     controller.menu.render()
            
        # print("quitting application...")
        
        
        # student = Student()
        # course = Course()
        # prof = Professor()
        # print(student.print_student())
        # print(course.print_course())
        # print(prof.print_professor())
        
        # print(ParseJSON.parse_student(student.print_student()))
        # print(ParseJSON.parse_professor(prof.print_professor()))
        # print(ParseJSON.parse_course(course.print_course()))
        # course.add_student_to_course(Student(1, "student2", "test", 1, "CS", "asdfsad"))
        # print(ParseJSON.parse_course(course.print_course()))

        
        # controller = FullRegistrationController(ProfessorController(ProfessorService(ProfessorDAO())), StudentController(StudentService(StudentDAO())), CourseController(CourseService(CourseDAO())))
        
        # controller.print_student_markdown_file(student)
