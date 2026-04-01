from DAO.ProfessorDAO import ProfessorDAO
from Model.Professor import Professor

class ProfessorService:
    def __init__(self, professor_dao: ProfessorDAO):
        self.professor_dao = professor_dao

    def get_professor_by_id(self, professor_id: int) -> Professor:
        return self.professor_dao.get_professor_by_id(professor_id)


    def create_professor(self, professor_data: Professor) -> Professor:
        return self.professor_dao.create_professor(professor_data)

    def update_professor(self, professor_id: int, professor_data: Professor) -> Professor:
        return self.professor_dao.update_professor(professor_id, professor_data)

    def delete_professor(self, professor_id: int) -> None:
        return self.professor_dao.delete_professor(professor_id)

    def get_all_professors(self) -> list[Professor]:
        return self.professor_dao.get_all_professors()