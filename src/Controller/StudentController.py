from ..Service.StudentService import StudentService

class StudentController:
    def __init__(self, student_service):
        self.student_service = student_service
        
    def get_student_service(self):
        return self.student_service

    def create_student(self, student_data):
        return self.student_service.create_student(student_data)

    def get_student_by_id(self, student_id):
        return self.student_service.get_student_by_id(student_id)

    def update_student(self, student_id, student_data):
        return self.student_service.update_student(student_id, student_data)

    def delete_student(self, student_id):
        return self.student_service.delete_student(student_id)

    def get_all_students(self):
        return self.student_service.get_all_students()
    