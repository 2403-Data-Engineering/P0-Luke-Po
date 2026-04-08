from ..Model.Student import Student
from ..Database import db_connection_manager
from mysql.connector.cursor import MySQLCursor
class StudentDAO:
    
    def get_all_students(self) -> list[Student]:
        """Retrieve all students in a list."""
        student_list = []
        with db_connection_manager.get_connection() as connection:
            cursor: MySQLCursor = connection.cursor(dictionary=True) # type: ignore
            sql = "SELECT * FROM student"
            cursor.execute(sql)
            for row in cursor:
                student_list.append(row)
            connection.close()
        return student_list
    
    def get_student_by_id(self, student_id: int) -> Student:
        """Retrieve a student by its ID."""
        with db_connection_manager.get_connection() as connection:
            cursor: MySQLCursor = connection.cursor(dictionary=True) # type: ignore
            sql = "SELECT * FROM student WHERE id = %(student_id)s"
            cursor.execute(sql, {'student_id': student_id})
        return cursor.fetchone()
    
    def create_student(self, student_data: Student) -> None:
        student_first_name = student_data.get_first_name()
        student_last_name = student_data.get_last_name()
        student_year = student_data.get_year()
        student_major = student_data.get_major()
        student_email = student_data.get_email()
        """Create a new student."""
        with db_connection_manager.get_connection() as connection:
            cursor : MySQLCursor = connection.cursor(dictionary=True) # type: ignore
            # sql = "INSERT INTO course (course_data) VALUES (%(course_data)s)", {"course_data": course_data}
            cursor.execute("INSERT INTO student (first_name, last_name, year, major, email) VALUES (%(first_name)s, %(last_name)s, %(year)s, %(major)s, %(email)s)", {'first_name': student_first_name, 'last_name': student_last_name, 'year': student_year, 'major': student_major, 'email': student_email})
            new_id = cursor.lastrowid
            student_data.set_student_id(new_id)

    def update_student(self, student_id: int, updated_student: Student) -> None:
        student_first_name = updated_student.get_first_name()
        student_last_name = updated_student.get_last_name()
        student_year = updated_student.get_year()
        student_major = updated_student.get_major()
        student_email = updated_student.get_email()
        with db_connection_manager.get_connection() as connection:
            cursor: MySQLCursor = connection.cursor(dictionary=True) # type: ignore
            cursor.execute("UPDATE student SET first_name = %(first_name)s, last_name = %(last_name)s, year = %(year)s, major = %(major)s, email = %(email)s WHERE id = %(id)s", {'first_name': student_first_name, 'last_name': student_last_name, 'year': student_year, 'major': student_major, 'email': student_email, 'id': updated_student.get_student_id()})
        

    def delete_student(self, student_id: int) -> None:
        with db_connection_manager.get_connection() as connection:
            cursor: MySQLCursor = connection.cursor(dictionary=True) # type: ignore
            cursor.execute("DELETE FROM student WHERE id = %s", [student_id])
        
            