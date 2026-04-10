from DAO.CourseDAO import CourseDAO
from Model.Course import Course
from Model.Student import Student
class CourseService:
    """Service layer for business logic related to Course operations."""
    
    def __init__(self, course_dao: CourseDAO):
        """
        Initialize the service with a CourseDAO.
        
        Args:
            course_dao: Data access object for Course entities
        """
        self.course_dao = course_dao
        
    def add_student_to_course(self, student_id: int, course_id: int) -> None:
        return self.course_dao.add_student_to_course(student_id, course_id)
    
    def remove_student_from_course(self, student_id: int, course_id: int) -> None:
        return self.course_dao.remove_student_from_course(student_id, course_id)
    
    def get_course_by_id(self, course_id: int) -> Course:
        """Retrieve a course by ID."""
        return self.course_dao.get_course_by_id(course_id)
    
    def create_course(self, course_data: Course) -> None:
        """Create a new course."""
        self.course_dao.create_course(course_data)
    
    def update_course(self, course_data: Course) -> None:
        """Update an existing course by its ID"""
        return self.course_dao.update_course(course_data)
    
    def delete_course(self, course_id: int) -> None:
        """Delete a course by ID."""
        return self.course_dao.delete_course(course_id)
    
    def get_all_courses(self) -> list[Course]:
        """Retrieve all courses."""
        return self.course_dao.get_all_courses()
    
    def student_enrollment_courses(self, student_id : int) -> list[Course]:
        return self.course_dao.student_enrollment_courses(student_id=student_id)
    
    def course_student_list(self, course_id: int) -> list[Student]:
        return self.course_dao.course_student_list(course_id)