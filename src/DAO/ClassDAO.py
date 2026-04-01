from ..Model.Class import Class
class ClassDAO:
    """Data Access Object for Class entities."""
    
    def get_by_id(self, class_id: int) -> Class:
        """Retrieve a class by its ID."""
        pass
    
    def create(self, class_data: Class) -> Class:
        """Create a new class."""
        pass
    
    def update(self, class_id: int, class_data: Class) -> Class:
        """Update an existing class by its ID"""
        pass
    
    def delete(self, class_id: int) -> None:
        """Delete a class by its ID."""
        pass
    
    def get_all(self) -> list[Class]:
        """Retrieve all classes."""
        pass