from Model.Student import Student
from mdutils.mdutils import MdUtils

from Service.StudentService import StudentService

class StudentController:
    def __init__(self, student_service: StudentService):
        self.student_service = student_service
        
    def get_student_service(self):
        return self.student_service

    def create_student(self, student_data: Student) -> None:
        self.student_service.create_student(student_data)

    def get_student_by_id(self, student_id: int) -> Student:
        return self.student_service.get_student_by_id(student_id)
            

    def update_student(self, student_data: Student) -> None:
        return self.student_service.update_student(student_data)

    def delete_student(self, student_id: int) -> None:
        return self.student_service.delete_student(student_id)

    def get_all_students(self) -> list[Student]:
        return self.student_service.get_all_students()
    
