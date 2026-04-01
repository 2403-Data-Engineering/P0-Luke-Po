from ..Model.Professor import Professor
class ProfessorDAO:
    def get_professor_by_id(self, professor_id: int) -> Professor:
        pass

    def create_professor(self, professor_data: Professor) -> Professor:
        pass

    def update_professor(self, professor_id: int, professor_data: Professor) -> Professor:
        pass

    def delete_professor(self, professor_id: int) -> None:
        pass

    def get_all_professors(self) -> list[Professor]:
        pass