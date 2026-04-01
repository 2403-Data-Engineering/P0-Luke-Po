from DAO.ClassDAO import ClassDAO
from Model.Class import Class
class ClassService:
    """Service layer for business logic related to Class operations."""
    
    def __init__(self, class_dao: ClassDAO):
        """
        Initialize the service with a class_dao.
        
        Args:
            class_dao: Data access object for Class entities
        """
        self.class_dao = class_dao
    
    def get_class_by_id(self, class_id: int) -> Class:
        """Retrieve a class by ID."""
        return self.class_dao.get_by_id(class_id)
    
    def create_class(self, class_data: Class) -> Class:
        """Create a new class."""
        return self.class_dao.create(class_data)
    
    def update_class(self, class_id: int, class_data: Class) -> Class:
        """Update an existing class by its ID"""
        return self.class_dao.update(class_id, class_data)
    
    def delete_class(self, class_id: int) -> None:
        """Delete a class by ID."""
        return self.class_dao.delete(class_id)
    
    def get_all_classes(self) -> list[Class]:
        """Retrieve all classes."""
        return self.class_dao.get_all()