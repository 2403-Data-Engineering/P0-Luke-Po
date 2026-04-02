from ..Model.Course import Course
class CourseDAO:
    """Data Access Object for Course entities."""
    
    def get_course_by_id(self, course_id: int) -> Course:
        """Retrieve a course by its ID."""
        a = Course()
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
    
    def get_all_courses(self) -> list[Course]:
        """Retrieve all courses."""
        a = Course()
        return [a]