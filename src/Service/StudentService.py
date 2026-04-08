from DAO.StudentDAO import StudentDAO
from Model.Student import Student

class StudentService:
    def __init__(self, student_dao: StudentDAO):
        self.student_dao = student_dao

    def create_student(self, student: Student) -> None:
        self.student_dao.create_student(student)

    def get_student_by_id(self, student_id: int) -> Student:
        return self.student_dao.get_student_by_id(student_id)

    def update_student(self, updated_student: Student) -> None:
        self.student_dao.update_student(updated_student)

    def delete_student(self, student_id: int) -> None:
        self.student_dao.delete_student(student_id)

    def get_all_students(self) -> list[Student]:
        return self.student_dao.get_all_students()