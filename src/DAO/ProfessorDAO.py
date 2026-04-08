from Model.Professor import Professor
from Database import db_connection_manager
from mysql.connector.cursor import MySQLCursor
class ProfessorDAO:
    
    def get_all_professors(self) -> list[Professor]:
        """Retrieve all professors in a list."""
        professor_list = []
        with db_connection_manager.get_connection() as connection:
            cursor: MySQLCursor = connection.cursor(dictionary=True)  # type: ignore
            sql = "SELECT * FROM professor"
            cursor.execute(sql)
            for row in cursor:
                professor_list.append(row)
            connection.close()
        return professor_list
    
    def get_professor_by_id(self, professor_id: int) -> Professor:
        """Retrieve a professor by its ID."""
        with db_connection_manager.get_connection() as connection:
            cursor = connection.cursor(dictionary=True) #type: ignore set setting to dictionary
            sql = "SELECT * FROM professor WHERE id = %s"
            cursor.execute(sql, [professor_id])
            return cursor.fetchone()

    def create_professor(self, professor_data: Professor) -> None:
        """Create a new professor."""
        with db_connection_manager.get_connection() as connection:
            cursor = connection.cursor(dictionary=True)
            # sql = "INSERT INTO course (course_data) VALUES (%(course_data)s)", {"course_data": course_data}
            cursor.execute("INSERT INTO professor (professor) VALUES (%(professor)s)", {"professor": professor_data})
            new_id = cursor.lastrowid
            professor_data.set_professor_id(new_id)

    def update_professor(self, professor_id: int, professor_data: Professor) -> None:
        pass

    def delete_professor(self, professor_id: int) -> None:
        pass

