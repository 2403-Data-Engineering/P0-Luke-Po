from ..Model.Course import Course
class ClassDAO:
    """Data Access Object for Class entities."""
    
    def get_by_id(self, class_id: int) -> Course:
        """Retrieve a class by its ID."""
        a = Course()
        return a
    
    def create_class(self, class_data: Course) -> Course:
        """Create a new class."""
        a = Course()
        return a
    
    def update_class(self, class_id: int, class_data: Course) -> None:
        """Update an existing class by its ID"""
        pass
    
    def delete_class(self, class_id: int) -> None:
        """Delete a class by its ID."""
        pass
    
    def get_all_classes(self) -> list[Course]:
        """Retrieve all classes."""
        a = Course()
        return [a]