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
        """Create a new course."""
        with db_connection_manager.get_connection() as connection:
            cursor : MySQLCursor = connection.cursor(dictionary=True) # type: ignore
            # sql = "INSERT INTO course (course_data) VALUES (%(course_data)s)", {"course_data": course_data}
            cursor.execute("INSERT INTO course (course) VALUES (%(course)s)", {"course": course_data})
            connection.commit()
        return course_data
    
    def update_course(self, course_id: int, course_data: Course) -> None:
        """Update an existing course by its ID"""
        pass
    
    def delete_course(self, course_id: int) -> None:
        """Delete a course by its ID."""
        pass
    
