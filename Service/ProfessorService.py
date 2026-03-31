from .. import DAO

class ProfessorService:
    def __init__(self, ProfessorDAO):
        self.ProfessorDAO = ProfessorDAO

    def get_professor_by_id(self, professor_id):
        return self.ProfessorDAO.get_professor_by_id(professor_id)


    def create_professor(self, professor_data):
        return self.ProfessorDAO.create_professor(professor_data)

    def update_professor(self, professor_id, professor_data):
        return self.ProfessorDAO.update_professor(professor_id, professor_data)

    def delete_professor(self, professor_id):
        return self.ProfessorDAO.delete_professor(professor_id)
    
    def get_all_professors(self):
        return self.ProfessorDAO.get_all_professors()