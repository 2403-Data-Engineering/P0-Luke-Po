from ..Model.Professor import Professor
from ..Database import db_connection_manager
class ProfessorDAO:
    def get_professor_by_id(self, professor_id: int) -> Professor:
        pass

    def create_professor(self, professor_data: Professor) -> Professor:
        pass

    def update_professor(self, professor_id: int, professor_data: Professor) -> None:
        pass

    def delete_professor(self, professor_id: int) -> None:
        pass

    def get_all_professors(self) -> list[Professor]:
        professor_list = []
        with db_connection_manager.get_connection() as connection:
            cursor = connection.cursor(dictionary=True)
            sql = "SELECT * FROM professor"
            cursor.execute(sql)
            for row in cursor:
                print(row)
                professor_list.append(row)
            connection.close()
        return professor_list