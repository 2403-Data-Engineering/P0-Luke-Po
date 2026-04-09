from Service.CourseService import CourseService
from Model.Course import Course

class CourseController:
    def __init__(self, course_service: CourseService):
        self.course_service = course_service
        
    def get_course_service(self) -> CourseService:
        return self.course_service
    
    def add_student_to_course(self, student_id: int, course_id: int) -> None:
        return self.course_service.add_student_to_course(student_id, course_id)
    
    def remove_student_from_course(self, student_id: int, course_id: int) -> None:
        return self.course_service.remove_student_from_course(student_id, course_id)

    def create_course(self, course_data: Course) -> None:
        self.course_service.create_course(course_data)

    def get_course_by_id(self, course_id: int) -> Course:
        return self.course_service.get_course_by_id(course_id)

    def update_course(self, course_id: int, course_data: Course) -> None:
        self.course_service.update_course(course_id, course_data)

    def delete_course(self, course_id: int) -> None:
        self.course_service.delete_course(course_id)
    
    def get_all_courses(self) -> list[Course]:
        return self.course_service.get_all_courses()
    