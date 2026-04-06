from dataclasses import dataclass
import json

    
@dataclass
class Student:
    
    id : int
    first_name : str
    last_name : str
    year : int
    major : str
    email : str
    
    def __init__(self, id: int = 0, first_name: str = "Dummy", last_name: str = "Student", year: int = 0, major: str = "physics", email: str = "dummys@gmail.com"):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.major = major
        self.email = email
    
    # Getters
    def get_student_id(self) -> int:
        return self.id
    def get_first_name(self) -> str:
        return self.first_name
    def get_last_name(self) -> str:
        return self.last_name
    def get_year(self) -> int:
        return self.year
    def get_major(self) -> str:
        return self.major
    def get_email(self) -> str:
        return self.email
    
    # Setters
    def set_student_id(self, id: int) -> None:
        self.id = id
    def set_first_name(self, first_name: str) -> None:
        self.first_name = first_name
    def set_last_name(self, last_name: str) -> None:
        self.last_name = last_name
    def set_year(self, year: int) -> None:
        self.year = year
    def set_major(self, major: str) -> None:
        self.major = major
    def set_email(self, email: str) -> None:
        self.email = email

    def print_student(self) -> str:
        student_string = json.dumps(self, indent=None, default=lambda o: o.__dict__)
        return student_string