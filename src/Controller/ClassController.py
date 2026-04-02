from ..Service.ClassService import ClassService
from ..Model.Course import Course

class ClassController:
    def __init__(self, class_service: ClassService):
        self.class_service = class_service
        
    def get_class_service(self) -> ClassService:
        return self.class_service

    def create_class(self, class_data: Course) -> Course:
        return self.class_service.create_class(class_data)

    def get_class_by_id(self, class_id: int) -> Course:
        return self.class_service.get_class_by_id(class_id)

    def update_class(self, class_id: int, class_data: Course) -> None:
        return self.class_service.update_class(class_id, class_data)

    def delete_class(self, class_id: int) -> None:
        return self.class_service.delete_class(class_id)
    
    def get_all_classes(self) -> list[Course]:
        return self.class_service.get_all_classes()
    
    