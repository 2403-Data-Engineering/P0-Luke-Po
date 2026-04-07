from ..Model.Course import Course
from ..Model.Student import Student
from ..Model.Professor import Professor
from ..Database import db_connection_manager
from mysql.connector.cursor import MySQLCursor
class CourseDAO:
    """Data Access Object for Course entities."""
    
    def get_all_courses(self) -> list[Course]:
        """Retrieve all courses in a list."""
        course_list = []
        with db_connection_manager.get_connection() as connection:
            cursor: MySQLCursor = connection.cursor(dictionary=True) # type: ignore
            sql = "SELECT * FROM course"
            cursor.execute(sql)
            for row in cursor:
                course_list.append(row)
            connection.close()
        
        return course_list
            
    
    def get_course_by_id(self, course_id: int) -> Course:
        """Retrieve a course by its ID."""
        with db_connection_manager.get_connection() as connection:
            cursor : MySQLCursor = connection.cursor(dictionary=True) # type: ignore
            sql = "SELECT * FROM course WHERE id = %s"
            cursor.execute(sql, [course_id])
        return cursor.fetchone()
    
    def create_course(self, course_data: Course) -> Course:
        course_name = course_data.get_name()
        course_students = course_data.get_students()
        course_professor = course_data.get_professor()
        """Create a new course."""
        with db_connection_manager.get_connection() as connection:
            cursor : MySQLCursor = connection.cursor(dictionary=True) # type: ignore
            # sql = "INSERT INTO course (course_data) VALUES (%(course_data)s)", {"course_data": course_data}
            cursor.execute("INSERT INTO course (name, students, professor) VALUES (%(name)s, %(students)s, %(professor)s)", {'name': course_name, 'students': course_students, 'professor': course_professor})
            connection.commit()
            new_id = cursor.lastrowid
        return course_data.set_course_id(new_id)
    
    def update_course(self, course_id: int, course_data: Course) -> None:
        course_name = course_data.get_name()
        course_students = course_data.get_students()
        course_professor = course_data.get_professor()
        """Update an existing course by its ID"""
        with db_connection_manager.get_connection() as connection:
            cursor : MySQLCursor = connection.cursor(dictionary=True) # type: ignore
            cursor.execute("UPDATE course SET name = %(course_name)s, students = %(course_students)s, professor = %(course_professor)s WHERE id = %(id)s", {'course_name' : course_name, 'course_students' : course_students, 'course_professor' : course_professor, 'id' : course_id })
    
    def delete_course(self, course_id: int) -> None:
        """Delete a course by its ID."""
        pass
    
