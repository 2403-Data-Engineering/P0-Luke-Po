from ..Model.Student import Student
class StudentDAO:
    def create_student(self, student: Student) -> None:
        pass

    def get_student_by_id(self, student_id: int) -> Student:
        pass

    def update_student(self, student_id: int, updated_student: Student) -> None:
        pass

    def delete_student(self, student_id: int) -> None:
        pass

    def get_all_students(self) -> list[Student]:
        pass