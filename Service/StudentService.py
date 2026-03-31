class StudentService:
    def __init__(self, StudentDAO):
        self.StudentDAO = StudentDAO

    def add_student(self, student):
        self.StudentDAO.add(student)

    def get_student(self, student_id):
        return self.StudentDAO.get(student_id)

    def update_student(self, student_id, updated_student):
        self.StudentDAO.update(student_id, updated_student)

    def delete_student(self, student_id):
        self.StudentDAO.delete(student_id)

    def get_all_students(self):
        return self.StudentDAO.get_all_students()