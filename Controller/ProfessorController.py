from .. import Service

class ProfessorController:
    def __init__(self, professor_service):
        self.professor_service = professor_service

    def create_professor(self, name, department):
        return self.professor_service.create_professor(name, department)

    def get_professor(self, professor_id):
        return self.professor_service.get_professor(professor_id)

    def update_professor(self, professor_id, name=None, department=None):
        return self.professor_service.update_professor(professor_id, name, department)

    def delete_professor(self, professor_id):
        return self.professor_service.delete_professor(professor_id)
    
    def get_all_professors(self):
        return self.professor_service.get_all_professors()