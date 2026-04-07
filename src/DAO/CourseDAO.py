from ..Model.Course import Course
from ..Model.Student import Student
from ..Model.Professor import Professor
from ..Database import db_connection_manager
from mysql.connector.cursor import MySQLCursor
class CourseDAO:
    """Data Access Object for Course entities."""
    
    def get_all_courses(self) -> list[Course]:
        """Retrieve all courses."""
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
            cursor = connection.cursor()
            sql = "SELECT * FROM database"
            
        return a
    
    def create_course(self, course_data: Course) -> Course:
        """Create a new course."""
        a = Course()
        return a
    
    def update_course(self, course_id: int, course_data: Course) -> None:
        """Update an existing course by its ID"""
        pass
    
    def delete_course(self, course_id: int) -> None:
        """Delete a course by its ID."""
        pass
    
get_all_courses()