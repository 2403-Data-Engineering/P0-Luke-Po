from Model.Class import Class
from enum import Enum
    
class Student:
    def __init__(self, id: int, first_name: str, last_name: str, year: int, major: str, email: str, classes: list[Class]):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.major = major
        self.email = email
        self.classes = classes
    
    # Getters
    def getStudentId(self) -> int:
        return self.id
    def getFirstName(self) -> str:
        return self.first_name
    def getLastName(self) -> str:
        return self.last_name
    def getYear(self) -> int:
        return self.year
    def getMajor(self) -> str:
        return self.major
    def getEmail(self) -> str:
        return self.email
    def getClasses(self) -> list[Class]:
        return self.classes
    
    # Setters
    def setStudentId(self, id: int) -> None:
        self.id = id
    def setFirstName(self, first_name: str) -> None:
        self.first_name = first_name
    def setLastName(self, last_name: str) -> None:
        self.last_name = last_name
    def setYear(self, year: int) -> None:
        self.year = year
    def setMajor(self, major: str) -> None:
        self.major = major
    def setEmail(self, email: str) -> None:
        self.email = email
    def setClasses(self, classes: list[Class]) -> None:
        self.classes = classes

