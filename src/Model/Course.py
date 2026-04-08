from dataclasses import dataclass
import json



from Model.Professor import Professor
from Model.Student import Student

@dataclass
class Course:
    id : int
    name : str
    students : list[Student]
    professor : Professor
    
    def __init__(self, id: int, name: str, students: list[Student], professor: Professor):
        self.id = id
        self.name = name
        self.students = students
        self.professor = professor
    
    # Getters
    def get_course_id(self) -> int:
        return self.id
    def get_name(self) -> str:
        return self.name
    def get_students(self) -> list[Student]:
        return self.students
    def get_professor(self) -> Professor:
        return self.professor
    
    # Setters
    def set_course_id(self, id: int) -> None:
        self.id = id
    def set_name(self, name: str) -> None:
        self.name = name
    def set_students(self, students: list[Student]) -> None:
        self.students = students
    def set_professor(self, professor: Professor) -> None:
        self.professor = professor
        
        #adds to end of list
    def add_student_to_course(self, student) -> Student:
        self.students.append(student)
        return student
    
    def remove_student_to_course(self, student) -> Student:
        self.students.remove(student)
        return student
        
        
    def print_course(self) -> str:
        course_string = json.dumps(self, indent=None, default=lambda o: o.__dict__)
        return course_string
        