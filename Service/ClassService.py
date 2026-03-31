class ClassService:
    """Service layer for business logic related to Class operations."""
    
    def __init__(self, ClassDAO):
        """
        Initialize the service with a ClassDAO.
        
        Args:
            ClassDAO: Data access object for Class entities
        """
        self.ClassDAO = ClassDAO
    
    def get_class_by_id(self, class_id):
        """Retrieve a class by ID."""
        return self.ClassDAO.get_by_id(class_id)
    
    def create_class(self, class_data):
        """Create a new class."""
        return self.ClassDAO.create(class_data)
    
    def update_class(self, class_id, class_data):
        """Update an existing class."""
        return self.ClassDAO.update(class_id, class_data)
    
    def delete_class(self, class_id):
        """Delete a class by ID."""
        return self.ClassDAO.delete(class_id)
    
    def get_all_classes(self):
        """Retrieve all classes."""
        return self.ClassDAO.get_all()