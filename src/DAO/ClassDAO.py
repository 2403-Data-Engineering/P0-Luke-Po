from ..Model.Class import Class
class ClassDAO:
    """Data Access Object for Class entities."""
    
    def get_by_id(self, class_id: int) -> Class:
        """Retrieve a class by its ID."""
        a = Class()
        return a
    
    def create_class(self, class_data: Class) -> Class:
        """Create a new class."""
        a = Class()
        return a
    
    def update_class(self, class_id: int, class_data: Class) -> None:
        """Update an existing class by its ID"""
        pass
    
    def delete_class(self, class_id: int) -> None:
        """Delete a class by its ID."""
        pass
    
    def get_all_classes(self) -> list[Class]:
        """Retrieve all classes."""
        a = Class()
        return [a]