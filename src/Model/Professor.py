from dataclasses import dataclass
import json


@dataclass
class Professor:
    
    id : int
    first_name : str
    last_name : str
    department : str
    email : str
    
    def __init__(self, id: int=0, first_name: str="Dummy", last_name: str="Professor", department: str="Department", email: str="dummyprofessor@gmail.com"):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.email = email
        
    # Getters
    def get_professor_id(self) -> int:
        return self.id
    def get_first_name(self) -> str:
        return self.first_name
    def get_last_name(self) -> str:
        return self.last_name
    def get_department(self) -> str:
        return self.department
    def get_email(self) -> str:
        return self.email
    
    # Setters
    def set_professor_id(self, id: int) -> None:
        self.id = id
    def set_first_name(self, first_name: str) -> None:
        self.first_name = first_name
    def set_last_name(self, last_name: str) -> None:
        self.last_name = last_name
    def set_department(self, department: str) -> None:
        self.department = department
    def set_email(self, email: str) -> None:
        self.email = email
        
    def print_professor(self) -> str:
        professor_string = json.dumps(self, indent=None, default=lambda o: o.__dict__)
        return professor_string