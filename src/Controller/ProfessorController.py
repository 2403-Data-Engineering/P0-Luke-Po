from ..Service.ProfessorService import ProfessorService
from ..Model.Professor import Professor


class ProfessorController:
    def __init__(self, professor_service: ProfessorService):
        self.professor_service = professor_service
        
    def get_professor_service(self) -> ProfessorService:
        return self.professor_service

    def create_professor(self, professor_data: Professor) -> None:
        self.professor_service.create_professor(professor_data)

    def get_professor_by_id(self, professor_id: int) -> Professor:
        return self.professor_service.get_professor_by_id(professor_id)

    def update_professor(self, professor_id: int, professor_data: Professor) -> None:
        return self.professor_service.update_professor(professor_id, professor_data)

    def delete_professor(self, professor_id: int) -> None:
        return self.professor_service.delete_professor(professor_id)

    def get_all_professors(self) -> list[Professor]:
        return self.professor_service.get_all_professors()