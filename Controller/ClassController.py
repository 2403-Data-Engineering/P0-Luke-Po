from .. import Service

class ClassController:
    def __init__(self, class_service):
        self.class_service = class_service

    def create_class(self, class_data):
        return self.class_service.create_class(class_data)
    
    def get_class(self, class_id):
        return self.class_service.get_class_by_id(class_id)
    
    def update_class(self, class_id, class_data):
        return self.class_service.update_class(class_id, class_data)
    
    def delete_class(self, class_id):
        return self.class_service.delete_class(class_id)
    
    def get_all_classes(self):
        return self.class_service.get_all_classes()
    
    