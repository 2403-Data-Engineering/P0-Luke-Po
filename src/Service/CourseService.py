from DAO.CourseDAO import ClassDAO
from Model.Course import Course
class CourseService:
    """Service layer for business logic related to Class operations."""
    
    def __init__(self, class_dao: ClassDAO):
        """
        Initialize the service with a class_dao.
        
        Args:
            class_dao: Data access object for Class entities
        """
        self.class_dao = class_dao
    
    def get_course_by_id(self, course_id: int) -> Course:
        """Retrieve a course by ID."""
        return self.class_dao.get_by_id(course_id)
    
    def create_course(self, course_data: Course) -> Course:
        """Create a new course."""
        return self.class_dao.create_class(course_data)
    
    def update_course(self, course_id: int, course_data: Course) -> None:
        """Update an existing course by its ID"""
        return self.class_dao.update_class(course_id, course_data)
    
    def delete_course(self, course_id: int) -> None:
        """Delete a course by ID."""
        return self.class_dao.delete_class(course_id)
    
    def get_all_courses(self) -> list[Course]:
        """Retrieve all courses."""
        return self.class_dao.get_all_classes()