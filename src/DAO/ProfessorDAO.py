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
    
    def database_contains_professor(self, professor_id: int) -> bool:
        prof_id_list = map(lambda p:p.get_professor_id(), ProfessorDAO().get_all_professors())
        return professor_id in prof_id_list
    
    def get_professor_by_id(self, professor_id: int) -> Professor:
        """Retrieve a professor by its ID."""
        with db_connection_manager.get_connection() as connection:
            cursor = connection.cursor(dictionary=True) #type: ignore set setting to dictionary
            sql = "SELECT * FROM professor WHERE id = %s"
            cursor.execute(sql, [professor_id])
            return cursor.fetchone() # type: ignore

    def create_professor(self, professor_data: Professor) -> None:
        """Create a new professor."""
        professor_first_name = professor_data.get_first_name()
        professor_last_name = professor_data.get_last_name()
        professor_department = professor_data.get_department()
        professor_email = professor_data.get_email()
        with db_connection_manager.get_connection() as connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("INSERT INTO professor (first_name, last_name, department, email) VALUES (%(first_name)s, %(last_name)s, %(department)s, %(email)s)", {'first_name': professor_first_name, 'last_name': professor_last_name, 'department': professor_department, 'email': professor_email})
            
            new_id = cursor.lastrowid
            professor_data.set_professor_id(new_id)

    def update_professor(self, professor_data: Professor) -> None:
        professor_first_name = professor_data.get_first_name()
        professor_last_name = professor_data.get_last_name()
        professor_department = professor_data.get_department()
        professor_email = professor_data.get_email()
        with db_connection_manager.get_connection() as connection:
            cursor: MySQLCursor = connection.cursor(dictionary=True) # type: ignore
            cursor.execute("UPDATE professor SET first_name = %(first_name)s, last_name = %(last_name)s, department = %(department)s, email = %(email)s WHERE id = %(id)s", {'first_name': professor_first_name, 'last_name': professor_last_name, 'department': professor_department, 'email': professor_email, 'id': professor_data.get_professor_id()})

    def delete_professor(self, professor_id: int) -> None:
        with db_connection_manager.get_connection() as connection:
            cursor: MySQLCursor = connection.cursor(dictionary=True) # type: ignore
            cursor.execute("DELETE FROM professor WHERE id = %s", [professor_id])

