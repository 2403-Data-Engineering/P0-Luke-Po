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
            sql = "SELECT * FROM student WHERE id = %s"
            cursor.execute(sql, [student_id])
        return cursor.fetchone()
    
    def create_student(self, student_data: Student) -> Student:
        """Create a new student."""
        with db_connection_manager.get_connection() as connection:
            cursor : MySQLCursor = connection.cursor(dictionary=True) # type: ignore
            # sql = "INSERT INTO course (course_data) VALUES (%(course_data)s)", {"course_data": course_data}
            cursor.execute("INSERT INTO student (student) VALUES (%(student)s)", {"student": student_data})
        return student_data

    def update_student(self, student_id: int, updated_student: Student) -> None:
        pass

    def delete_student(self, student_id: int) -> None:
        pass